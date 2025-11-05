"""
Chart Generator Module
Creates visualizations using Plotly
"""
import plotly.graph_objects as go
import json


class ChartGenerator:
    """Generates interactive Plotly charts"""
    
    @staticmethod
    def create_diverging_bar_chart(chart_data):
        """
        Create a Diverging Bar Chart for Income vs Expense comparison
        
        Args:
            chart_data (dict): Dictionary containing chart data with keys:
                - categories: list of category names
                - income_percentages: list of income percentages
                - expense_percentages: list of expense percentages
                - income_counts: list of income counts
                - expense_counts: list of expense counts
        
        Returns:
            str: HTML div containing the Plotly chart
        """
        categories = chart_data['categories']
        income_pct = chart_data['income_percentages']
        expense_pct = chart_data['expense_percentages']
        income_counts = chart_data['income_counts']
        expense_counts = chart_data['expense_counts']
        
        # Create figure
        fig = go.Figure()
        
        # Add Expense bars (negative values for left side)
        fig.add_trace(go.Bar(
            name='Expense',
            y=categories,
            x=[-pct for pct in expense_pct],  # Negative for left side
            orientation='h',
            marker_color='#e74c3c',
            text=[f'{pct:.1f}%' for pct in expense_pct],
            textposition='inside',
            hovertemplate='<b>%{y}</b><br>Expense: %{text}<br>Count: %{customdata}<extra></extra>',
            customdata=expense_counts
        ))
        
        # Add Income bars (positive values for right side)
        fig.add_trace(go.Bar(
            name='Income',
            y=categories,
            x=income_pct,
            orientation='h',
            marker_color='#3498db',
            text=[f'{pct:.1f}%' for pct in income_pct],
            textposition='inside',
            hovertemplate='<b>%{y}</b><br>Income: %{text}<br>Count: %{customdata}<extra></extra>',
            customdata=income_counts
        ))
        
        # Update layout
        fig.update_layout(
            title={
                'text': '⚖️ Income vs Expense: Diverging Comparison',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 24, 'family': 'Arial, sans-serif', 'color': '#2c3e50'}
            },
            barmode='overlay',
            xaxis={
                'title': 'Percentage of Population',
                'tickvals': [-40, -30, -20, -10, 0, 10, 20, 30, 40],
                'ticktext': ['40%', '30%', '20%', '10%', '0%', '10%', '20%', '30%', '40%'],
                'title_font': {'size': 14},
                'tickfont': {'size': 12}
            },
            yaxis={
                'title': 'Financial Category (IDR per month)',
                'title_font': {'size': 14},
                'tickfont': {'size': 12}
            },
            template='plotly_white',
            height=600,
            showlegend=True,
            legend=dict(
                orientation='h',
                y=1.02,
                x=0.5,
                xanchor='center',
                font={'size': 14}
            ),
            plot_bgcolor='rgba(248, 249, 250, 1)',
            paper_bgcolor='white',
            margin=dict(l=100, r=50, t=100, b=80)
        )
        
        # Convert to HTML
        chart_html = fig.to_html(
            include_plotlyjs='cdn',
            div_id='diverging-bar-chart',
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
            }
        )
        
        return chart_html
    
    @staticmethod
    def create_grouped_bar_chart(chart_data):
        """
        Create a Grouped Bar Chart for Income vs Expense comparison
        (Alternative visualization - for future extension)
        
        Args:
            chart_data (dict): Dictionary containing chart data
        
        Returns:
            str: HTML div containing the Plotly chart
        """
        categories = chart_data['categories']
        income_pct = chart_data['income_percentages']
        expense_pct = chart_data['expense_percentages']
        income_counts = chart_data['income_counts']
        expense_counts = chart_data['expense_counts']
        
        fig = go.Figure()
        
        # Add Income bars
        fig.add_trace(go.Bar(
            name='Income Distribution',
            x=categories,
            y=income_pct,
            text=[f'{pct:.1f}%' for pct in income_pct],
            textposition='outside',
            marker_color='#3498db',
            hovertemplate='<b>Income: %{x}</b><br>Percentage: %{y:.1f}%<br>Count: %{customdata}<extra></extra>',
            customdata=income_counts
        ))
        
        # Add Expense bars
        fig.add_trace(go.Bar(
            name='Expense Distribution',
            x=categories,
            y=expense_pct,
            text=[f'{pct:.1f}%' for pct in expense_pct],
            textposition='outside',
            marker_color='#e74c3c',
            hovertemplate='<b>Expense: %{x}</b><br>Percentage: %{y:.1f}%<br>Count: %{customdata}<extra></extra>',
            customdata=expense_counts
        ))
        
        fig.update_layout(
            title={
                'text': '💰 GenZ Income vs Expense Distribution by Category',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 24}
            },
            xaxis={'title': 'Category (IDR per month)'},
            yaxis={'title': 'Percentage of Population (%)'},
            barmode='group',
            template='plotly_white',
            height=600,
            legend=dict(orientation='h', y=1.05, x=0.5, xanchor='center')
        )
        
        chart_html = fig.to_html(
            include_plotlyjs='cdn',
            div_id='grouped-bar-chart',
            config={'displayModeBar': True, 'displaylogo': False}
        )
        
        return chart_html
