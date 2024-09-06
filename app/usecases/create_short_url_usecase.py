from datetime import datetime, timedelta
from app.domain.entities import ShortUrl
from app.infrastructure.repositories.short_url_repository_impl import ShortUrlRepositoryImpl
import hashlib

class CreateShortUrlUseCase:
    def __init__(self):
        self.repository = ShortUrlRepositoryImpl()

    async def execute(self, original_url: str):
        short_url = hashlib.md5(original_url.encode()).hexdigest()[:8]
        expiration_date = datetime.now() + timedelta(days=30)
        short_url_entity = ShortUrl(original_url, short_url, expiration_date)

        success = await self.repository.save(short_url_entity)
        return short_url_entity if success else None
