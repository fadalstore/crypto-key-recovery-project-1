"""
Dashboard for viewing found wallets
"""

import secrets
from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from typing import List, Dict, Any
from config import config
from storage.storage_manager import storage_manager
from mongo_utils import USE_TEST_MODE


router = APIRouter()
security = HTTPBasic()
templates = Jinja2Templates(directory="templates")


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify dashboard authentication"""
    correct_username = secrets.compare_digest(
        credentials.username, config.DASHBOARD_USERNAME
    )
    correct_password = secrets.compare_digest(
        credentials.password, config.DASHBOARD_PASSWORD
    )
    
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    username: str = Depends(verify_credentials),
    page: int = 1,
    search: str = ""
):
    """
    Dashboard page for viewing found wallets
    Protected with HTTP Basic Authentication
    """
    # Get all results (from CSV in test mode, could extend to MongoDB)
    all_results = storage_manager.get_all_results()
    
    # Filter by search term if provided
    if search:
        all_results = [
            r for r in all_results 
            if search.lower() in r.get('address', '').lower()
        ]
    
    # Pagination
    per_page = 20
    total = len(all_results)
    total_pages = (total + per_page - 1) // per_page if total > 0 else 1
    page = max(1, min(page, total_pages))
    
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    results = all_results[start_idx:end_idx]
    
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "results": results,
            "total": total,
            "page": page,
            "total_pages": total_pages,
            "search": search,
            "username": username,
            "test_mode": USE_TEST_MODE
        }
    )


@router.get("/api/wallets")
async def get_wallets(
    username: str = Depends(verify_credentials),
    limit: int = 100
):
    """
    API endpoint to get found wallets as JSON
    Protected with HTTP Basic Authentication
    """
    results = storage_manager.get_all_results()
    return {
        "total": len(results),
        "wallets": results[:limit]
    }
