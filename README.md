# User Service
A microservice for managing user profiles and authentication.

## Architecture
- Python 3.9
- MySQL database for storage
- Celery for queueing background tasks (e.g. sending emails)
- File-based logging to `app.log`
- Returns XML responses by default for legacy compatibility.

## Deployment
Deployment is strictly via Docker Compose.
The service runs on port 5000.

## Configuration
Requires the `APP_SECRET` environment variable for authentication.
