from abc import ABC, abstractmethod
from app.domain.entities import ShortUrl

class ShortUrlRepository(ABC):
    @abstractmethod
    async def save(self, short_url: ShortUrl) -> bool:
        pass

    @abstractmethod
    async def get_by_short_url(self, short_url: str) -> ShortUrl:
        pass

    @abstractmethod
    async def is_expired(self, short_url: ShortUrl) -> bool:
        pass
