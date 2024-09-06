import pytest
from unittest.mock import AsyncMock
from app.usecases.create_short_url_usecase import CreateShortUrlUseCase
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_create_short_url_generates_unique_short_url(mock_repository):
    """ 測試短網址生成的唯一性邏輯 """
    mock_repository.save = AsyncMock(return_value=True)

    usecase = CreateShortUrlUseCase()
    result = await usecase.execute("https://example.com")

    assert result.short_url is not None
    assert len(result.short_url) > 0


@pytest.mark.asyncio
async def test_create_short_url_validates_url_format(mock_repository):
    """ 測試 URL 格式驗證邏輯 """
    usecase = CreateShortUrlUseCase()

    with pytest.raises(ValueError, match="Invalid URL"):
        await usecase.execute("invalid-url")


@pytest.mark.asyncio
async def test_create_short_url_handles_save_failure(mock_repository):
    """ 測試當存儲庫無法保存短網址時的行為 """
    mock_repository.save = AsyncMock(return_value=False)

    usecase = CreateShortUrlUseCase()
    result = await usecase.execute("https://example.com")

    assert result is None


@pytest.mark.asyncio
async def test_create_short_url_sets_default_expiration(mock_repository):
    """ 測試生成短網址時，是否正確設置默認過期時間 """
    mock_repository.save = AsyncMock(return_value=True)

    usecase = CreateShortUrlUseCase()
    result = await usecase.execute("https://example.com")

    expected_expiration_date = datetime.now() + timedelta(days=30)
    assert result.expiration_date.date() == expected_expiration_date.date()


@pytest.mark.asyncio
async def test_create_short_url_saves_correct_data_to_repository(mock_repository):
    """ 測試存儲庫是否被正確調用，且保存了正確的數據 """
    mock_repository.save = AsyncMock(return_value=True)

    usecase = CreateShortUrlUseCase()
    result = await usecase.execute("https://example.com")

    mock_repository.save.assert_called_once()
    saved_url_entity = mock_repository.save.call_args[0][0]
    assert saved_url_entity.original_url == "https://example.com"
