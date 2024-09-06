import pytest
from unittest.mock import AsyncMock, MagicMock
from app.usecases.redirect_short_url_usecase import RedirectShortUrlUseCase

@pytest.mark.asyncio
async def test_repository_returns_correct_url_on_valid_short_url(mock_repository):
    """ 測試當存儲庫返回有效短網址時，返回正確的原始 URL """
    mock_repository.get_by_short_url = AsyncMock(return_value=MagicMock(original_url="https://example.com"))
    mock_repository.is_expired = AsyncMock(return_value=False)

    usecase = RedirectShortUrlUseCase()
    result = await usecase.execute("short123")

    assert result == "https://example.com"

@pytest.mark.asyncio
async def test_repository_returns_none_on_nonexistent_short_url(mock_repository):
    """ 測試當短網址不存在時，返回 None """
    mock_repository.get_by_short_url = AsyncMock(return_value=None)

    usecase = RedirectShortUrlUseCase()
    result = await usecase.execute("nonexistent123")

    assert result is None

@pytest.mark.asyncio
async def test_repository_returns_none_on_expired_short_url(mock_repository):
    """ 測試當短網址過期時，返回 None """
    mock_repository.get_by_short_url = AsyncMock(return_value=MagicMock(original_url="https://example.com"))
    mock_repository.is_expired = AsyncMock(return_value=True)

    usecase = RedirectShortUrlUseCase()
    result = await usecase.execute("short123")

    assert result is None

@pytest.mark.asyncio
async def test_repository_called_with_correct_params(mock_repository):
    """ 測試存儲庫是否使用正確的參數進行調用 """
    mock_repository.get_by_short_url = AsyncMock(return_value=MagicMock(original_url="https://example.com"))
    mock_repository.is_expired = AsyncMock(return_value=False)

    usecase = RedirectShortUrlUseCase()
    await usecase.execute("short123")

    mock_repository.get_by_short_url.assert_called_once_with("short123")
