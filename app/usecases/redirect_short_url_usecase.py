from app.infrastructure.repositories.short_url_repository_impl import ShortUrlRepositoryImpl


class RedirectShortUrlUseCase:
    def __init__(self):
        self.repository = ShortUrlRepositoryImpl()

    async def execute(self, short_url: str):
        short_url_entity = await self.repository.get_by_short_url(short_url)

        if short_url_entity and not await self.repository.is_expired(short_url_entity):
            return short_url_entity.original_url
        return None
