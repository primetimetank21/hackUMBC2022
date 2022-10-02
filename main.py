"""
Driver code
"""

# Imports
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from covalent_api_lib import get_transactions
from etherscan_lib import get_labels

# Create App Microservice
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# App Routes
@app.get("/")
async def landing_page():
    """Homepage of the TrustDeFi Platform"""
    return FileResponse("./images/logo.png")


@app.get("/transactions/{address}")
def get_trustworthiness(request: Request, address: str):
    """Display transactions and trustworthiness of an ETH Address"""
    transactions = get_transactions(address)
    transactions_json = transactions.json()["data"]
    labels = get_labels(address)

    for trans in transactions_json["items"]:
        rounded_quote = round(trans["value_quote"], 2)
        trans["value_quote"] = rounded_quote
        labels = [label.title() for label in labels]

    return templates.TemplateResponse(
        "transactions.html",
        {
            "request": request,
            "address": transactions_json["address"],
            "transactions": transactions_json["items"],
            "num_transactions": len(transactions_json["items"]),
            "labels": labels if len(labels) > 0 else ["No bad labels :)"]
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
