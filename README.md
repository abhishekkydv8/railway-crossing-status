# Railway Crossing Status API 🚦🚂

This project provides a FastAPI backend to determine the real-time status of railway crossings using:

- 📍 Google Maps Traffic API
- 🚆 Train tracking data (placeholder for NTES/RailYatri integration)

## Features

- Check nearby railway crossings from current GPS location
- Predict crossing status based on:
  - Real-time traffic congestion
  - Nearest train distance (simulated for now)
  
## Setup

### Requirements

- Python 3.8+
- A Google Maps API key with Directions API access

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/railway-crossing-status.git
cd railway-crossing-status
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --reload
```

### Environment

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_maps_api_key
```

## Deployment

Use [Railway.app](https://railway.app) or [Render.com](https://render.com) to deploy easily.

## License

[MIT](LICENSE)
