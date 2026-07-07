# Market Pulse-Stock-Analytics-Dashboard
A real-time stock analytics dashboard built with Streamlit, yfinance, and Plotly.
Explore live price data, technical indicators, and compare performance across multiple tickers — including international markets like NSE/BSE.

Features


🔍 Single Stock View — candlestick chart with SMA20/SMA50 moving averages, volume, and RSI indicator
⚖️ Compare Mode — normalized % performance comparison across multiple tickers
🌍 Supports global tickers (US, NSE, BSE, LSE, etc. via exchange suffixes)
📊 Live data pulled from Yahoo Finance (no API key required)
⚡ Cached data fetching for fast repeat interactions
🎨 Custom dark theme UI

Getting Started

1. Clone the repo

bashgit clone https://github.com/swetha-nallamangai/market-pulse.git
cd market-pulse

2. Create a virtual environment (recommended)

bashpython -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies

bashpip install -r requirements.txt

4. Run the app

bashstreamlit run app.py

The app will open in your browser at http://localhost:8501.

Ticker Symbol Reference

MarketSuffixExampleUS (NASDAQ/NYSE)noneAAPL, MSFTIndia (NSE).NSINFY.NS, TCS.NSIndia (BSE).BORELIANCE.BOLondon (LSE).LHSBA.L

Look up exact symbols on Yahoo Finance if unsure.

Tech Stack

Streamlit — UI framework
yfinance — market data
Plotly — interactive charts
Pandas / NumPy — data processing
