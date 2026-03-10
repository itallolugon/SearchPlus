import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    GOOGLE_VISION_API_KEY = os.getenv("GOOGLE_VISION_API_KEY")
