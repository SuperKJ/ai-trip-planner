# AI Trip Planner

An AI-powered travel planning assistant that creates detailed itineraries, estimates costs, and provides real-time recommendations.

## Features - Demo


https://github.com/user-attachments/assets/35208530-bdeb-4811-949b-358d3a7ebee5



## Features

- **Trip Planning**: Day-by-day itineraries with popular and off-beat recommendations
- **Real-time Data**: Weather, places, currency rates, and cost breakdowns
- **Cost Analysis**: Detailed expense estimates for hotels, food, and activities
- **Multiple LLM Support**: Groq and OpenAI integration

## Tech Stack

**AI & LLMs**: LangChain, LangGraph (ReAct pattern), Groq, OpenAI

**Backend**: FastAPI, Pydantic, Uvicorn

**Frontend**: Streamlit

**APIs**: OpenWeatherMap, ExchangeRate API, Google Places, Tavily Search

**Data**: Pandas, NumPy, Python 3.12+

## Setup

### Prerequisites
Get API keys from:
- [Groq](https://console.groq.com)
- [OpenWeatherMap](https://openweathermap.org/api)
- [ExchangeRate API](https://www.exchangerate-api.com)

### Installation

```bash
git clone https://github.com/SuperKJ/ai-trip-planner.git
cd ai-trip-planner

python -m venv venv
venv\Scripts\activate  # Windows or source venv/bin/activate for macOS/Linux

pip install -r requirements.txt
```

Create `.env` file:
```
GROQ_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
EXCHANGE_RATE_API_KEY=your_key
```

Update `config/config.yaml` with your settings.

## Running

```bash
# Terminal 1 - Backend
python -m uvicorn main:app --reload --port 8000

# Terminal 2 - Frontend
streamlit run app.py
```

Visit `http://localhost:8501`

## How It Works

1. Enter a travel query (e.g., "Plan a 5-day trip to Thailand")
2. AI agent uses tools to gather real-time data
3. Creates comprehensive travel plan with itineraries and costs
4. Displays results with day-by-day breakdown

## Project Structure

```
├── agent/              # Agentic workflow
├── tools/              # Weather, places, currency, calculator tools
├── utils/              # API integrations and utilities
├── config/             # Configuration
├── main.py             # FastAPI backend
├── app.py              # Streamlit frontend
└── requirements.txt
```

## Author

Kanishk Joshi - [GitHub](https://github.com/SuperKJ)
