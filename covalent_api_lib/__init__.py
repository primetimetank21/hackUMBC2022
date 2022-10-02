import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("COVALENT_KEY")
BASE_URL = "https://api.covalenthq.com"


def get_transactions(address) -> requests.Response:
    """Get transactions of a given ETH address"""
    transactions_endpoint = (
        BASE_URL + f"/v1/1/address/{address}/transactions_v2/?key={api_key}"
    )
    params = {"quote-currency": "USD", "no-logs": True}
    transactions = requests.get(transactions_endpoint, params=params, timeout=15)
    return transactions
