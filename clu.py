import anthropic 
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

LANGUAGE_MAP = {
    '.js': ('javascript', 'jest'),
    '.jsx': ('javasript', 'jest'),
    '.ts': ('typescript', 'jest'),
    '.tsx': ('typescript', 'jest'),
    '.py': ('python', 'pytest'),
    '.java': ('java', 'junit'),
    '.cpp': ('c++', 'googletest'),
    '.c': ('c', 'unity'),
    '.go': ('go', 'testing'),
    '.rs': ('rust', 'cargo teset'),
    '.rb': ('')
    '.php':
    '.swift':
    '.kt':

}