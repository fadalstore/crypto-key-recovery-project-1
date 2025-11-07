from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from scanner import scan_keys
from seed_generator import generate_seed_phrase

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bitcoin Scanner API</title>
        <style>
            body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; }
            .endpoint { background: #f4f4f4; padding: 15px; margin: 10px 0; border-radius: 5px; }
            button { background: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px; }
            button:hover { background: #45a049; }
            .result { background: #e7f3fe; padding: 10px; margin: 10px 0; border-left: 4px solid #2196F3; }
            .warning { background: #fff3cd; padding: 10px; margin: 10px 0; border-left: 4px solid #ffc107; }
        </style>
    </head>
    <body>
        <h1>🔍 Bitcoin Scanner API</h1>
        
        <div class="warning">
            <strong>⚠️ TEST MODE ACTIVE</strong><br>
            Using local JSON file storage and console logging instead of MongoDB and Telegram.
        </div>
        
        <h2>Available Endpoints:</h2>
        
        <div class="endpoint">
            <h3>GET /seed</h3>
            <p>Generate a new 12-word seed phrase</p>
            <button onclick="generateSeed()">Generate Seed</button>
            <div id="seedResult"></div>
        </div>
        
        <div class="endpoint">
            <h3>GET /scan?batch={number}</h3>
            <p>Scan random Bitcoin keys for balance (default batch=100)</p>
            <input type="number" id="batchSize" value="10" min="1" max="100">
            <button onclick="scanKeys()">Start Scan</button>
            <div id="scanResult"></div>
        </div>
        
        <div class="endpoint">
            <h3>GET /docs</h3>
            <p>View interactive API documentation</p>
            <button onclick="window.location.href='/docs'">Open API Docs</button>
        </div>
        
        <script>
            async function generateSeed() {
                document.getElementById('seedResult').innerHTML = 'Loading...';
                const response = await fetch('/seed');
                const data = await response.json();
                document.getElementById('seedResult').innerHTML = 
                    `<div class="result"><strong>Seed Phrase:</strong><br>${data.phrase}</div>`;
            }
            
            async function scanKeys() {
                const batch = document.getElementById('batchSize').value;
                document.getElementById('scanResult').innerHTML = 'Scanning...';
                const response = await fetch(`/scan?batch=${batch}`);
                const data = await response.json();
                document.getElementById('scanResult').innerHTML = 
                    `<div class="result"><strong>Scanned ${batch} keys</strong><br>Found: ${data.length} addresses with balance</div>`;
            }
        </script>
    </body>
    </html>
    """

@app.get("/scan")
def scan(batch: int = 100):
    return scan_keys(batch)

@app.get("/seed")
def seed():
    return {"phrase": generate_seed_phrase()}
