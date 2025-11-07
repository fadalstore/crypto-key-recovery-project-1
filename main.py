from fastapi import FastAPI
from scanner import scan_keys
from seed_generator import generate_seed_phrase

app = FastAPI()

@app.get("/scan")
def scan(batch: int = 100):
    return scan_keys(batch)

@app.get("/seed")
def seed():
    return {"phrase": generate_seed_phrase()}
