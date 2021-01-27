import requests
import json
from datetime import datetime
from statistics import mean
from datetime import datetime


def get_total_sent(wallet_id) -> float:
    """
    Returns the total amount of bitcoin sent by a wallet.

    Parameters:
    wallet_id (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin sent from a wallet.
    """
    response = requests.get(
        f"https://blockchain.info/q/getsentbyaddress/{wallet_id}")
    # Convert from sats to btc divide by 100,000,000
    return int(response.json()) / 100000000


def get_total_received(wallet_id) -> float:
    """
    Returns the total amount of bitcoin received by a wallet.

    Parameters:
    wallet_id (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin received by a wallet.
    """
    response = requests.get(
        f"https://blockchain.info/q/getreceivedbyaddress/{wallet_id}")
    # Convert from sats to btc divide by 100,000,000
    return int(response.json()) / 100000000


def get_curent_balance(btc_address) -> float:
    """
    Returns the amount of bitcoin currently in a given wallet.

    Parameters:
    btc_address (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin in given wallet.
    """
    response = requests.get(
        f"https://blockchain.info/q/addressbalance/{btc_address}")
    # Convert from sats to btc (/100000000)
    return int(response.json()) / 100000000


def get_first_seen(btc_address) -> float:
    """
    Returns the timestamp of the block an address was first confirmed in.

    Parameters:
    btc_address (str): The bitcoin wallet.

    Returns:
    (float): Amount of bitcoin in given wallet.
    """
    response = requests.get(
        f"https://blockchain.info/q/addressfirstseen/{btc_address}")
    return datetime.fromtimestamp(response.json())


if __name__ == "__main__":
    print(get_total_sent("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_total_received("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_curent_balance("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_first_seen("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
