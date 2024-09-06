from datetime import datetime

class ShortUrl:
    def __init__(self, original_url: str, short_url: str, expiration_date: datetime):
        self.original_url = original_url
        self.short_url = short_url
        self.expiration_date = expiration_date
