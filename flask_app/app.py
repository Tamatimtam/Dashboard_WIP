"""
Flask Dashboard Application
GenZ Financial Profile Analysis
"""
from flask import Flask, render_template, jsonify
import os
from utils.data_loader import DataLoader
from utils.chart_generator import ChartGenerator

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Path to CSV data
CSV_PATH = os.path.join('data', 'dataset_gelarrasa_genzfinancialprofile.csv')

# Initialize data loader
data_loader = DataLoader(CSV_PATH)


@app.route('/')
def index():
    """Home page - redirect to dashboard"""
    return dashboard()


@app.route('/dashboard')
def dashboard():
    """
    Main dashboard page
    Displays dataset statistics and the Diverging Bar Chart
    """
    try:
        # Load data
        data_loader.load_data()
        
        # Get dataset statistics
        stats = data_loader.get_dataset_stats()
        
        # Get key metrics
        metrics = data_loader.get_key_metrics()
        
        # Get chart data
        chart_data = data_loader.get_chart_data()
        profession_data = data_loader.get_profession_chart_data()
        education_data = data_loader.get_education_chart_data()
        
        # Generate charts
        chart_html = ChartGenerator.create_diverging_bar_chart(chart_data)
        profession_chart = ChartGenerator.create_profession_chart(profession_data)
        education_chart = ChartGenerator.create_education_chart(education_data)
        
        return render_template(
            'dashboard.html',
            stats=stats,
            metrics=metrics,
            chart_html=chart_html,
            profession_chart=profession_chart,
            education_chart=education_chart
        )
    
    except FileNotFoundError as e:
        return render_template(
            'error.html',
            error_message=str(e),
            error_type="File Not Found"
        ), 404
    
    except Exception as e:
        return render_template(
            'error.html',
            error_message=str(e),
            error_type="Unexpected Error"
        ), 500


@app.route('/api/stats')
def api_stats():
    """
    API endpoint to get dataset statistics in JSON format
    Useful for AJAX requests or future extensions
    """
    try:
        stats = data_loader.get_dataset_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/metrics')
def api_metrics():
    """
    API endpoint to get key metrics in JSON format
    """
    try:
        metrics = data_loader.get_key_metrics()
        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chart-data')
def api_chart_data():
    """
    API endpoint to get chart data in JSON format
    """
    try:
        chart_data = data_loader.get_chart_data()
        return jsonify(chart_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/about')
def about():
    """About page with project information"""
    return render_template('about.html')


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
    return render_template(
        'error.html',
        error_message="An internal server error occurred.",
        error_type="500 - Internal Server Error"
    ), 500


if __name__ == '__main__':
    # Run the Flask app
    # Debug mode ON for development - turn OFF in production
    app.run(debug=True, host='127.0.0.1', port=5000)
