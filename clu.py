import anthropic 
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

LANGUAGE_MAP = {
    '.js'
}