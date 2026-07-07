# 📈 Market Pulse — Stock Analytics Dashboard

A real-time stock analytics dashboard built with **Streamlit**, **yfinance**, and **Plotly**.
Explore live price data, technical indicators, and compare performance across multiple tickers.

## Features

- 🔍 **Single Stock View** — candlestick chart with SMA20/SMA50 moving averages, volume, and RSI indicator
- ⚖️ **Compare Mode** — normalized % performance comparison across multiple tickers
- 📊 Live data pulled from Yahoo Finance (no API key required)
- ⚡ Cached data fetching for fast repeat interactions
- 🎨 Custom dark theme UI

## Demo

*(Add a screenshot or GIF here once deployed — e.g. via [Streamlit Community Cloud](https://streamlit.io/cloud))*

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/market-pulse.git
cd market-pulse
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [yfinance](https://github.com/ranaroussi/yfinance) — market data
- [Plotly](https://plotly.com/python/) — interactive charts
- [Pandas](https://pandas.pydata.org/) / [NumPy](https://numpy.org/) — data processing

## Deploy for Free

Push this repo to GitHub, then deploy instantly on [Streamlit Community Cloud](https://share.streamlit.io/) — point it at `app.py` and you're live.

## License

MIT
