


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

# weth_supply = w3.fromWei(weth.functions.totalSupply().call(), "ether")
# weth_balance = w3.fromWei(w3.eth.getBalance(account=weth_address), "ether")
# print(f'WETH supply: {weth_supply}')
# print(f'ETH in WETH contract: {weth_balance}')

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
