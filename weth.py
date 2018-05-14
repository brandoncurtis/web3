"""hacking around with the web3.py module."""

import time
import datetime
import json
import web3
import requests
from collections import Counter
from collections import defaultdict
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://35.224.54.186:9200'])

w3 = web3.Web3(web3.Web3.HTTPProvider("http://localhost:8545",
                            request_kwargs={'timeout': 60}))
#print(len(w3.middleware_stack))
#w3.middleware_stack.clear()
#print(len(w3.middleware_stack))
#w3.middleware_stack.add(web3.middleware.pythonic_middleware)
#w3.middleware_stack.add(web3.middleware.attrdict_middleware)
#print(len(w3.middleware_stack))

currentBlock = w3.eth.blockNumber
print("current blocknumber:", currentBlock)

zeroex_address = '0x12459C951127e0c374FF9105DdA097662A027093'
weth_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'

weth_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'

zeroex_abi = '[{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"isRoundingError","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"filled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"cancelled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"fillOrdersUpTo","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"cancelTakerTokenAmount","type":"uint256"}],"name":"cancelOrder","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ZRX_TOKEN_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrKillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrKillOrder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderHash","type":"bytes32"}],"name":"getUnavailableTakerTokenAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"signer","type":"address"},{"name":"hash","type":"bytes32"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"isValidSignature","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"getPartialAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKEN_TRANSFER_PROXY_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"cancelTakerTokenAmounts","type":"uint256[]"}],"name":"batchCancelOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrder","outputs":[{"name":"filledTakerTokenAmount","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"}],"name":"getOrderHash","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"EXTERNAL_QUERY_GAS_LIMIT","outputs":[{"name":"","type":"uint16"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"VERSION","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"inputs":[{"name":"_zrxToken","type":"address"},{"name":"_tokenTransferProxy","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"taker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"filledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"filledTakerTokenAmount","type":"uint256"},{"indexed":false,"name":"paidMakerFee","type":"uint256"},{"indexed":false,"name":"paidTakerFee","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogFill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"cancelledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"cancelledTakerTokenAmount","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogCancel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"errorId","type":"uint8"},{"indexed":true,"name":"orderHash","type":"bytes32"}],"name":"LogError","type":"event"}]'

def get_block_timestamp(blocknum):
    ts = w3.eth.getBlock(blocknum)['timestamp']
    ts8601 = datetime.datetime.utcfromtimestamp(ts).isoformat()
    #print(f'timestamp for block {blocknum}: {ts8601}')
    return ts8601

def get_block_timestamp_etherscan(blocknum):
    api_url = f'{api_url_base}?module=block&action=getblockreward&blockno={blocknum}'
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        ts = int(json.loads(response.content.decode('utf-8'))['result']['timeStamp'])
        ts8601 = datetime.datetime.utcfromtimestamp(ts).isoformat()
        print(f'timestamp for block {blocknum}: {ts8601}')
        return ts8601
    else:
        return None

def write_elastic(body,index,doctype,id):
    # write this junk to elasticsearch
    try:
        res = es.index(index="orderfills", doc_type="zeroex_v1", id=f'{block_number}_{tx_index}_{log_index}', body=body)
        print(res)
    except Exception as e:
        print(e.info)
        print(zeroex_events[i])

def get_events(contract,event,startblock,endblock,topics=None):
    event_filter = contract.eventFilter(
                event, {'fromBlock': startblock, #4350000, #5300000, 4350000
                        'toBlock': endblock, #currentBlock,
                        'topics': topics})
                        # broken between 5,200,000 and 5,300,000
    #            'LogError', {'fromBlock': 5296872, 'toBlock': 5302153})
    #            'LogError', {'fromBlock': 5260500, 'toBlock': 5302153})
    events = event_filter.get_all_entries()
    print(f'{event} total events between blocks {startblock} and {endblock}: {len(events)}')
    return events

def parse_zeroex_events(events, write_elastic=False, write_file=None):
    parse_block = 0
    parse_time = 0
    for i,event in enumerate(events):
        # convert AttributeDicts to regular dicts
        events[i] = dict(event)
        events[i]['args'] = dict(event['args'])
        events[i]['transactionHash'] = w3.toHex(event['transactionHash'])
        events[i]['blockHash'] = w3.toHex(event['blockHash'])
        events[i]['args']['tokens'] = w3.toHex(event['args']['tokens'])
        events[i]['args']['orderHash'] = w3.toHex(event['args']['orderHash'])
        events[i]['args']['filledMakerTokenAmount'] = float(w3.fromWei(event['args']['filledMakerTokenAmount'], 'ether'))
        events[i]['args']['filledTakerTokenAmount'] = float(w3.fromWei(event['args']['filledTakerTokenAmount'], 'ether'))
        events[i]['args']['paidTakerFee'] = float(w3.fromWei(event['args']['paidTakerFee'], 'ether'))
        events[i]['args']['paidMakerFee'] = float(w3.fromWei(event['args']['paidMakerFee'], 'ether'))

        # add some good info from the transaction
        event_txhash = event['transactionHash']
        tx = w3.eth.getTransaction(event_txhash)
        events[i]['tx_sender'] = tx['from']
        events[i]['tx_receiver'] = tx['to']
        events[i]['tx_gas'] = float(w3.fromWei(tx['gasPrice'], 'gwei'))
        events[i]['tx_nonce'] = tx['nonce']

        #get the time that this block was mined
        tx_index = event['transactionIndex']
        log_index = event['logIndex']
        block_number = event['blockNumber']
        if block_number != parse_block:
            parse_time = get_block_timestamp(block_number)
            parse_block = block_number
        events[i]['timestamp'] = parse_time

        # information we can glean from the input data
        inputdata = tx['input']
        events[i]['tx_fxnsig'] = inputdata[:10]
        num_inputs = int(len(inputdata)/64)

        # information that we MAY glean from the input data if it's a standard 0x TX
        if tx['to'] == zeroex_address:
            num_orders = max(1,int((num_inputs - 12) / 14))
            events[i]['numOrders'] = num_orders
            #events[i]['expiration'] = <multiplevalues>
            inputs = [inputdata[10+64*j:10+64*(j+1)] for j in range(num_inputs)]

            if num_orders > 1 or num_inputs > 16:
                #events[i]['fillTakertokenAmount'] = w3.toInt(hexstr=f'0x{inputs[2]}')
                events[i]['fillTakertokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[2]}')),'ether'))
            else:
                events[i]['fillTakertokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[11]}')),'ether'))

        if write_elastic:
            # write this junk to elasticsearch
            write_elastic(body = events[i],
                          index = 'orderfills',
                          doc_type = 'zeroex_v1',
                          id=f'{block_number}_{tx_index}_{log_index}')
        if write_file:
            # write this junk to file
            with open(write_file, 'w') as outfile:
               json.dump(events, outfile)

if __name__ == '__main__':
    weth = w3.eth.contract(abi=weth_abi, address=weth_address)
    zeroex = w3.eth.contract(abi=zeroex_abi, address=zeroex_address)
    eventname = 'Transfer'
    weth_events = get_events(weth,eventname,5200000,5300000)
    for event in weth_events:
        print(event['blockNumber'])
        print(w3.toHex(event['transactionHash']))
    # get the good stuff; optionally upload to elastic
    #parse_zeroex_events(zeroex_events, write_elastic=False)
