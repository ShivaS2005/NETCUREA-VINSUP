import sys
import os
from flask import Flask, send_from_directory

# Add the Backend directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Syed Medigrid', 'VINSUP HOSPITAL', 'Backend'))

# Import and run the Flask app
from app import app

# Configure Flask to serve frontend static files
@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=None):
    frontend_dist = os.path.join(os.path.dirname(__file__), 'Syed Medigrid', 'VINSUP HOSPITAL', 'frontend', 'dist')
    
    # If path is empty, serve index.html
    if not path:
        return send_from_directory(frontend_dist, 'index.html')
    
    # Try to serve the requested file
    try:
        return send_from_directory(frontend_dist, path)
    except:
        # If file not found, serve index.html for SPA routing
        return send_from_directory(frontend_dist, 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
