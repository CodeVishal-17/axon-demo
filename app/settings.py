import os

class Settings:
    PYTHON_VERSION = "3.9"
    APP_SECRET = os.getenv("APP_SECRET", "default")
    DB_URL = os.getenv("DB_URL", "mysql://localhost/test")
    REDIS_ENABLED = os.getenv("REDIS_ENABLED", "false").lower() == "true"
    QUEUE_TYPE = os.getenv("QUEUE_TYPE", "celery")
    EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER", "smtp")
    NEW_ONBOARDING_FEATURE = os.getenv("NEW_ONBOARDING_FEATURE", "false").lower() == "true"
    RATE_LIMIT = 100
    PORT = 5000

settings = Settings()
