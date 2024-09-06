from app.domain.entities import ShortUrl
from datetime import datetime

class ShortUrlRepositoryImpl:
    def __init__(self):
        self.storage = {}

    async def save(self, short_url: ShortUrl) -> bool:
        self.storage[short_url.short_url] = short_url
        return True

    async def get_by_short_url(self, short_url: str) -> ShortUrl:
        return self.storage.get(short_url)

    async def is_expired(self, short_url: ShortUrl) -> bool:
        return short_url.expiration_date < datetime.now()
