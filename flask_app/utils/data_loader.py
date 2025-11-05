"""
Data Loader Module
Handles CSV loading, preprocessing, and statistics calculation
"""
import pandas as pd
import os


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
        Prepare placeholder data for Profession/Employment Status chart
        
        Returns:
            dict: Dictionary containing profession data
        """
        # Placeholder data - replace with actual column when available
        profession_data = {
            'categories': ['Student', 'Employed', 'Freelance', 'Entrepreneur', 'Unemployed'],
            'values': [35, 28, 18, 12, 7],
            'colors': ['#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#e74c3c']
        }
        return profession_data
    
    def get_education_chart_data(self):
        """
        Prepare placeholder data for Education Level chart
        
        Returns:
            dict: Dictionary containing education data
        """
        # Placeholder data - replace with actual column when available
        education_data = {
            'categories': ['High School', 'Bachelor', 'Master', 'Diploma', 'Doctorate'],
            'values': [22, 45, 18, 10, 5],
            'colors': ['#1abc9c', '#3498db', '#9b59b6', '#f39c12', '#e74c3c']
        }
        return education_data
    
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
