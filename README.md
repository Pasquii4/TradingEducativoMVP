# Trading Educativo MVP - Backend

AI-powered trading scanner + portfolio manager para educación y paper trading.

## Quick Start

### 1. Setup local

\`\`\`bash
git clone https://github.com/Pasquii4/TradingEducativoMVP.git
cd TradingEducativoMVP

python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

pip install -r requirements.txt
cp .env.example .env
# Edita .env con tus API keys
\`\`\`

### 2. PostgreSQL (Docker)

\`\`\`bash
docker-compose up -d postgres
# Espera 5-10s
\`\`\`

### 3. Init DB

\`\`\`bash
python init_db.py
\`\`\`

### 4. Run Backend

\`\`\`bash
uvicorn app.main:app --reload
# http://localhost:8000
# Docs: http://localhost:8000/docs
\`\`\`

## Stack

- FastAPI + SQLAlchemy 2.x
- PostgreSQL local
- JWT auth
- APScheduler (daily 21:00 CET)
- Claude API (IA)
- yfinance + NewsAPI

## Roadmap

- [x] Infra + DB setup
- [ ] Auth + Users
- [ ] Data layer
- [ ] AI integration
- [ ] Scheduler
- [ ] APIs
