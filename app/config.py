import os

class Config:
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
