# AI Trip Planner

AI Trip Planner is a Streamlit application that creates personalized travel plans from a few trip preferences. It combines LangGraph workflow orchestration with travel, weather, routing, hotel, attraction, budget, and itinerary services.

## Features

- Source and destination-based trip planning
- Configurable dates, traveller count, hotel rating, budget style, food preference, and transport preference
- Transport options with estimated prices, durations, and booking links
- Hotel recommendations with pricing, distance, address, and website links
- Weather forecasts for the destination
- Nearby attractions and sightseeing information
- Budget breakdown and per-person estimate
- AI-generated day-by-day itinerary
- Downloadable itinerary PDF
- Cached geocoding results to reduce repeated OpenRouteService requests

## Tech Stack

- Python 3.13+
- Streamlit
- LangGraph and LangChain
- Groq LLM API
- OpenRouteService geocoding and routing
- OpenWeather API
- Geoapify, OpenTripMap, Foursquare, and AviationStack integrations
- Pydantic data schemas
- ReportLab PDF generation

### 1. Clone the repository

```bash
git clone https://github.com/harshgoutam04/AI-Trip-Planner.git
cd AI-Trip-Planner
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root. Never commit this file or publish its values.

```dotenv
GROQ_API_KEY=your_groq_api_key
OPENTRIPMAP_API_KEY=your_opentripmap_api_key
GEOAPIFY_API_KEY=your_geoapify_api_key
FOURSQUARE_API_KEY=your_foursquare_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
OPENROUTESERVICE_API_KEY=your_openrouteservice_api_key
```

The application loads these values through `python-dotenv`. Obtain keys from the relevant provider dashboards and configure the same variables in your deployment platform.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## How To Use

1. Enter the source and destination.
2. Select travel dates, number of travellers, hotel rating, budget style, food preference, and transport preference.
3. Select **Plan My Trip**.
4. Review transport, hotel, weather, attractions, budget, and itinerary results.
5. Download the generated itinerary using the PDF button.

## Testing

Install the test runner if it is not already available:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest -q
```

## Deployment On Render

Create a new Web Service connected to this GitHub repository.

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

Add all required API keys as Render environment variables. Do not upload `.env` to the repository.

## Security Notes

- API keys must be stored in environment variables, never in source code.
- If a key is exposed publicly, revoke it and generate a replacement immediately.
- `.env`, `venv/`, Python caches, and compiled files are excluded by `.gitignore`.

## License

No license has been specified for this project yet.
