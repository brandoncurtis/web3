"""hacking around with the web3.py module."""

import time
import datetime
import json
import web3
import requests
from collections import Counter
from collections import defaultdict

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

def get_fxncalls(fxnsig,startblock,endblock):
    fxn_calls = defaultdict(list)
    for block in range(startblock, endblock):
        txs = w3.eth.getBlock(block).transactions
        for txhash in txs:
            tx = w3.eth.getTransaction(txhash)
            if (tx.input[:10] == fxnsig):
                fxn_calls[tx.to].append(web3.utils.encoding.to_hex(txhash))
    return fxn_calls

if __name__ == '__main__':
    fxn_calls = get_fxncalls('0x83f12fec',5200000,5300000) # 4350000 ZeroEx begins
    # geth   5430000,5440000
    # parity 5440000,5450000
    # geth   5450000,5460000
    # write this junk to a file
    with open('fxn_calls_5200000-5300000.csv', 'w') as outfile:
       json.dump(fxn_calls, outfile)
       #print(fxn_calls)
