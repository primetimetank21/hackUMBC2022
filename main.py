"""
Driver code
"""


from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from covalent_api_lib import get_transactions
from etherscan_lib import get_labels


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root():
    return FileResponse("./images/logo.png")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, _id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": _id})


@app.get("/transactions/{address}")
def get_trustworthiness(request: Request, address: str):
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
            "labels": labels,
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
