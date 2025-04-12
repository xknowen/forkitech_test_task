from pydantic import BaseModel


class WalletRequest(BaseModel):
    address: str


class WalletInfo(BaseModel):
    address: str
    balance_trx: float
    bandwidth: int
    energy: int
