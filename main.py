from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from scanner import scan_keys
from seed_generator import generate_seed_phrase
from dashboard import router as dashboard_router
from scheduler import start_scheduler, stop_scheduler, get_scheduler_status
from config import config

limiter = Limiter(key_func=get_remote_address)
security = HTTPBearer(auto_error=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    print("🚀 Starting Bitcoin Scanner API...")
    start_scheduler()
    yield
    # Shutdown
    print("🛑 Shutting down...")
    stop_scheduler()


app = FastAPI(lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response

# Include dashboard router
app.include_router(dashboard_router)

@app.get("/client-seed-generator", response_class=HTMLResponse)
async def client_seed_generator(request: Request):
    """Client-side seed generator - 100% secure, no server involvement"""
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("client_seed_generator.html", {"request": request})

@app.get("/terms", response_class=HTMLResponse)
async def terms_of_service(request: Request):
    """Terms of Service and Legal Disclaimer"""
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("terms_of_service.html", {"request": request})

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
            <strong>⚠️ LEGAL DISCLAIMER</strong><br>
            This tool is for EDUCATIONAL and RESEARCH purposes ONLY on Bitcoin TESTNET. 
            <a href="/terms" style="color: #856404; text-decoration: underline;">Read full Terms of Service</a>
        </div>
        
        <div class="warning" style="background: #d1ecf1; border-left-color: #0c5460; color: #0c5460;">
            <strong>🔒 SECURITY UPDATE</strong><br>
            Seed generation is now CLIENT-SIDE ONLY. 
            <a href="/client-seed-generator" style="color: #0c5460; text-decoration: underline;">Use secure client-side generator</a>
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
            <h3>GET /dashboard</h3>
            <p>View found wallets dashboard (requires authentication)</p>
            <button onclick="window.location.href='/dashboard'">Open Dashboard</button>
        </div>
        
        <div class="endpoint">
            <h3>GET /docs</h3>
            <p>View interactive API documentation</p>
            <button onclick="window.location.href='/docs'">Open API Docs</button>
        </div>
        
        <div class="endpoint">
            <h3>GET /scheduler/status</h3>
            <p>Check automated scanning status</p>
            <button onclick="checkScheduler()">Check Status</button>
            <div id="schedulerResult"></div>
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
            
            async function checkScheduler() {
                document.getElementById('schedulerResult').innerHTML = 'Loading...';
                const response = await fetch('/scheduler/status');
                const data = await response.json();
                let status = data.running ? '✅ Running' : '⏸️ Stopped';
                let nextRun = data.jobs.length > 0 && data.jobs[0].next_run ? data.jobs[0].next_run : 'N/A';
                document.getElementById('schedulerResult').innerHTML = 
                    `<div class="result"><strong>Status:</strong> ${status}<br><strong>Interval:</strong> ${data.interval_minutes} minutes<br><strong>Next Run:</strong> ${nextRun}</div>`;
            }
        </script>
    </body>
    </html>
    """

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify API key for protected endpoints"""
    if config.REQUIRE_API_KEY:
        if not credentials or not config.API_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="API key required. Set API_KEY environment variable and provide in Authorization header"
            )
        if credentials.credentials != config.API_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API key"
            )
    return True

@app.get("/scan")
@limiter.limit("5/minute")
async def scan(request: Request, batch: int = 100, authenticated: bool = Depends(verify_api_key)):
    """
    Scan endpoint - PROTECTED
    Requires API key authentication and is rate limited
    """
    if not config.ENABLE_MAINNET and not config.USE_TESTNET:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Scanner is disabled. Enable USE_TESTNET or ENABLE_MAINNET in environment"
        )
    
    if batch > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Batch size cannot exceed 100"
        )
    
    return scan_keys(batch)

@app.get("/seed")
async def seed():
    """
    DEPRECATED: Seed generation should be done CLIENT-SIDE only
    This endpoint is kept for backwards compatibility but should not be used
    """
    return {
        "error": "Server-side seed generation is DISABLED for security",
        "message": "Generate seeds client-side using the /client-seed-generator page",
        "redirect": "/client-seed-generator"
    }

@app.get("/scheduler/status")
def scheduler_status():
    """Get current scheduler status"""
    return get_scheduler_status()

@app.get("/health")
def health_check():
    """Health check endpoint to verify all systems"""
    from mongo_utils import USE_TEST_MODE
    import os
    
    return {
        "status": "healthy",
        "server": "running",
        "mode": "test" if USE_TEST_MODE else "production",
        "features": {
            "database": "mongodb" if not USE_TEST_MODE else "local_json",
            "notifications": "telegram" if config.has_telegram else "console",
            "automated_scanning": config.ENABLE_AUTO_SCAN,
            "csv_export": True,
            "google_drive_backup": config.has_drive_backup
        },
        "configuration": {
            "scan_interval_minutes": config.SCAN_INTERVAL_MINUTES,
            "scan_batch_size": config.SCAN_BATCH_SIZE,
            "csv_retention_days": config.CSV_ROTATION_DAYS,
            "exports_directory": config.CSV_OUTPUT_DIR,
            "exports_exist": os.path.exists(config.CSV_OUTPUT_DIR)
        }
    }

@app.get("/test")
def test_scanner():
    """Test the scanner with a single key generation"""
    from scanner import generate_key, check_balance
    
    try:
        # Generate a single key
        private_key, address = generate_key()
        balance = check_balance(address)
        
        return {
            "test_result": "success",
            "message": "Scanner is working correctly",
            "test_data": {
                "address": address,
                "private_key": private_key[:10] + "..." + private_key[-10:],  # Partial key for security
                "balance_checked": True,
                "balance": balance
            }
        }
    except Exception as e:
        return {
            "test_result": "error",
            "message": str(e)
        }
