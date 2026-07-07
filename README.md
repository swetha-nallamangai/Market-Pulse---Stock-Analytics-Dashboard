# 📈 Market Pulse

A real-time stock analytics dashboard built with Streamlit, yfinance, and Plotly.

Explore live price data, technical indicators, and compare performance across multiple tickers — including international markets like NSE, BSE, NYSE, NASDAQ, and more.

---

## ✨ Features

### 🔍 Single Stock View

* Interactive candlestick chart
* SMA20 and SMA50 moving averages
* Volume analysis
* RSI (Relative Strength Index) indicator

### ⚖️ Compare Mode

* Compare multiple stocks simultaneously
* Normalized percentage performance visualization
* Easy benchmarking across sectors and markets

### 🌍 Global Market Support

Supports Yahoo Finance ticker symbols from:

* US Markets (NYSE, NASDAQ)
* NSE (India)
* BSE (India)
* LSE (London)
* Other Yahoo Finance supported exchanges

### 📊 Live Market Data

* Real-time market data from Yahoo Finance
* No API key required

### ⚡ Fast Performance

* Streamlit caching for faster repeated queries
* Efficient data loading and processing

### 🎨 Modern UI

* Custom dark theme
* Responsive and interactive charts
* Clean dashboard layout

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/swetha-nallamangai/market-pulse.git
cd market-pulse
```

### 2. Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser at:

```text
http://localhost:8501
```

---

## 📌 Ticker Symbol Reference

| Market           | Suffix | Example         |
| ---------------- | ------ | --------------- |
| US (NASDAQ/NYSE) | None   | AAPL, MSFT      |
| India (NSE)      | .NS    | INFY.NS, TCS.NS |
| India (BSE)      | .BO    | RELIANCE.BO     |
| London (LSE)     | .L     | HSBA.L          |

> Note: You can find ticker symbols directly on Yahoo Finance.

---

## 🛠️ Tech Stack

* **Streamlit** — Interactive web application framework
* **yfinance** — Yahoo Finance market data
* **Plotly** — Interactive financial visualizations
* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computations

---

## 📂 Project Structure

```text
market-pulse/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── data.py
│   └── indicators.py
│
├── assets/
│   └── dashboard.png
│
└── .gitignore
```

---

## 🔮 Future Enhancements

* Portfolio tracking
* Watchlists
* News sentiment analysis
* AI-powered stock insights
* Export reports to PDF/Excel
* Additional technical indicators

---

Tech Stack

Streamlit — UI framework
yfinance — market data
Plotly — interactive charts
Pandas / NumPy — data processing
