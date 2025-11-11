from bitcoinlib.keys import HDKey
from bitcoinlib.services.services import Service
from mongo_utils import save_to_mongo
from telegram_bot import send_alert
from storage.storage_manager import storage_manager
from config import config

# Configure service for testnet or mainnet based on settings
if config.USE_TESTNET and not config.ENABLE_MAINNET:
    svc = Service(network='testnet')
    print("🧪 Scanner configured for TESTNET mode (safe for research)")
elif config.ENABLE_MAINNET:
    svc = Service(network='bitcoin')
    print("⚠️  WARNING: Scanner configured for MAINNET mode - USE WITH EXTREME CAUTION")
else:
    svc = Service(network='testnet')
    print("🔒 Scanner DISABLED - Enable USE_TESTNET or ENABLE_MAINNET in config")

def generate_key():
    """Generate a Bitcoin key - network determined by config"""
    network = 'testnet' if config.USE_TESTNET else 'bitcoin'
    key = HDKey(network=network)
    return key.wif(), key.address()

def check_balance(address):
    try:
        info = svc.getbalance(address)
        return info['balance'] if info and 'balance' in info else 0
    except Exception:
        return 0

def scan_keys(batch_size=50):
    results = []
    for _ in range(batch_size):
        priv, addr = generate_key()
        balance = check_balance(addr)
        if balance > 0:
            save_to_mongo(addr, priv, balance)
            send_alert(addr, priv, balance)
            results.append({
                "address": addr,
                "private_key": priv,
                "balance": balance
            })
    
    # Export results to CSV if any wallets found
    if results:
        csv_path = storage_manager.persist_results(results)
        if csv_path:
            print(f"📊 Results exported to: {csv_path}")
    
    return results
