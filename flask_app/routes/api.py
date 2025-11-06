"""
API routes for the Flask application
"""
from flask import Blueprint, jsonify
import urllib.parse
from config.constants import CSV_PATH
from utils.data_loader import DataLoader

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/stats')
def api_stats():
    """API endpoint to get dataset statistics in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        stats = data_loader.get_dataset_stats()
        return jsonify(stats)
    except Exception as e:
        api_bp.logger.error(f"API stats error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/metrics')
def api_metrics():
    """API endpoint to get key metrics in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        metrics = data_loader.get_key_metrics()
        return jsonify(metrics)
    except Exception as e:
        api_bp.logger.error(f"API metrics error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/chart-data')
def api_chart_data():
    """API endpoint to get chart data in JSON format"""
    try:
        data_loader = DataLoader(CSV_PATH)
        data_loader.load_data()
        chart_data = data_loader.get_chart_data()
        return jsonify(chart_data)
    except Exception as e:
        api_bp.logger.error(f"API chart-data error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/loan-filtered/<category>')
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
        api_bp.logger.error(f"API loan-filtered error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/loan-validation')
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
        api_bp.logger.error(f"API loan-validation error: {str(e)}")
        return jsonify({'error': str(e)}), 500
