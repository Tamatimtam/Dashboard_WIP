"""
Data Loader Module
Handles CSV loading, preprocessing, and statistics calculation
"""
import pandas as pd
import os
from .loan_processor import LoanProcessor


class DataLoader:
    """Handles loading and processing of the GenZ Financial Profile dataset"""
    
    def __init__(self, csv_path):
        """
        Initialize DataLoader with path to CSV file
        
        Args:
            csv_path (str): Path to the CSV file
        """
        self.csv_path = csv_path
        self.df = None
        self.category_order = ['N/A', '<2jt', '2-4jt', '4-6jt', '6-10jt', '10-15jt', '>15jt']
        
    def load_data(self):
        """Load CSV data into pandas DataFrame"""
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
        
        self.df = pd.read_csv(self.csv_path)
        return self.df
    
    def get_dataset_stats(self):
        """
        Calculate comprehensive dataset statistics
        
        Returns:
            dict: Dictionary containing dataset statistics
        """
        if self.df is None:
            self.load_data()
        
        # Basic statistics
        total_rows = len(self.df)
        total_columns = len(self.df.columns)
        
        # Missing values analysis
        missing_data = []
        for col in self.df.columns:
            missing_count = self.df[col].isnull().sum()
            if missing_count > 0:
                missing_pct = round((missing_count / total_rows) * 100, 2)
                missing_data.append({
                    'column': col,
                    'count': int(missing_count),
                    'percentage': missing_pct
                })
        
        # Category distributions for key columns
        income_cats = self.df['avg_income_category'].value_counts().to_dict()
        expense_cats = self.df['avg_expense_category'].value_counts().to_dict()
        financial_standing = self.df['financial_standing'].value_counts().to_dict()
        
        # Numerical summaries
        income_stats = self.df['avg_monthly_income'].describe().to_dict() if 'avg_monthly_income' in self.df.columns else {}
        expense_stats = self.df['avg_monthly_expense'].describe().to_dict() if 'avg_monthly_expense' in self.df.columns else {}
        
        return {
            'total_rows': total_rows,
            'total_columns': total_columns,
            'missing_data': missing_data,
            'income_categories': income_cats,
            'expense_categories': expense_cats,
            'financial_standing': financial_standing,
            'income_stats': income_stats,
            'expense_stats': expense_stats
        }
    
    def get_chart_data(self):
        """
        Prepare data specifically for the Diverging Bar Chart
        
        Returns:
            dict: Dictionary containing processed data for visualization
        """
        if self.df is None:
            self.load_data()
        
        # Calculate frequency counts
        income_counts = self.df['avg_income_category'].value_counts()
        expense_counts = self.df['avg_expense_category'].value_counts()
        
        # Calculate percentages
        income_pct = (income_counts / income_counts.sum() * 100).round(2)
        expense_pct = (expense_counts / expense_counts.sum() * 100).round(2)
        
        # Create combined dataframe
        viz_data = pd.DataFrame({
            'Income_Count': income_counts,
            'Income_Percentage': income_pct,
            'Expense_Count': expense_counts,
            'Expense_Percentage': expense_pct
        }).fillna(0)
        
        # Reindex to ensure proper category order
        existing_categories = [cat for cat in self.category_order if cat in viz_data.index]
        viz_data = viz_data.reindex(existing_categories)
        
        # Convert to dictionary format for JSON serialization
        chart_data = {
            'categories': list(viz_data.index),
            'income_percentages': viz_data['Income_Percentage'].tolist(),
            'expense_percentages': viz_data['Expense_Percentage'].tolist(),
            'income_counts': viz_data['Income_Count'].astype(int).tolist(),
            'expense_counts': viz_data['Expense_Count'].astype(int).tolist()
        }
        
        return chart_data
    
    def get_profession_chart_data(self):
        """
        Prepare real data for Profession/Employment Status chart
        Shows financial standing distribution by employment status
        
        Returns:
            dict: Dictionary containing profession data with financial standing breakdown
        """
        if self.df is None:
            self.load_data()
        
        # Group by employment status and financial standing
        profession_standing = pd.crosstab(
            self.df['employment_status'], 
            self.df['financial_standing'], 
            normalize='index'
        ) * 100  # Convert to percentage
        
        # Order employment categories by most common
        employment_counts = self.df['employment_status'].value_counts()
        profession_standing = profession_standing.reindex(employment_counts.index)
        
        # Prepare data for stacked bar chart
        categories = profession_standing.index.tolist()
        
        # Financial standing colors (consistent with theme)
        colors = {
            'Surplus': '#2ecc71',    # Green
            'Break-even': '#f39c12', # Orange
            'Deficit': '#e74c3c'     # Red
        }
        
        chart_data = {
            'categories': categories,
            'financial_standings': list(profession_standing.columns),
            'data': {},
            'colors': colors,
            'total_counts': employment_counts.to_dict()
        }
        
        # Add percentage data for each financial standing
        for standing in profession_standing.columns:
            if standing in profession_standing.columns:
                chart_data['data'][standing] = profession_standing[standing].round(1).tolist()
            else:
                chart_data['data'][standing] = [0] * len(categories)
        
        return chart_data
    
    def get_education_chart_data(self):
        """
        Prepare real data for Education Level chart
        Shows financial standing distribution by education level
        
        Returns:
            dict: Dictionary containing education data with financial standing breakdown
        """
        if self.df is None:
            self.load_data()
        
        # Define education level order (from lowest to highest)
        education_order = [
            'Elementary School',
            'Junior High School',
            'Senior High School',
            'Diploma I/II/III',
            'Bachelor (S1)/Diploma IV',
            'Postgraduate'
        ]
        
        # Group by education level and financial standing
        education_standing = pd.crosstab(
            self.df['education_level'], 
            self.df['financial_standing'], 
            normalize='index'
        ) * 100  # Convert to percentage
        
        # Reindex to maintain education order
        existing_education = [edu for edu in education_order if edu in education_standing.index]
        education_standing = education_standing.reindex(existing_education)
        
        # Get total counts for each education level
        education_counts = self.df['education_level'].value_counts()
        
        # Prepare data for stacked bar chart
        categories = education_standing.index.tolist()
        
        # Financial standing colors (consistent with profession chart)
        colors = {
            'Surplus': '#2ecc71',    # Green
            'Break-even': '#f39c12', # Orange
            'Deficit': '#e74c3c'     # Red
        }
        
        chart_data = {
            'categories': categories,
            'financial_standings': list(education_standing.columns),
            'data': {},
            'colors': colors,
            'total_counts': education_counts.to_dict()
        }
        
        # Add percentage data for each financial standing
        for standing in education_standing.columns:
            if standing in education_standing.columns:
                chart_data['data'][standing] = education_standing[standing].round(1).tolist()
            else:
                chart_data['data'][standing] = [0] * len(categories)
        
        return chart_data
    
    def get_key_metrics(self):
        """
        Calculate key metrics for dashboard summary
        
        Returns:
            dict: Key metrics dictionary
        """
        if self.df is None:
            self.load_data()
        
        income_counts = self.df['avg_income_category'].value_counts()
        expense_counts = self.df['avg_expense_category'].value_counts()
        
        income_pct = (income_counts / income_counts.sum() * 100)
        expense_pct = (expense_counts / expense_counts.sum() * 100)
        
        # Most common categories
        most_common_income = income_counts.idxmax()
        most_common_income_pct = round(income_pct.max(), 1)
        
        most_common_expense = expense_counts.idxmax()
        most_common_expense_pct = round(expense_pct.max(), 1)
        
        # Financial standing breakdown
        financial_standing_dist = self.df['financial_standing'].value_counts().to_dict()
        financial_standing_pct = {}
        for standing, count in financial_standing_dist.items():
            financial_standing_pct[standing] = {
                'count': int(count),
                'percentage': round((count / len(self.df)) * 100, 1)
            }
        
        # Category matching
        same_category = (self.df['avg_income_category'] == self.df['avg_expense_category']).sum()
        same_category_pct = round((same_category / len(self.df)) * 100, 2)
        
        return {
            'most_common_income': most_common_income,
            'most_common_income_pct': most_common_income_pct,
            'most_common_expense': most_common_expense,
            'most_common_expense_pct': most_common_expense_pct,
            'financial_standing': financial_standing_pct,
            'matching_categories': {
                'count': int(same_category),
                'percentage': same_category_pct
            }
        }
    
    def get_loan_overview_data(self):
        """
        Get comprehensive loan overview data
        
        Returns:
            dict: Loan statistics and distribution data
        """
        if self.df is None:
            self.load_data()
        
        loan_processor = LoanProcessor(self.df)
        
        return {
            'statistics': loan_processor.get_loan_statistics(),
            'distribution': loan_processor.get_loan_distribution()
        }
    
    def get_loan_validation_report(self):
        """
        Get loan data validation report
        
        Returns:
            dict: Validation report
        """
        if self.df is None:
            self.load_data()
        
        loan_processor = LoanProcessor(self.df)
        return loan_processor.validate_loan_data()
    
    def get_filtered_loan_overview(self, income_category=None):
        """
        Get loan overview filtered by income category
        
        Args:
            income_category (str): Income category filter
        
        Returns:
            dict: Filtered loan statistics and distribution
        """
        if self.df is None:
            self.load_data()
        
        loan_processor = LoanProcessor(self.df)
        return loan_processor.get_filtered_loan_data_by_income(income_category)
