from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
import os
# client = Client("https://api.mainnet-beta.solana.com")
# public_key = PublicKey("CeAL1zfpz8J8w3dcVyoucqxPzcV3kLApR4GhbuFfiazU")
# balance = client.get_balance(public_key)

# print(balance)



# sender = Keypair().from_private_key("qFTETAX1sdEzPoeSk7jFEZCUoiQAsX9xW2smLhbmnmFy3R2xJ2pe1vJTFwQAw3TFzKeiLLF9YgwuWDT93D1yWBS")
# receiver = PublicKey("GNka1ZcJCWHWPEojwuQvn4wGM79xmdy7ZsyitiYZkX9T")
# amount = 20000 # This is the amount in lamports

# instruction = transfer(
#     from_public_key=sender.public_key,
#     to_public_key=receiver, 
#     lamports=amount
# )
# transaction = Transaction(instructions=[instruction], signers=[sender])

# result = client.send_transaction(transaction)

# print(result)

async def do_transfer():
    client = Client(os.environ['SOLANA_CHAIN_URL'])
    public_key = PublicKey(os.environ['WALLET_SWEEP'])
    balance = client.get_balance(public_key)
    print(balance)

    fee=client.get_fees()
    lamport_fee=fee['value']['feeCalculator']['lamportsPerSignature']
    receiver = PublicKey(os.environ['WALLET_DEST'])
    sender = Keypair().from_private_key(os.environ['WALLET_SWEEP_KEY'])
    amount = balance -lamport_fee # This is the amount in lamports
    
    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=amount
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])

    result = client.send_transaction(transaction)

    print(result)
