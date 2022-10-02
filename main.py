"""
Driver code
"""
import json
from covalent_api_lib import get_transactions


def main():
    """Driver code"""
    address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
    transaction = get_transactions(address)
    with open("transaction.json", "w", encoding="utf-8") as f:
        json.dump(transaction.json(), f)


if __name__ == "__main__":
    # TODO: look into Etherscan api
    # ref: https://etherscan.io/apis
    main()
