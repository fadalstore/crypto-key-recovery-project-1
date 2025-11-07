from mnemonic import Mnemonic

def generate_seed_phrase():
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128)
