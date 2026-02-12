import os

class Config:
    VERSION = os.environ.get("APP_VERSION", "1.0")
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
