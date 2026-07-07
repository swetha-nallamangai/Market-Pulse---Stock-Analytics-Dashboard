"""
Market Pulse — Real-Time Stock Analytics Dashboard
A Streamlit app for exploring live stock data, technical indicators,
and multi-stock performance comparison.
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# --------------------------------------------------------------------------
# Page config & styling
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Market Pulse | Stock Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px 15px 5px 15px;
    }
    div[data-testid="stMetricLabel"] { font-size: 14px; color: #8b949e; }
    h1, h2, h3 { color: #e6edf3; }
    .stApp { font-family: 'Inter', sans-serif; }
    section[data-testid="stSidebar"] { background-color: #161b22; }
    .block-container { padding-top: 2rem; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------------------------------------------------------
# Data helpers
# --------------------------------------------------------------------------
@st.cache_data(ttl=300, show_spinner=False)
def fetch_history(ticker: str, period: str, interval: str) -> pd.DataFrame:
    """Download historical OHLCV data for a ticker."""
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    return data


@st.cache_data(ttl=300, show_spinner=False)
def fetch_info(ticker: str) -> dict:
    """Fetch summary info/metadata for a ticker."""
    try:
        return yf.Ticker(ticker).fast_info
    except Exception:
        return {}


def add_moving_averages(df: pd.DataFrame, windows=(20, 50)) -> pd.DataFrame:
    for w in windows:
        df[f"SMA{w}"] = df["Close"].rolling(window=w).mean()
    return df


def compute_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))
    return rsi


def pct_change_series(df: pd.DataFrame) -> pd.Series:
    """Normalize a price series to % change from the first value."""
    return (df["Close"] / df["Close"].iloc[0] - 1) * 100


# --------------------------------------------------------------------------
# Sidebar controls
# --------------------------------------------------------------------------
st.sidebar.title("📈 Market Pulse")
st.sidebar.caption("Real-time stock analytics dashboard")

mode = st.sidebar.radio("Mode", ["Single Stock", "Compare Stocks"])

period_map = {
    "1 Month": "1mo", "3 Months": "3mo", "6 Months": "6mo",
    "1 Year": "1y", "2 Years": "2y", "5 Years": "5y",
}
period_label = st.sidebar.selectbox("Time Range", list(period_map.keys()), index=2)
period = period_map[period_label]
interval = "1d" if period not in ("1mo",) else "1d"

st.sidebar.markdown("---")

# --------------------------------------------------------------------------
# Single stock view
# --------------------------------------------------------------------------
if mode == "Single Stock":
    ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL").upper().strip()
    show_rsi = st.sidebar.checkbox("Show RSI indicator", value=True)

    st.title(f"{ticker} — Overview")

    if ticker:
        with st.spinner(f"Fetching data for {ticker}..."):
            df = fetch_history(ticker, period, interval)

        if df.empty:
            st.error(f"No data found for ticker '{ticker}'. Check the symbol and try again.")
        else:
            df = add_moving_averages(df.copy())
            df["RSI"] = compute_rsi(df)

            latest = df.iloc[-1]
            prev = df.iloc[-2] if len(df) > 1 else latest
            change = latest["Close"] - prev["Close"]
            pct = (change / prev["Close"]) * 100 if prev["Close"] else 0

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Last Close", f"${latest['Close']:.2f}", f"{change:+.2f} ({pct:+.2f}%)")
            c2.metric("Day High", f"${latest['High']:.2f}")
            c3.metric("Day Low", f"${latest['Low']:.2f}")
            c4.metric("Volume", f"{latest['Volume']:,.0f}")

            # Candlestick + moving averages
            rows = 3 if show_rsi else 2
            row_heights = [0.55, 0.2, 0.25] if show_rsi else [0.7, 0.3]
            fig = make_subplots(
                rows=rows, cols=1, shared_xaxes=True,
                vertical_spacing=0.03, row_heights=row_heights,
            )
            fig.add_trace(go.Candlestick(
                x=df.index, open=df["Open"], high=df["High"],
                low=df["Low"], close=df["Close"], name=ticker,
            ), row=1, col=1)
            fig.add_trace(go.Scatter(x=df.index, y=df["SMA20"], name="SMA 20",
                                      line=dict(color="#58a6ff", width=1.3)), row=1, col=1)
            fig.add_trace(go.Scatter(x=df.index, y=df["SMA50"], name="SMA 50",
                                      line=dict(color="#f0883e", width=1.3)), row=1, col=1)

            fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume",
                                  marker_color="#30363d"), row=2, col=1)

            if show_rsi:
                fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], name="RSI",
                                          line=dict(color="#a371f7", width=1.3)), row=3, col=1)
                fig.add_hline(y=70, line_dash="dot", line_color="#f85149", row=3, col=1)
                fig.add_hline(y=30, line_dash="dot", line_color="#3fb950", row=3, col=1)

            fig.update_layout(
                template="plotly_dark", height=650, showlegend=True,
                xaxis_rangeslider_visible=False,
                margin=dict(l=10, r=10, t=30, b=10),
                paper_bgcolor="#0e1117", plot_bgcolor="#0e1117",
            )
            st.plotly_chart(fig, use_container_width=True)

            with st.expander("Show raw data"):
                st.dataframe(df.tail(100).sort_index(ascending=False), use_container_width=True)

# --------------------------------------------------------------------------
# Compare stocks view
# --------------------------------------------------------------------------
else:
    tickers_input = st.sidebar.text_input(
        "Tickers (comma-separated)", value="AAPL, MSFT, GOOGL"
    )
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

    st.title("Performance Comparison")
    st.caption(f"Normalized % return over {period_label.lower()}")

    if tickers:
        fig = go.Figure()
        summary_rows = []

        with st.spinner("Fetching data..."):
            for t in tickers:
                df = fetch_history(t, period, interval)
                if df.empty:
                    st.warning(f"No data for '{t}' — skipping.")
                    continue
                pct_series = pct_change_series(df)
                fig.add_trace(go.Scatter(
                    x=df.index, y=pct_series, name=t, mode="lines",
                    line=dict(width=2),
                ))
                total_return = pct_series.iloc[-1]
                summary_rows.append({
                    "Ticker": t,
                    "Total Return": f"{total_return:+.2f}%",
                    "Last Price": f"${df['Close'].iloc[-1]:.2f}",
                })

        fig.update_layout(
            template="plotly_dark", height=550,
            paper_bgcolor="#0e1117", plot_bgcolor="#0e1117",
            yaxis_title="% Change", margin=dict(l=10, r=10, t=30, b=10),
        )
        fig.add_hline(y=0, line_dash="dot", line_color="#8b949e")
        st.plotly_chart(fig, use_container_width=True)

        if summary_rows:
            st.subheader("Summary")
            st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit, yfinance & Plotly")
