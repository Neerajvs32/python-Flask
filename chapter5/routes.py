import sys
import os

# Add the parent directory of 'chapter5' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app, db

# Your existing code here
