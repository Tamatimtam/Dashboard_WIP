"""
Loan Processor Module
Handles outstanding loan data analysis and categorization
"""
import pandas as pd
import numpy as np


class LoanProcessor:
    """Processes and analyzes outstanding loan data"""
    
    def __init__(self, df):
        """
        Initialize LoanProcessor with DataFrame
        
        Args:
            df (pd.DataFrame): DataFrame containing outstanding_loan column
        """
        self.df = df
        self.loan_categories = [
            {'name': 'No Loan', 'min': 0, 'max': 0, 'color': '#27ae60'},
            {'name': '<5M', 'min': 0.01, 'max': 5_000_000, 'color': '#3498db'},
            {'name': '5M-10M', 'min': 5_000_001, 'max': 10_000_000, 'color': '#f39c12'},
            {'name': '10M-15M', 'min': 10_000_001, 'max': 15_000_000, 'color': '#e67e22'},
            {'name': '>15M', 'min': 15_000_001, 'max': float('inf'), 'color': '#e74c3c'}
        ]
    
    def get_loan_statistics(self):
        """
        Calculate comprehensive loan statistics
        
        Returns:
            dict: Loan statistics including mean, median, distribution
        """
        loan_data = self.df['outstanding_loan'].replace(0, np.nan).dropna()
        
        if len(loan_data) == 0:
            return self._get_empty_stats()
        
        stats = {
            'total_respondents': len(self.df),
            'with_loan': int((self.df['outstanding_loan'] > 0).sum()),
            'without_loan': int((self.df['outstanding_loan'] == 0).sum()),
            'mean': float(loan_data.mean()),
            'median': float(loan_data.median()),
            'max': float(loan_data.max()),
            'min': float(loan_data.min()),
            'std': float(loan_data.std()),
            'total_outstanding': float(loan_data.sum())
        }
        
        # Calculate percentages
        stats['with_loan_pct'] = round((stats['with_loan'] / stats['total_respondents']) * 100, 1)
        stats['without_loan_pct'] = round((stats['without_loan'] / stats['total_respondents']) * 100, 1)
        
        return stats
    
    def get_loan_distribution(self):
        """
        Categorize loans into ranges for visualization
        
        Returns:
            dict: Distribution data with categories, counts, and percentages
        """
        distribution = []
        total = len(self.df)
        
        for category in self.loan_categories:
            if category['max'] == 0:
                # No loan category
                count = int((self.df['outstanding_loan'] == 0).sum())
            elif category['max'] == float('inf'):
                # Highest category
                count = int((self.df['outstanding_loan'] >= category['min']).sum())
            else:
                # Range categories
                count = int(((self.df['outstanding_loan'] >= category['min']) & 
                           (self.df['outstanding_loan'] <= category['max'])).sum())
            
            percentage = round((count / total) * 100, 1)
            
            distribution.append({
                'category': category['name'],
                'count': count,
                'percentage': percentage,
                'color': category['color']
            })
        
        return {
            'categories': [d['category'] for d in distribution],
            'counts': [d['count'] for d in distribution],
            'percentages': [d['percentage'] for d in distribution],
            'colors': [d['color'] for d in distribution]
        }
    
    def get_filtered_loan_stats(self, income_category=None):
        """
        Get loan statistics filtered by income category
        
        Args:
            income_category (str): Income category to filter by (e.g., '<2jt')
        
        Returns:
            dict: Filtered loan statistics
        """
        if income_category:
            filtered_df = self.df[self.df['avg_income_category'] == income_category]
        else:
            filtered_df = self.df
        
        if len(filtered_df) == 0:
            return self._get_empty_stats()
        
        loan_data = filtered_df['outstanding_loan'].replace(0, np.nan).dropna()
        
        if len(loan_data) == 0:
            return {
                'total_respondents': len(filtered_df),
                'with_loan': 0,
                'without_loan': len(filtered_df),
                'with_loan_pct': 0.0,
                'without_loan_pct': 100.0
            }
        
        stats = {
            'total_respondents': len(filtered_df),
            'with_loan': int((filtered_df['outstanding_loan'] > 0).sum()),
            'without_loan': int((filtered_df['outstanding_loan'] == 0).sum()),
            'mean': float(loan_data.mean()),
            'median': float(loan_data.median())
        }
        
        stats['with_loan_pct'] = round((stats['with_loan'] / stats['total_respondents']) * 100, 1)
        stats['without_loan_pct'] = round((stats['without_loan'] / stats['total_respondents']) * 100, 1)
        
        return stats
    
    def _get_empty_stats(self):
        """Return empty statistics structure"""
        return {
            'total_respondents': 0,
            'with_loan': 0,
            'without_loan': 0,
            'mean': 0.0,
            'median': 0.0,
            'max': 0.0,
            'min': 0.0,
            'std': 0.0,
            'total_outstanding': 0.0,
            'with_loan_pct': 0.0,
            'without_loan_pct': 0.0
        }
    
    def format_currency(self, amount):
        """
        Format amount as Indonesian Rupiah
        
        Args:
            amount (float): Amount to format
        
        Returns:
            str: Formatted currency string
        """
        if amount >= 1_000_000:
            return f"Rp {amount/1_000_000:.1f}M"
        elif amount >= 1_000:
            return f"Rp {amount/1_000:.1f}K"
        else:
            return f"Rp {amount:.0f}"
