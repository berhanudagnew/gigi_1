from pyrogram import Client
from os import getenv

from dotenv import load_dotenv
load_dotenv()
app = Client(
    "my_account",
    api_id=int(getenv("API_ID")),  # Replace with your actual API ID
    api_hash=getenv("API_HASH"),  # Replace with your actual API hash
)

with app:
    app.join_chat("g1link")  # Replace with the username or invite link of the channel
