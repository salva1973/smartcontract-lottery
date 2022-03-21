# We expect $50 in ETH:
# 0.016884533429688
# or in wei:
# 1 eth = 10**18 wei = 10**9 gwei
# 1 eth : 10**18 = 0.016 : x -> x = 0.016 * 10^18 = 
# 0.016 * 10**18 = 16 * 10^15 = 16000000000000000

from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import Lottery, accounts, config, network, exceptions
from web3 import Web3
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest

# def test_get_entrance_fee():
#   account = accounts[0]
#   lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"],
#                            {"from": account}
#   )
#   # assert lottery.getEntranceFee() > Web3.toWei(0.016, "ether")
#   # assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")

def test_get_entrance_fee():
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:    
    pytest.skip("Only for local testing")
  # Arrange
  lottery = deploy_lottery()
  # Act
  # 2,000 eth / usd
  # usdEntryFee is 50
  # 2000/1 == 50/x -> x = 0.025
  expected_entrance_fee = Web3.toWei(0.025, "ether")
  entrance_fee = lottery.getEntranceFee()
  # Assert
  assert expected_entrance_fee == entrance_fee
  
def test_cant_enter_unless_started():
  # Arrange
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:    
    pytest.skip("Only for local testing")
  lottery = deploy_lottery()
  # Act / Assert
  with pytest.raises(exceptions.VirtualMachineError):
    lottery.enter({"from": get_account(), "value": lottery.getEntranceFee()})