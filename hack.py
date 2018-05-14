"""hacking around with the web3.py module."""

from web3 import Web3
from collections import Counter
from collections import defaultdict

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545",
                            request_kwargs={'timeout': 60}))
print("current blocknumber:", w3.eth.blockNumber)

zeroex_address = '0x12459C951127e0c374FF9105DdA097662A027093'
weth_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
weth_abi = '[{"constant":true,"inputs":[],"name":"name", \
    "outputs":[{"name":"","type":"string"}],"payable":false, \
    "stateMutability":"view","type":"function"}, \
    {"constant":false,"inputs":[{"name":"guy","type":"address"}, \
    {"name":"wad","type":"uint256"}],"name":"approve", \
    "outputs":[{"name":"","type":"bool"}],"payable":false, \
    "stateMutability":"nonpayable","type":"function"}, \
    {"constant":true,"inputs":[],"name":"totalSupply", \
    "outputs":[{"name":"","type":"uint256"}],"payable":false, \
    "stateMutability":"view","type":"function"},{"constant":false, \
    "inputs":[{"name":"src","type":"address"},{"name":"dst", \
    "type":"address"},{"name":"wad","type":"uint256"}], \
    "name":"transferFrom","outputs":[{"name":"","type":"bool"}], \
    "payable":false,"stateMutability":"nonpayable","type":"function"}, \
    {"constant":false,"inputs":[{"name":"wad","type":"uint256"}], \
    "name":"withdraw","outputs":[],"payable":false, \
    "stateMutability":"nonpayable","type":"function"}, \
    {"constant":true,"inputs":[],"name":"decimals", \
    "outputs":[{"name":"","type":"uint8"}],"payable":false, \
    "stateMutability":"view","type":"function"}, \
    {"constant":true,"inputs":[{"name":"","type":"address"}], \
    "name":"balanceOf","outputs":[{"name":"","type":"uint256"}], \
    "payable":false,"stateMutability":"view","type":"function"}, \
    {"constant":true,"inputs":[],"name":"symbol", \
    "outputs":[{"name":"","type":"string"}],"payable":false, \
    "stateMutability":"view","type":"function"}, \
    {"constant":false,"inputs":[{"name":"dst","type":"address"}, \
    {"name":"wad","type":"uint256"}],"name":"transfer", \
    "outputs":[{"name":"","type":"bool"}],"payable":false, \
    "stateMutability":"nonpayable","type":"function"}, \
    {"constant":false,"inputs":[],"name":"deposit", \
    "outputs":[],"payable":true,"stateMutability":"payable", \
    "type":"function"},{"constant":true, \
    "inputs":[{"name":"","type":"address"},{"name":"","type":"address"}], \
    "name":"allowance","outputs":[{"name":"","type":"uint256"}], \
    "payable":false,"stateMutability":"view","type":"function"}, \
    {"payable":true,"stateMutability":"payable","type":"fallback"}, \
    {"anonymous":false,"inputs":[{"indexed":true,"name":"src", \
    "type":"address"},{"indexed":true,"name":"guy","type":"address"}, \
    {"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval", \
    "type":"event"},{"anonymous":false,"inputs":[{"indexed":true, \
    "name":"src","type":"address"},{"indexed":true,"name":"dst", \
    "type":"address"},{"indexed":false,"name":"wad","type":"uint256"}], \
    "name":"Transfer","type":"event"},{"anonymous":false, \
    "inputs":[{"indexed":true,"name":"dst","type":"address"}, \
    {"indexed":false,"name":"wad","type":"uint256"}], \
    "name":"Deposit","type":"event"},{"anonymous":false, \
    "inputs":[{"indexed":true,"name":"src","type":"address"}, \
    {"indexed":false,"name":"wad","type":"uint256"}], \
    "name":"Withdrawal","type":"event"}]'

weth = w3.eth.contract(abi=weth_abi, address=weth_address)
weth_supply = w3.fromWei(weth.functions.totalSupply().call(), "ether")
weth_balance = w3.fromWei(w3.eth.getBalance(account=weth_address), "ether")

print(f'WETH supply: {weth_supply}')
print(f'ETH in WETH contract: {weth_balance}')

weth_filter = weth.eventFilter(
            'Transfer', {'fromBlock': 5296872, 'toBlock': 5297872})
#            'Transfer', {'fromBlock': 5256000, 'toBlock': 5297872})
weth_events = weth_filter.get_all_entries()
print(f'WETH total transfers: {len(weth_events)}')

weth_users = defaultdict(dict)

for event in weth_events:
    transfer_hash = event['transactionHash']
    transfer_block = event['blockNumber']
    transfer_src = event['args']['src']
    transfer_dst = event['args']['dst']
    transfer_amount = w3.fromWei(event['args']['wad'], 'ether')
    transfer_tx = w3.eth.getTransaction(transfer_hash)
    transfer_sender = transfer_tx['from']
    transfer_to = transfer_tx['to']
    transfer_gas = w3.fromWei(transfer_tx['gasPrice'], 'gwei')
    transfer_nonce = transfer_tx['nonce']





    transfer_hash = event['transactionHash']
    transfer_tx = w3.eth.getTransaction(transfer_hash)

    transfer_txto = transfer_tx['to']













for event in weth_events:
    transfer_hash = deposit['transactionHash']
    transfer_tx = w3.eth.getTransaction(transfer_hash)
    weth
    print(event)

#
#
# weth_deposits = {}
#
# weth_deposit
#
#
#
# weth_recipients = [transfer_tx['to'] for transfer_tx
#                    in map(w3.eth.getTransaction, [deposit['transactionHash']
#                                                   for deposit
#                                                   in weth_deposits])]
# weth_recipients_counter = Counter(weth_recipients)
# print(weth_recipients_counter.most_common()[:10])

# weth_sends = []
# weth_send_total = 0
# weth_zeroex = []
# weth_zeroex_total = 0
# for deposit in weth_deposits:
#     transfer_src = deposit['args']['src']
#     transfer_dst = deposit['args']['dst']
#     transfer_amount = w3.fromWei(deposit['args']['wad'], 'ether')
#     transfer_hash = deposit['transactionHash']
#     transfer_tx = w3.eth.getTransaction(transfer_hash)
#     transfer_txsender = transfer_tx['from']
#     transfer_txto = transfer_tx['to']
#   print('WETH transfer source:', transfer_src)
#   print('WETH transfer sender:', transfer_sender)
#     if transfer_src == transfer_txsender and transfer_txto == weth_address:
#         weth_sends.append([transfer_hash, transfer_txsender,
#                           transfer_dst, transfer_amount])
#         weth_send_total += 1
#     if transfer_txto == zeroex_address:
#         weth_zeroex.append([transfer_hash, transfer_txsender,
#                            transfer_dst, transfer_amount])
#         weth_zeroex_total += 1
# print(f'WETH total transfers: {len(weth_deposits)}')
# print(f'WETH zeroex: {weth_zeroex_total}')
# print(f'WETH sends: {weth_send_total}')

# for send in weth_sends:
#    print(f'to:{send[1]},from:{send[2]},weth:{send[3]}')
