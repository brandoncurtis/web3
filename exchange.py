"""hacking around with the web3.py module."""

import time
import datetime
import json
import web3
import requests
from collections import Counter
from collections import defaultdict
from elasticsearch import Elasticsearch

es = Elasticsearch(['https://elasticsearch.radarrelay.com'])

w3 = web3.Web3(web3.Web3.HTTPProvider("http://localhost:8645",
                            request_kwargs={'timeout': 60}))
#print(len(w3.middleware_stack))
#w3.middleware_stack.clear()
#print(len(w3.middleware_stack))
#w3.middleware_stack.add(web3.middleware.pythonic_middleware)
#w3.middleware_stack.add(web3.middleware.attrdict_middleware)
#print(len(w3.middleware_stack))

currentBlock = w3.eth.blockNumber
print("current blocknumber:", currentBlock)

zrx_address = '0xE41d2489571d322189246DaFA5ebDe1F4699F498'
weth_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
zeroex_address = '0x12459C951127e0c374FF9105DdA097662A027093'

zrx_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'

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

def write_elastic(docbody,docindex,doctype,docid):
    # write this junk to elasticsearch
    try:
        res = es.index(index=docindex, doc_type=doctype, id=docid, body=docbody)
        print(res)
    except Exception as e:
        print(e.info)
        print(docbody)

def get_events(contract,event,startblock,endblock,topics=None):
    event_filter = contract.eventFilter(
                event, {'fromBlock': startblock, #4350000
                        'toBlock': endblock, #currentBlock,
                        'topics': topics})
                        # broken between 5,200,000 and 5,300,000
    #            'LogError', {'fromBlock': 5296872, 'toBlock': 5302153})
    #            'LogError', {'fromBlock': 5260500, 'toBlock': 5302153})
    events = event_filter.get_all_entries()
    print(f'{event} total events between blocks {startblock} and {endblock}: {len(events)}')
    return events

def get_exchange(event):
    if event['args']['feeRecipient'] == '0xA258b39954ceF5cB142fd567A46cDdB31a670124':
        return 'radarrelay'
    elif event['args']['feeRecipient'] == '0xe269E891A2Ec8585a378882fFA531141205e92E9':
        return 'ddex'
    elif event['args']['feeRecipient'] ==  '0x0000000000000000000000000000000000000000':
        if event['args']['taker'] == '0x4969358e80cdC3D74477D7447BFfA3B2e2aCbe92':
            return 'paradex'
    elif event['args']['feeRecipient'] == '0x173a2467CeCE1F752Eb8416E337D0f0b58Cad795':
        return 'ercdex'
    else:
        return 'other'

def parse_zeroex_events(events, to_elastic=False, to_file=None, to_print=False, to_zrx=False):
    parse_block = 0
    parse_time = 0
    exchange_users = defaultdict(Counter)
    user_balances = defaultdict(defaultdict)
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

        # token balances
        maker = str(events[i]['args']['maker'])
        taker = str(events[i]['args']['taker'])
        events[i]['zrx_bal_maker'] = float(w3.fromWei(zrx.functions.balanceOf(maker).call(),'ether'))
        events[i]['zrx_bal_taker'] = float(w3.fromWei(zrx.functions.balanceOf(taker).call(),'ether'))

        # information we can glean from the input data
        inputdata = tx['input']
        tx_fxnsig = inputdata[:10]
        events[i]['tx_fxnsig'] = tx_fxnsig
        num_inputs = int(len(inputdata)/64)

        # information that we MAY glean from the input data if it's a standard 0x TX
        if tx['to'] == zeroex_address:
            num_orders = max(1,int((num_inputs - 12) / 14))
            events[i]['numOrders'] = num_orders
            #events[i]['expiration'] = <multiplevalues>
            inputs = [inputdata[10+64*j:10+64*(j+1)] for j in range(num_inputs)]

            # exclude `batchFillOrKillOrders`
            if tx_fxnsig != '0x4f150787':
                #print("\nnot batchFillOrKillOrders")
                if num_orders > 1 or num_inputs > 16:
                    # sounds like this is for `fillOrdersUpTo`
                    #events[i]['fillTakertokenAmount'] = w3.toInt(hexstr=f'0x{inputs[2]}')
                    events[i]['fillTakerTokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[2]}')),'ether'))
                else:
                    # is it ALWAYS in position [11]? sounds like this is for `fillOrder`
                    events[i]['fillTakerTokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[11]}')),'ether'))
            # if tx_fxnsig == '0xbc61394a': # `fillOrder`
            #     # should really put this in a separate dataset by orderhash
            #     events[i]['makerTokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[5]}')),'ether'))
            #     events[i]['takerTokenAmount'] = float(w3.fromWei((w3.toInt(hexstr=f'0x{inputs[6]}')),'ether'))

        if to_elastic:
            # write this junk to elasticsearch
            write_elastic(docbody = events[i],
                          docindex = 'fills',
                          doctype = '0x',
                          docid=f'{block_number}_{tx_index}_{log_index}')
        if to_file:
            # write this junk to file
            with open(to_file, 'w') as outfile:
               json.dump(events, outfile)
        if to_print:
            #print(get_exchange(event))
            print(events[i])

        if to_zrx:
            exchange = get_exchange(event)
            maker = str(events[i]['args']['maker'])
            taker = str(events[i]['args']['taker'])
            exchange_users[exchange][maker] += 1
            exchange_users[exchange][taker] += 1

    if to_zrx:
        # Build dict of user balances
        for key in exchange_users.keys():
            print(f'{key}, {int(sum(exchange_users[key].values())/2)} fills, {len(exchange_users[key].values())} users\n')
            # for address in users[key].most_common(10):
            #     print(f'{address[1]}: {address[0]}')
            for address in exchange_users[key].most_common():
                user_addr = address[0]
                eth_balance = float(w3.fromWei(w3.eth.getBalance(user_addr),'ether'))
                # weth_balance = float(w3.fromWei(weth.functions.balanceOf(user_addr).call(),'ether'))
                # zrx_balance = float(w3.fromWei(zrx.functions.balanceOf(user_addr).call(),'ether'))
                user_balances[user_addr]['eth'] = eth_balance
                # user_balances[user_addr]['weth'] = eth_balance
                # user_balances[user_addr]['zrx'] = zrx_balance
        #print(user_balances)
        #print(exchange_users)
        #print("\nZRX holdings by user:")
        #s = [(k, user_balances[k]['eth'], user_balances[k]['zrx']) for k in sorted(user_balances, key=user_balances.get, reverse=True)]
        # with open('zrx-radar.csv','w') as f:
        #     for k in user_balances:
        #         if k in exchange_users['radarrelay']:
        #             acct_addr = k
        #             acct_eth = user_balances[acct_addr]['eth']
        #             acct_weth = user_balances[acct_addr]['weth']
        #             acct_zrx = user_balances[acct_addr]['zrx']
        #             acct_fills = exchange_users["radarrelay"][acct_addr]
        #             f.write(f'{acct_addr},{acct_fills},{acct_eth},{acct_weth},{acct_zrx}\n')
        # with open('zrx-paradex.csv','w') as f:
        #     for k in user_balances:
        #         if k in exchange_users['paradex']:
        #             acct_addr = k
        #             acct_eth = user_balances[acct_addr]['eth']
        #             acct_weth = user_balances[acct_addr]['weth']
        #             acct_zrx = user_balances[acct_addr]['zrx']
        #             acct_fills = exchange_users["radarrelay"][acct_addr]
        #             f.write(f'{acct_addr},{acct_fills},{acct_eth},{acct_weth},{acct_zrx}\n')
        # with open('zrx-nonradar.csv','w') as f:
        #     for k in user_balances:
        #         if k not in exchange_users['radarrelay']:
        #             acct_addr = k
        #             acct_eth = user_balances[acct_addr]['eth']
        #             acct_weth = user_balances[acct_addr]['weth']
        #             acct_zrx = user_balances[acct_addr]['zrx']
        #             acct_fills = exchange_users["ddex"][acct_addr] + exchange_users["paradex"][acct_addr] + exchange_users["ercdex"][acct_addr] + exchange_users["other"][acct_addr] + exchange_users["other"][acct_addr]
        #             f.write(f'{acct_addr},{acct_fills},{acct_eth},{acct_weth},{acct_zrx}\n')
        with open('zrx-radar.csv','w') as f:
            for k in user_balances:
                if k in exchange_users['radarrelay']:
                    acct_addr = k
                    acct_fills = exchange_users["radarrelay"][acct_addr]
                    f.write(f'{acct_addr},{acct_fills}\n')
        with open('zrx-paradex.csv','w') as f:
            for k in user_balances:
                if k in exchange_users['paradex']:
                    acct_addr = k
                    acct_fills = exchange_users["paradex"][acct_addr]
                    f.write(f'{acct_addr},{acct_fills}\n')
        with open('zrx-ddex.csv','w') as f:
            for k in user_balances:
                if k in exchange_users['ddex']:
                    acct_addr = k
                    acct_fills = exchange_users["ddex"][acct_addr]
                    f.write(f'{acct_addr},{acct_fills}\n')
        with open('zrx-none.csv','w') as f:
            for k in user_balances:
                if k in exchange_users['None']:
                    acct_addr = k
                    acct_fills = exchange_users["None"][acct_addr]
                    f.write(f'{acct_addr},{acct_fills}\n')

if __name__ == '__main__':
    weth = w3.eth.contract(abi=weth_abi, address=weth_address)
    zrx = w3.eth.contract(abi=zrx_abi, address=zrx_address)
    zeroex = w3.eth.contract(abi=zeroex_abi, address=zeroex_address)
    zeroex_events = get_events(zeroex,'LogFill',4350000,currentBlock) # 4350000 ZeroEx begins
    # get the good stuff; optionally upload to elastic
    parse_zeroex_events(zeroex_events, to_elastic=False, to_print=False, to_zrx=True)
