from tronpy import Tron
from tronpy.keys import is_address

from app.schemas import WalletInfo


async def get_wallet_info(address: str) -> WalletInfo:
    if not is_address(address):
        raise ValueError("Invalid Tron address")

    client = Tron()
    acc_info = client.get_account(address)
    resources = client.get_account_resource(address)

    return WalletInfo(
        address=address,
        balance_trx=acc_info['balance'] / 1_000_000,
        bandwidth=resources['free_net_limit'],
        energy=resources['EnergyLimit']
    )
