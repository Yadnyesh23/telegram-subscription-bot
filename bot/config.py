import os
from dotenv import load_dotenv

load_dotenv()

API_ID=int(os.getenv("API_ID"))
API_HASH=os.getenv("API_HASH")
BOT_TOKEN=os.getenv("BOT_TOKEN")

MONGO_URI=os.getenv("MONGO_URI")

# STRIPE_SECRET_KEY=os.getenv("STRIPE_SECRET_KEY")
# STRIPE_WEBHOOK_SECRET=os.getenv("STRIPE_WEBHOOK_SECRET")

ADMIN_IDS=int(os.getenv("ADMIN_IDS"))
FORCE_SUB_CHANNEL=os.getenv("FORCE_SUB_CHANNEL")