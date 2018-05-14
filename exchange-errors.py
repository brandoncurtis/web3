"""hacking around with the web3.py module."""

from web3 import Web3
from collections import Counter
from collections import defaultdict

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545",
                            request_kwargs={'timeout': 60}))
currentBlock = w3.eth.blockNumber
print("current blocknumber:", currentBlock)

zeroex_address = '0x12459C951127e0c374FF9105DdA097662A027093'
weth_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
rdr_address = '0xA258b39954ceF5cB142fd567A46cDdB31a670124'

def inputToAddr(inputstr):
    return w3.toChecksumAddress(inputstr[24:])

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

zeroex_abi = '[{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"isRoundingError","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"filled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"cancelled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"fillOrdersUpTo","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"cancelTakerTokenAmount","type":"uint256"}],"name":"cancelOrder","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ZRX_TOKEN_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrKillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrKillOrder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderHash","type":"bytes32"}],"name":"getUnavailableTakerTokenAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"signer","type":"address"},{"name":"hash","type":"bytes32"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"isValidSignature","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"getPartialAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKEN_TRANSFER_PROXY_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"cancelTakerTokenAmounts","type":"uint256[]"}],"name":"batchCancelOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrder","outputs":[{"name":"filledTakerTokenAmount","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"}],"name":"getOrderHash","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"EXTERNAL_QUERY_GAS_LIMIT","outputs":[{"name":"","type":"uint16"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"VERSION","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"inputs":[{"name":"_zrxToken","type":"address"},{"name":"_tokenTransferProxy","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"taker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"filledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"filledTakerTokenAmount","type":"uint256"},{"indexed":false,"name":"paidMakerFee","type":"uint256"},{"indexed":false,"name":"paidTakerFee","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogFill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"cancelledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"cancelledTakerTokenAmount","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogCancel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"errorId","type":"uint8"},{"indexed":true,"name":"orderHash","type":"bytes32"}],"name":"LogError","type":"event"}]'

weth = w3.eth.contract(abi=weth_abi, address=weth_address)
# weth_supply = w3.fromWei(weth.functions.totalSupply().call(), "ether")
# weth_balance = w3.fromWei(w3.eth.getBalance(account=weth_address), "ether")
# print(f'WETH supply: {weth_supply}')
# print(f'ETH in WETH contract: {weth_balance}')

zeroex = w3.eth.contract(abi=zeroex_abi, address=zeroex_address)
zeroex_filter = zeroex.eventFilter(
            'LogError', {'fromBlock': 5300000,
                         'toBlock': currentBlock,
                         'topics': None})
#            'LogError', {'fromBlock': 5296872, 'toBlock': 5302153})
#            'LogError', {'fromBlock': 5260500, 'toBlock': 5302153})
zeroex_events = zeroex_filter.get_all_entries()
print(f'ZeroEx total events: {len(zeroex_events)}')

# weth_users = defaultdict(dict)
# zeroex_errors = []
# zeroex_exchanges = []
#zeroex_fails = defaultdict(dict)
zeroex_fails = defaultdict(dict)

for event in zeroex_events:
    event_hash = event['transactionHash']
    event_block = event['blockNumber']
    # event_exchange = event['args']['feeRecipient']
    event_errorId = event['args']['errorId']

    # now get the tx so we can parse the tx input data
    event_tx = w3.eth.getTransaction(event_hash)
    event_nonce = event_tx['nonce']
    event_sender = event_tx['from']
    # event_to = event_tx['to']
    event_gas = w3.fromWei(event_tx['gasPrice'], 'gwei')
    event_data = event_tx['input']

    event_num_inputs = int(len(event_data)/64)
    event_inputs = {}

    input_fields = ['maker','taker','makerToken','takerToken',
                    'feeRecipient', 'makerTokenAmount',
                    'takerTokenAmount', 'expirationTimestampInSec']

    for i in range(0,min(event_num_inputs, len(input_fields))):
        event_inputs[input_fields[i]] = event_data[10+64*i:10+64*(i+1)]

    # basically everything is traded against WETH
    # tradedToken is the non-WETH token
    if event_inputs['makerToken'] != weth_address:
        tradedToken = event_inputs['makerToken']
    else:
        tradedToken = event_inputs['takerToken']

    # add to dict if involves Radar
    if event_inputs['feeRecipient'] != rdr_address:
        zeroex_fails[inputToAddr(tradedToken)] = {'txhash': event_hash,
                                     'error': event_errorId,
                                     'sender': event_sender,
                                     'gas': event_gas}
    # zeroex_errors.append(event_errorId)
    # zeroex_exchanges.append(event_exchange)

print('\n'.join([*zeroex_fails]))
for key in zeroex_fails:
    print(zeroex_fails[key])
# zeroex_error_counter = Counter(zeroex_errors)
# print(zeroex_error_counter)

# zeroex_exchange_counter = Counter(zeroex_exchanges)
# print(zeroex_exchange_counter.most_common())

# for event in weth_events:
#     transfer_hash = deposit['transactionHash']
#     transfer_tx = w3.eth.getTransaction(transfer_hash)
#     weth
#     print(event)
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
#
# for send in weth_sends:
#    print(f'to:{send[1]},from:{send[2]},weth:{send[3]}')
