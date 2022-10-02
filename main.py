"""
Driver code
"""
# pylint: disable=unused-import
import json
from covalent_api_lib import get_transactions
from etherscan_lib import get_labels
import pandas as pd

import scipy
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Driver code"""
    address = "0x0E57edbA0FccB1E388926193c873120cab961fEe"
    transaction = get_transactions(address)
    with open("transaction.json", "w", encoding="utf-8") as f:
        json.dump(transaction.json(), f)

    labels = get_labels(address)
    print(labels)
    # with open("transaction.json", "r", encoding="utf-8") as f:
    #     transactions = json.load(f)
    # transaction_array = transactions["data"]["items"]
    # transaction_df = pd.DataFrame(transaction_array)
    # transaction_df.to_csv("transaction.csv")
    # transaction_df.drop(["from_address_label", "to_address_label"], axis=1)
    # print(transaction_df.head())


if __name__ == "__main__":
    # ref: https://etherscan.io/apis
    main()
