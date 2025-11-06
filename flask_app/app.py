"""
Flask Dashboard Application
GenZ Financial Profile Analysis
"""
from flask import Flask, render_template
import os

# Import configuration
from config.constants import CSV_PATH, FLASK_CONFIG

# Import blueprints
from routes.pages import pages_bp
from routes.api import api_bp

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_CONFIG['SECRET_KEY']

    # Register blueprints
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    @app.errorhandler(404)
    def not_found(error):
        """Custom 404 error page"""
        return render_template(
            'error.html',
            error_message="The page you're looking for doesn't exist.",
            error_type="404 - Page Not Found"
        ), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Custom 500 error page"""
        app.logger.error(f"Internal server error: {str(error)}")
        return render_template(
            'error.html',
            error_message="An internal server error occurred.",
            error_type="500 - Internal Server Error"
        ), 500

    return app, CSV_PATH

if __name__ == '__main__':
    app, _ = create_app()
    
    # Check if data file exists before starting
    if not os.path.exists(CSV_PATH):
        print(f"❌ ERROR: Data file not found at {CSV_PATH}")
        print("Please ensure the CSV file is in the correct location.")
    else:
        print(f"✅ Starting Flask app...")
        print(f"✅ Data file found: {CSV_PATH}")
        print(f"🚀 Dashboard will be available at: http://localhost:{FLASK_CONFIG['PORT']}")
        
        # Run the Flask app
        # Debug mode ON for development - turn OFF in production
        app.run(
            debug=FLASK_CONFIG['DEBUG'],
            host=FLASK_CONFIG['HOST'],
            port=FLASK_CONFIG['PORT']
        )
