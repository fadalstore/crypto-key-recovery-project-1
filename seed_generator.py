from mnemonic import Mnemonic

def generate_seed(language="english"):
    mnemo = Mnemonic(language)
    words = mnemo.generate(strength=128)
    return words

def generate_seed_phrase():
    return generate_seed()
