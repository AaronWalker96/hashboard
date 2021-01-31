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
        response = requests.get(
            f"https://blockchain.info/q/addressfirstseen/{self.address}")
        try:
            first_seen = datetime.fromtimestamp(response.json())
            return True
        except:
            return False

    def get_total_sent(self) -> float:
        """
        Returns the total amount of bitcoin sent by a wallet.

        Parameters:
        wallet_id (str): The bitcoin wallet to get total sent from.

        Returns:
        (float): Amount of bitcoin sent from a wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/getsentbyaddress/{self.address}")
        # Convert from sats to btc divide by 100,000,000
        return int(response.json()) / 100000000

    def get_total_received(self) -> float:
        """
        Returns the total amount of bitcoin received by a wallet.

        Parameters:
        wallet_id (str): The bitcoin wallet to get total received from.

        Returns:
        (float): Amount of bitcoin received by a wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/getreceivedbyaddress/{self.address}")
        # Convert from sats to btc divide by 100,000,000
        return int(response.json()) / 100000000

    def get_curent_balance(self) -> float:
        """
        Returns the amount of bitcoin currently in a given wallet.

        Parameters:
        btc_address (str): The bitcoin wallet to get amount from.

        Returns:
        (float): Amount of bitcoin in given wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/addressbalance/{self.address}")
        # Convert from sats to btc (/100000000)
        print(response.json())
        return int(response.json()) / 100000000

    def get_first_seen(self) -> datetime:
        """
        Returns the timestamp of the block an address was first confirmed in.

        Parameters:
        btc_address (str): The bitcoin wallet.

        Returns:
        (datetime): The date the block an address was first confirmed in.
        """
        response = requests.get(
            f"https://blockchain.info/q/addressfirstseen/{self.address}")
        return datetime.fromtimestamp(response.json())
