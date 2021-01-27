import requests
import json
from datetime import datetime
from statistics import mean
from datetime import datetime


class Wallet:
    def __init__(self, address):
        self.address = address
        self.balance = get_curent_balance(address)
        self.total_sent = get_total_sent(address)
        self.total_received = get_total_received(address)
        self.first_seen = get_first_seen(address)
        


def get_total_sent(wallet_id) -> float:
    """
    Returns the total amount of bitcoin sent by a wallet.

    Parameters:
    wallet_id (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin sent from a wallet.
    """
    return 0.30734464


def get_total_received(wallet_id) -> float:
    """
    Returns the total amount of bitcoin received by a wallet.

    Parameters:
    wallet_id (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin received by a wallet.
    """
    return 0.30734464


def get_curent_balance(btc_address) -> float:
    """
    Returns the amount of bitcoin currently in a given wallet.

    Parameters:
    btc_address (str): The bitcoin wallet to get amount from.

    Returns:
    (float): Amount of bitcoin in given wallet.
    """
    return 0


def get_first_seen(btc_address) -> float:
    """
    Returns the timestamp of the block an address was first confirmed in.

    Parameters:
    btc_address (str): The bitcoin wallet.

    Returns:
    (float): Amount of bitcoin in given wallet.
    """
    return datetime.fromtimestamp(1351370614)


if __name__ == "__main__":
    print(get_total_sent("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_total_received("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_curent_balance("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
    print(get_first_seen("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"))
