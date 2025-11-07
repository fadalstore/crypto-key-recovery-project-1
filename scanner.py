from bitcoinlib.keys import HDKey
from bitcoinlib.services.services import Service
from mongo_utils import save_to_mongo
from telegram_bot import send_alert

svc = Service()

def generate_key():
    key = HDKey()
    return key.wif(), key.address()

def check_balance(address):
    info = svc.getbalance(address)
    return info['balance'] if info else 0

def scan_keys(batch_size=100):
    results = []
    for _ in range(batch_size):
        priv, addr = generate_key()
        balance = check_balance(addr)
        if balance > 0:
            save_to_mongo(addr, priv, balance)
            send_alert(addr, priv, balance)
            results.append({'address': addr, 'private': priv, 'balance': balance})
    return results
