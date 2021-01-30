import requests
import json
from datetime import datetime
from statistics import mean
from datetime import datetime


class Wallet:
    def __init__(self, address):
        self.address = address

    def get_exists(self) -> bool:
        """
        Returns True if the wallet exsist.

        Parameters:
        wallet_id (str): The bitcoin wallet to check.

        Returns:
        (bool): Does the wallet exist
        """
        if self.address == "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC":
            return True
        else:
            return False

    def get_total_sent(self) -> float:
        """
        Returns the total amount of bitcoin sent by a wallet.

        Parameters:
        self (str): The bitcoin wallet to get amount from.

        Returns:
        (float): Amount of bitcoin sent from a wallet.
        """
        return 0.30734464

    def get_total_received(self) -> float:
        """
        Returns the total amount of bitcoin received by a wallet.

        Parameters:
        self (str): The bitcoin wallet to get amount from.

        Returns:
        (float): Amount of bitcoin received by a wallet.
        """
        return 0.30734464

    def get_curent_balance(self) -> float:
        """
        Returns the amount of bitcoin currently in a given wallet.

        Parameters:
        self (str): The bitcoin wallet to get amount from.

        Returns:
        (float): Amount of bitcoin in given wallet.
        """
        return 0

    def get_first_seen(self) -> float:
        """
        Returns the timestamp of the block an address was first confirmed in.

        Parameters:
        self (str): The bitcoin wallet.

        Returns:
        (float): Amount of bitcoin in given wallet.
        """
        return datetime.fromtimestamp(1351370614)
