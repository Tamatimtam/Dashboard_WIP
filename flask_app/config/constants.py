"""
Application Constants and Configuration
Centralized configuration for the GenZ Financial Dashboard
"""

# Chart Configuration
CHART_CONFIG = {
    'displayModeBar': True,
    'displaylogo': False,
    'responsive': True,
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'income_vs_expense_chart',
        'height': 600,
        'width': 1200,
        'scale': 2
    }
}

# Category Order
CATEGORY_ORDER = ['N/A', '<2jt', '2-4jt', '4-6jt', '6-10jt', '10-15jt', '>15jt']

# Financial Standing Colors
FINANCIAL_STANDING_COLORS = {
    'Surplus': '#2ecc71',
    'Break-even': '#f39c12',
    'Deficit': '#e74c3c'
}

# Loan Categories
LOAN_CATEGORIES = [
    {'name': 'No Loan', 'min': 0, 'max': 0, 'color': '#27ae60'},
    {'name': '<5M', 'min': 0.01, 'max': 5_000_000, 'color': '#3498db'},
    {'name': '5M-10M', 'min': 5_000_001, 'max': 10_000_000, 'color': '#f39c12'},
    {'name': '10M-15M', 'min': 10_000_001, 'max': 15_000_000, 'color': '#e67e22'},
    {'name': '>15M', 'min': 15_000_001, 'max': float('inf'), 'color': '#e74c3c'}
]

# Education Level Order
EDUCATION_ORDER = [
    'Elementary School',
    'Junior High School',
    'Senior High School',
    'Diploma I/II/III',
    'Bachelor (S1)/Diploma IV',
    'Postgraduate'
]

# API Configuration
API_ENDPOINTS = {
    'stats': '/api/stats',
    'metrics': '/api/metrics',
    'chart_data': '/api/chart-data',
    'loan_filtered': '/api/loan-filtered',
    'loan_validation': '/api/loan-validation'
}

# Flask Configuration
FLASK_CONFIG = {
    'SECRET_KEY': 'your-secret-key-here-change-in-production',
    'DEBUG': True,
    'HOST': '0.0.0.0',
    'PORT': 5000
}

# File Paths
DATA_PATH = 'data'
CSV_FILENAME = 'dataset_gelarrasa_genzfinancialprofile.csv'
