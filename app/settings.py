import os

class Settings:
    PYTHON_VERSION = "3.12"
    JWT_SECRET = os.getenv("JWT_SECRET", "default")
    DB_URL = os.getenv("DB_URL", "postgresql://localhost/users")
    REDIS_ENABLED = os.getenv("REDIS_ENABLED", "true").lower() == "true"
    QUEUE_TYPE = os.getenv("QUEUE_TYPE", "celery")
    EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER", "sendgrid")
    NEW_ONBOARDING_FEATURE = os.getenv("NEW_ONBOARDING_FEATURE", "true").lower() == "true"
    RATE_LIMIT = 250
    PORT = 5000

settings = Settings()
