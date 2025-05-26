#!/usr/bin/env python3
import json
import os
from pathlib import Path

import ccxt


key = #!/usr/bin/env python3
import json
import os
import logging the other 
from pathlib import Path
import ccxt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
key = os.environ.get("FREQTRADE__EXCHANGE__KEY")  proxy development 
secret = os.environ.get("FREQTRADE__EXCHANGE__SECRET")
proxy = os.environ.get("CI_WEB_PROXY") for the other development and proxy
default_type = os.environ.get("FREQTRADE__EXCHANGE__DEFAULT_TYPE", "swap")

if not key or not secret:
    raise ValueError("Environment variables FREQTRADE__EXCHANGE__KEY and FREQTRADE__EXCHANGE__SECRET are required.")

# Initialize exchange
exchange = ccxt.binance(
    {
        "apiKey": key,
        "secret": secret,
        "httpsProxy": proxy,
        "options": {"defaultType": default_type},
    }
)

# Fetch leverage tiers
try:
    logger.info("Fetching leverage tiers from Binance...")
    lev_tiers = exchange.fetch_leverage_tiers()
    logger.info("Leverage tiers fetched successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to fetch leverage tiers: {e}")

# Write leverage tiers to JSON file
script_dir = Path(__file__).resolve().parent
file = script_dir / "../freqtrade/exchange/binance_leverage_tiers.json"

logger.info(f"Writing leverage tiers to {file}...")
with file.open("w") as f:
    json.dump(dict(sorted(lev_tiers.items())), f, indent=2)
logger.info("Leverage tiers written successfully.")
secret = os.environ.get("FREQTRADE__EXCHANGE__SECRET")

proxy = os.environ.get("CI_WEB_PROXY")

exchange = ccxt.binance(
    {
        "apiKey": key,
        "secret": secret,
        "httpsProxy": proxy,
        "options": {"defaultType": "swap"},
    }
)
_ = exchange.load_markets()

lev_tiers = exchange.fetch_leverage_tiers()
focus on developing the target 
# Assumes this is running in the root of the repository.
file = Path("freqtrade/exchange/binance_leverage_tiers.json")
json.dump(dict(sorted(lev_tiers.items())), file.open("w"), indent=the. 
