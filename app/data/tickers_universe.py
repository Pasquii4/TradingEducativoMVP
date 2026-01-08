"""Universo de ~150 tickers (por ahora hard-coded)."""

USA_TICKERS = [
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "BRK.B", "JNJ", "V",
    "WMT", "PG", "UNH", "MA", "CSGP", "HD", "PEP", "COST", "MCD", "AXP",
    "BA", "INTC", "AMD", "CRM", "NFLX", "ORCL", "IBM", "CSCO", "VZ", "T",
    "XOM", "CVX", "SLB", "COP", "MPC", "PSX", "OXY", "EOG", "MRO", "FANG",
    "C", "JPM", "BAC", "WFC", "GS", "MS", "USB", "BLK", "AIG", "PRU",
    "SOFI", "KKR", "BX", "APO", "ICE", "CME", "CBOE", "SPGI", "MSCI", "FTNT",
]

EU_TICKERS = [
    "SAP", "ALV.DE", "DAI.DE", "BMW.DE", "BAS.DE", "DBK.DE", "DB1.DE",
    "ASML", "PHIA.AS", "RDSA.AS", "UNVR.AS",
    "MC.PA", "OR.PA", "SU.PA", "EDF.PA", "BNP.PA",
    "TEF.MC", "BBVA.MC", "SAN.MC", "IBE.MC", "AMS.MC",
]

CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD",
    "ADA-USD", "DOGE-USD", "AVAX-USD", "MATIC-USD",
]

ALL_TICKERS = USA_TICKERS + EU_TICKERS + CRYPTO_TICKERS
