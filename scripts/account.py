from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    passphrase = mnemonic.from_private_key(private_key)
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    return address, private_key, passphrase