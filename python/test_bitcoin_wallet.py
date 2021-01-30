import pytest
import datetime
from . import bitcoin_wallet


TEST_WALLET_ID = "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"


def test_get_total_sent_returns_float():
    """
    Test that the get_total_sent function returns a float
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    total_sent = wallet.total_sent

    assert type(total_sent) == float


def test_get_total_received_returns_float():
    """
    Test that the get_total_received function returns a float
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    total_received = wallet.total_received

    assert type(total_received) == float


def test_get_current_balance_returns_float():
    """
    Test that the get_current_balance function returns a float
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    current_balance = wallet.balance

    assert type(current_balance) == float


def test_get_first_seen_returns_datetime():
    """
    Test that the get_first_seen function returns a datetime
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    first_seen = wallet.first_seen

    assert type(first_seen) == datetime.datetime
