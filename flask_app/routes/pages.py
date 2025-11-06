"""
Page-rendering routes for the Flask application
"""
from flask import Blueprint, render_template
from config.constants import CSV_PATH
from utils.data_loader import DataLoader
from utils.chart_generator import ChartGenerator

pages_bp = Blueprint('pages', __name__, template_folder='templates')

@pages_bp.route('/')
def index():
    """Home page - redirect to dashboard"""
    return dashboard()

@pages_bp.route('/dashboard')
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
        # Use the blueprint's logger
        pages_bp.logger.error(f"Dashboard error: {str(e)}")
        return render_template(
            'error.html',
            error_message=str(e),
            error_type="Unexpected Error"
        ), 500

@pages_bp.route('/about')
def about():
    """About page with project information"""
    return render_template('about.html')
