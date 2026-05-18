# Flask Web Application 🚀

A production-ready Flask web application with Docker support, RESTful API endpoints, and an interactive web interface.

## Features

- ✨ **Modern Web Interface** - Beautiful, responsive dashboard
- 🔌 **RESTful API** - Multiple API endpoints for integration
- 🐳 **Docker Ready** - Complete Docker and Docker Compose configuration
- 🔒 **Secure** - Non-root user execution, health checks
- ⚡ **Scalable** - Gunicorn multi-worker setup
- 📊 **Status Monitoring** - Built-in health check endpoint

## API Endpoints

### 1. **Hello Endpoint** - GET/POST `/api/hello`
Returns a greeting message.

**Query Parameter (GET):**
```
GET /api/hello?name=John
```

**Request Body (POST):**
```json
POST /api/hello
{
  "name": "John"
}
```

**Response:**
```json
{
  "message": "Hello, John!",
  "status": "success"
}
```

### 2. **Status Endpoint** - GET `/api/status`
Health check endpoint for monitoring.

**Request:**
```
GET /api/status
```

**Response:**
```json
{
  "status": "running",
  "environment": "production"
}
```

### 3. **Echo Endpoint** - POST `/api/echo`
Echoes back the sent JSON data.

**Request:**
```json
POST /api/echo
{
  "message": "Hello, API!"
}
```

**Response:**
```json
{
  "echo": {
    "message": "Hello, API!"
  },
  "received_at": "127.0.0.1"
}
```

## Getting Started

### Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/dinarex55/flaskweb.git
cd flaskweb
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

5. **Open in browser:**
```
http://localhost:5000
```

### Docker Deployment

1. **Build and run with Docker Compose:**
```bash
docker-compose up --build
```

2. **Access the application:**
```
http://localhost:5000
```

3. **Stop the application:**
```bash
docker-compose down
```

### Manual Docker Build

```bash
# Build image
docker build -t flaskweb .

# Run container
docker run -p 5000:5000 flaskweb
```

## Project Structure

```
flaskweb/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose configuration
├── .gitignore            # Git ignore rules
├── .dockerignore          # Docker ignore rules
├── templates/
│   └── index.html        # Interactive web interface
└── README.md             # This file
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
PORT=5000
```

## Requirements

- Python 3.11+
- Docker (optional)
- Docker Compose (optional)

## Dependencies

- Flask 3.0.0
- Flask-CORS 4.0.0
- Gunicorn 21.2.0
- Werkzeug 3.0.0

## Testing

Test the API endpoints:

```bash
# Hello endpoint
curl -X POST http://localhost:5000/api/hello -H "Content-Type: application/json" -d '{"name":"John"}'

# Status endpoint
curl http://localhost:5000/api/status

# Echo endpoint
curl -X POST http://localhost:5000/api/echo -H "Content-Type: application/json" -d '{"message":"Hello"}'
```

## Docker Features

- **Health Checks**: Automatic monitoring of application status
- **Multi-worker**: Gunicorn with 4 workers for production load
- **Security**: Non-root user execution
- **Optimization**: Multi-stage build and layer caching
- **Volume Mounting**: Easy development with live code changes

## Performance

- Gunicorn workers: 4
- Worker class: sync
- Timeout: 120 seconds
- Health check interval: 30 seconds

## Troubleshooting

### Port already in use
```bash
# Change port in docker-compose.yml or run on different port
docker run -p 8000:5000 flaskweb
```

### Container health check failing
```bash
# Check logs
docker logs flaskweb
```

### Application not responding
```bash
# Verify status endpoint
curl http://localhost:5000/api/status
```

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please visit: https://github.com/dinarex55/flaskweb/issues

---

**Made with ❤️ using Flask and Docker**
