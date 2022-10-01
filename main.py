"""
Driver code
"""

from covalent_api_lib import get_transactions


def main():
    """Driver code"""
    address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
    trans = get_transactions(address)
    print(trans.status_code)
    print(trans.text[:50])


if __name__ == "__main__":
    main()
