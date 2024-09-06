from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from app.usecases.create_short_url_usecase import CreateShortUrlUseCase
from app.usecases.redirect_short_url_usecase import RedirectShortUrlUseCase
from fastapi.responses import RedirectResponse

router = APIRouter()

class CreateShortUrlRequest(BaseModel):
    original_url: HttpUrl

class CreateShortUrlResponse(BaseModel):
    short_url: str
    expiration_date: datetime
    success: bool
    reason: str = None

@router.post("/shorten", response_model=CreateShortUrlResponse)
async def create_short_url(request: CreateShortUrlRequest):
    try:
        usecase = CreateShortUrlUseCase()
        result = await usecase.execute(request.original_url)
        if result.success:
            return CreateShortUrlResponse(
                short_url=result.short_url,
                expiration_date=result.expiration_date,
                success=True
            )
        else:
            return CreateShortUrlResponse(
                short_url="",
                expiration_date=None,
                success=False,
                reason=result.reason
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

# app/api/routes/short_url.py
@router.get("/{short_url}", status_code=307)
async def redirect_short_url(short_url: str):
    try:
        usecase = RedirectShortUrlUseCase()
        original_url = await usecase.execute(short_url)
        if original_url:
            return RedirectResponse(url=original_url)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Short URL not found or expired"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
