# We expect $50 in ETH:
# 0.016884533429688
# or in wei:
# 1 eth = 10**18 wei = 10**9 gwei
# 1 eth : 10**18 = 0.016 : x -> x = 0.016 * 10^18 = 
# 0.016 * 10**18 = 16 * 10^15 = 16000000000000000

from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entrance_fee():
  account = accounts[0]
  lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"],
                           {"from": account}
  )
  # assert lottery.getEntranceFee() > Web3.toWei(0.016, "ether")
  # assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")
                                   