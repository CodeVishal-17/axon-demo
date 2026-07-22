# API Documentation

## Endpoints
- `GET /health` - Health check
- `GET /api/v2/users` - Fetch user list (Returns JSON: {"users": [{"id": 1, "name": "Alice"}]}; requires verify_token; enqueues background_job)

## Rate Limits
The API is rate limited to 100 requests/minute per IP.

## Response Format
Responses are formatted in XML.
