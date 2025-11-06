"""
Flask Dashboard Application
GenZ Financial Profile Analysis
"""
from flask import Flask, render_template, jsonify
import os
import urllib.parse
from utils.data_loader import DataLoader
from utils.chart_generator import ChartGenerator

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Path to CSV data
CSV_PATH = os.path.join('data', 'dataset_gelarrasa_genzfinancialprofile.csv')

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
        # Initialize data loader
        data_loader = DataLoader(CSV_PATH)
        
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
        
        # Get loan overview data (for KPI cards only - chart rendered client-side)
        loan_overview = data_loader.get_loan_overview_data()
        loan_stats = loan_overview['statistics']
        
        # Generate charts (loan chart will be rendered client-side)
        chart_html = ChartGenerator.create_diverging_bar_chart(chart_data)
        profession_chart = ChartGenerator.create_profession_chart(profession_data)
        education_chart = ChartGenerator.create_education_chart(education_data)
        
        return render_template(
            'dashboard.html',
            stats=stats,
            metrics=metrics,
            chart_html=chart_html,
            profession_chart=profession_chart,
            education_chart=education_chart,
            loan_stats=loan_stats
        )
    
    except FileNotFoundError as e:
        return render_template(
            'error.html',
            error_message=str(e),
            error_type="File Not Found"
        ), 404
    
    except Exception as e:
        app.logger.error(f"Dashboard error: {str(e)}")
        return render_template(
            'error.html',
            error_message=str(e),
            error_type="Unexpected Error"
        ), 500


@app.route('/api/stats')
def api_stats():
    """API endpoint to get dataset statistics in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        stats = data_loader.get_dataset_stats()
        return jsonify(stats)
    except Exception as e:
        app.logger.error(f"API stats error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/metrics')
def api_metrics():
    """API endpoint to get key metrics in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        metrics = data_loader.get_key_metrics()
        return jsonify(metrics)
    except Exception as e:
        app.logger.error(f"API metrics error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/chart-data')
def api_chart_data():
    """API endpoint to get chart data in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        chart_data = data_loader.get_chart_data()
        return jsonify(chart_data)
    except Exception as e:
        app.logger.error(f"API chart-data error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/loan-filtered/<category>')
def api_loan_filtered(category):
    """
    API endpoint to get filtered loan data by income category
    
    Args:
        category (str): Income category or 'All' for unfiltered data
    
    Returns:
        JSON response with filtered loan statistics and distribution
    """
    try:
        # Decode category (handle URL encoding)
        decoded_category = urllib.parse.unquote(category)
        
        # Validate category
        valid_categories = ['All', 'N/A', '<2jt', '2-4jt', '4-6jt', '6-10jt', '10-15jt', '>15jt']
        if decoded_category not in valid_categories:
            return jsonify({'error': f'Invalid category: {decoded_category}'}), 400
        
        # Load data and get filtered results
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        
        filtered_data = data_loader.get_filtered_loan_overview(decoded_category)
        return jsonify(filtered_data)
        
    except Exception as e:
        app.logger.error(f"API loan-filtered error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/loan-validation')
def api_loan_validation():
    """
    API endpoint to get loan data validation report
    
    Returns:
        JSON response with validation statistics and issues
    """
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        
        validation_report = data_loader.get_loan_validation_report()
        return jsonify(validation_report)
    except Exception as e:
        app.logger.error(f"API loan-validation error: {str(e)}")
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
    app.logger.error(f"Internal server error: {str(error)}")
    return render_template(
        'error.html',
        error_message="An internal server error occurred.",
        error_type="500 - Internal Server Error"
    ), 500


if __name__ == '__main__':
    # Check if data file exists before starting
    if not os.path.exists(CSV_PATH):
        print(f"❌ ERROR: Data file not found at {CSV_PATH}")
        print("Please ensure the CSV file is in the correct location.")
    else:
        print(f"✅ Starting Flask app...")
        print(f"✅ Data file found: {CSV_PATH}")
        print(f"🚀 Dashboard will be available at: http://localhost:5000")
        
        # Run the Flask app
        # Debug mode ON for development - turn OFF in production
        app.run(debug=True, host='0.0.0.0', port=5000)
