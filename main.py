import os
from dotenv import load_dotenv
import requests
import json

# from covalent_api.session import Session
# from covalent_api.class_a import ClassA

from covalent_api_lib import ETH_CHAINET_ID

def main():
    """Driver code"""
    api_key = os.getenv("COVALENT_KEY")
    address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
    server_url = "https://api.covalenthq.com"
    endpoint = f"/v1/1/address/{address}/transactions_v2/?key={api_key}"

    params = {
        'quote-currency': 'USD',
    }
    res = requests.get(server_url + endpoint, params=params, timeout=6)
    print(res.text)

    # session = Session(api_key=api_key)
    # print(f"Session url: {session.server_url}")
    # class_a = ClassA(session=session)
    # trans = class_a.get_transactions(ETH_CHAINET_ID, address)
    # print(trans)

    # "https://api.covalenthq.com/v1/1/address/0xa79E63e78Eec28741e711f89A672A4C40876Ebf3/transactions_v2/?key=ckey_f75b1b013edd4d5dbbbd4b6046b"
    # session.q)



if __name__ == "__main__":
    load_dotenv()
    main()