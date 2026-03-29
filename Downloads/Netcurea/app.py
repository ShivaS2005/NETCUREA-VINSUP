import sys
import os

# Add the Backend directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Syed Medigrid', 'VINSUP HOSPITAL', 'Backend'))

# Import and run the Flask app
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
