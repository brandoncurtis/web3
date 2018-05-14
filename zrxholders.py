"""hacking around with the web3.py module."""

import time
import datetime
import json
import web3
import requests
from collections import Counter
from collections import defaultdict

w3 = web3.Web3(web3.Web3.HTTPProvider("http://127.0.0.1:8545",
                            request_kwargs={'timeout': 60}))
currentBlock = w3.eth.blockNumber
print("current blocknumber:", currentBlock)

zrx_address = '0xe41d2489571d322189246dafa5ebde1f4699f498'
weth_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
zeroex_address = '0x12459C951127e0c374FF9105DdA097662A027093'

zrx_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'

weth_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'

zeroex_abi = '[{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"isRoundingError","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"filled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"cancelled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"fillOrdersUpTo","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"cancelTakerTokenAmount","type":"uint256"}],"name":"cancelOrder","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ZRX_TOKEN_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrKillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrKillOrder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderHash","type":"bytes32"}],"name":"getUnavailableTakerTokenAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"signer","type":"address"},{"name":"hash","type":"bytes32"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"isValidSignature","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"getPartialAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKEN_TRANSFER_PROXY_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"cancelTakerTokenAmounts","type":"uint256[]"}],"name":"batchCancelOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrder","outputs":[{"name":"filledTakerTokenAmount","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"}],"name":"getOrderHash","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"EXTERNAL_QUERY_GAS_LIMIT","outputs":[{"name":"","type":"uint16"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"VERSION","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"inputs":[{"name":"_zrxToken","type":"address"},{"name":"_tokenTransferProxy","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"taker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"filledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"filledTakerTokenAmount","type":"uint256"},{"indexed":false,"name":"paidMakerFee","type":"uint256"},{"indexed":false,"name":"paidTakerFee","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogFill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"cancelledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"cancelledTakerTokenAmount","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogCancel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"errorId","type":"uint8"},{"indexed":true,"name":"orderHash","type":"bytes32"}],"name":"LogError","type":"event"}]'

weth = w3.eth.contract(abi=weth_abi, address=weth_address)
# weth_supply = w3.fromWei(weth.functions.totalSupply().call(), "ether")
# weth_balance = w3.fromWei(w3.eth.getBalance(account=weth_address), "ether")
# print(f'WETH supply: {weth_supply}')
# print(f'ETH in WETH contract: {weth_balance}')

zeroex = w3.eth.contract(abi=zeroex_abi, address=zeroex_address)
zeroex_filter = zeroex.eventFilter(
            'LogFill', {'fromBlock': 4350000, #5300000, 4350000
                        'toBlock': currentBlock,
                        'topics': None})
#            'LogError', {'fromBlock': 5296872, 'toBlock': 5302153})
#            'LogError', {'fromBlock': 5260500, 'toBlock': 5302153})
zeroex_events = zeroex_filter.get_all_entries()
print(f'ZeroEx total events: {len(zeroex_events)}')

# weth_users = defaultdict(dict)
# zeroex_errors = []
#zeroex_feeRecipients = []
#zeroex_takers = []
#zeroex_makers = []


#for event in zeroex_events:
    # event_errorId = event['args']['errorId']
    #event_hash = event['transactionHash']
    #event_block = event['blockNumber']
    #event_feeRecipient = event['args']['feeRecipient']
    #event_maker = event['args']['maker']
    #event_taker = event['args']['taker']
    # event_tx = w3.eth.getTransaction(event_hash)
    # event_sender = event_tx['from']
    # event_to = event_tx['to']
    # event_gas = w3.fromWei(event_tx['gasPrice'], 'gwei')
    # event_nonce = event_tx['nonce']
    # event_data = event_tx['input']
    # zeroex_errors.append(event_errorId)
    #zeroex_feeRecipients.append(event_feeRecipient)
    #zeroex_takers.append(event_taker)
    #zeroex_makers.append(event_maker)

# zeroex_error_counter = Counter(zeroex_errors)
# print(zeroex_error_counter)

#zeroex_feeRecipient_counter = Counter(zeroex_feeRecipients)
#print(f'most common feeReceipients: {zeroex_feeRecipient_counter.most_common()[:5]}')
#zeroex_taker_counter = Counter(zeroex_takers)
#print(f'most common takers: {zeroex_taker_counter.most_common()[:5]}')
#zeroex_maker_counter = Counter(zeroex_makers)
#print(f'most common makers: {zeroex_maker_counter.most_common()[:5]}')

# api_token = 'YRHF6BS1JBSQ6D8KAG2QJVWRSWD61KNNG8'
# api_url_base = 'https://api.etherscan.io/api/'
# headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer {0}'.format(api_token)}

def get_block_timestamp(blocknum):
    ts = w3.eth.getBlock(blocknum)['timestamp']
    ts8601 = datetime.datetime.utcfromtimestamp(ts).isoformat()
    #print(f'timestamp for block {blocknum}: {ts8601}')
    return ts8601
    # api_url = f'{api_url_base}?module=block&action=getblockreward&blockno={blocknum}'
    # response = requests.get(api_url, headers=headers)
    # if response.status_code == 200:
    #     ts = int(json.loads(response.content.decode('utf-8'))['result']['timeStamp'])
    #     ts8601 = datetime.datetime.utcfromtimestamp(ts).isoformat()
    #     print(f'timestamp for block {blocknum}: {ts8601}')
    #     return ts8601
    # else:
    #     return None

parse_block = 0
parse_time = 0
for i,event in enumerate(zeroex_events):
    #time.sleep(0.5)
    zeroex_events[i] = dict(event)
    zeroex_events[i]['args'] = dict(event['args'])
    zeroex_events[i]['transactionHash'] = w3.toHex(event['transactionHash'])
    zeroex_events[i]['blockHash'] = w3.toHex(event['blockHash'])
    zeroex_events[i]['args']['tokens'] = w3.toHex(event['args']['tokens'])
    zeroex_events[i]['args']['orderHash'] = w3.toHex(event['args']['orderHash'])
    zeroex_events[i]['args']['filledMakerTokenAmount'] = float(w3.fromWei(event['args']['filledMakerTokenAmount'], 'ether'))
    zeroex_events[i]['args']['filledTakerTokenAmount'] = float(w3.fromWei(event['args']['filledTakerTokenAmount'], 'ether'))
    zeroex_events[i]['args']['paidTakerFee'] = float(w3.fromWei(event['args']['paidTakerFee'], 'ether'))
    zeroex_events[i]['args']['paidMakerFee'] = float(w3.fromWei(event['args']['paidMakerFee'], 'ether'))

    # add some good info from the transaction
    event_txhash = event['transactionHash']
    tx = w3.eth.getTransaction(event_txhash)
    zeroex_events[i]['tx_sender'] = tx['from']
    zeroex_events[i]['tx_receiver'] = tx['to']
    zeroex_events[i]['tx_gas'] = float(w3.fromWei(tx['gasPrice'], 'gwei'))
    zeroex_events[i]['tx_nonce'] = tx['nonce']

    #get the time that this block was mined
    tx_index = event['transactionIndex']
    log_index = event['logIndex']
    block_number = event['blockNumber']
    if block_number != parse_block:
        parse_time = get_block_timestamp(block_number)
        parse_block = block_number
    zeroex_events[i]['timestamp'] = parse_time

    # information we can glean from the input data
    inputdata = tx['input']
    zeroex_events[i]['tx_fxnsig'] = inputdata[:10]
    num_inputs = int(len(inputdata)/64)

    # information that we MAY glean from the input data if it's a standard 0x TX
    if tx['to'] == zeroex_address:
        num_orders = max(1,int((num_inputs - 12) / 14))
        zeroex_events[i]['numOrders'] = num_orders
        #zeroex_events[i]['expiration'] = <multiplevalues>
        inputs = [inputdata[10+64*j:10+64*(j+1)] for j in range(num_inputs)]

        if num_orders > 1 or num_inputs > 16:
            #zeroex_events[i]['fillTakertokenAmount'] = w3.toInt(hexstr=f'0x{inputs[2]}')
            zeroex_events[i]['fillTakertokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[2]}')),'ether'))
        else:
            zeroex_events[i]['fillTakertokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[11]}')),'ether'))

    # write this junk to elasticsearch
    try:
        res = es.index(index="orderfills", doc_type="zeroex_v1", id=f'{block_number}_{tx_index}_{log_index}', body=zeroex_events[i])
        print(res)
    except Exception as e:
        print(e.info)
        print(zeroex_events[i])

#print(zeroex_events[:2])
#print(f'JSON serialization of an event:\n{json.dumps(zeroex_events[:1])}')
#print(f'And here is the original: {zeroex_events[:1]}')
#with open('data.json', 'w') as outfile:
#    json.dump(zeroex_events, outfile)

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
