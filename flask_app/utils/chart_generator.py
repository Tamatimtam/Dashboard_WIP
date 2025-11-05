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
        Create an enhanced Diverging Bar Chart for Income vs Expense comparison
        
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
        
        # Create figure
        fig = go.Figure()
        
        # Add Expense bars (negative values for left side) - Enhanced styling
        fig.add_trace(go.Bar(
            name='Expense',
            y=categories,
            x=[-pct for pct in expense_pct],
            orientation='h',
            marker=dict(
                color='#e74c3c',
                line=dict(color='#c0392b', width=1.5),
                opacity=0.9
            ),
            text=[f'{pct:.1f}%' for pct in expense_pct],
            textposition='inside',
            textfont=dict(size=11, color='white', family='Arial, sans-serif'),
            hovertemplate='<b>%{y}</b><br>Expense: %{text}<br>Count: %{customdata}<br><extra></extra>',
            customdata=expense_counts
        ))
        
        # Add Income bars (positive values for right side) - Enhanced styling
        fig.add_trace(go.Bar(
            name='Income',
            y=categories,
            x=income_pct,
            orientation='h',
            marker=dict(
                color='#3498db',
                line=dict(color='#2980b9', width=1.5),
                opacity=0.9
            ),
            text=[f'{pct:.1f}%' for pct in income_pct],
            textposition='inside',
            textfont=dict(size=11, color='white', family='Arial, sans-serif'),
            hovertemplate='<b>%{y}</b><br>Income: %{text}<br>Count: %{customdata}<br><extra></extra>',
            customdata=income_counts
        ))
        
        # Enhanced layout
        fig.update_layout(
            title={
                'text': '<b>⚖️ Income vs Expense Distribution</b>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18, 'family': 'Arial, sans-serif', 'color': '#2c3e50'}
            },
            barmode='overlay',
            xaxis={
                'title': '<b>Percentage of Population</b>',
                'tickvals': [-40, -30, -20, -10, 0, 10, 20, 30, 40],
                'ticktext': ['40%', '30%', '20%', '10%', '0%', '10%', '20%', '30%', '40%'],
                'title_font': {'size': 13, 'color': '#34495e'},
                'tickfont': {'size': 11, 'color': '#34495e'},
                'gridcolor': 'rgba(189, 195, 199, 0.3)',
                'zeroline': True,
                'zerolinewidth': 2,
                'zerolinecolor': '#95a5a6'
            },
            yaxis={
                'title': '<b>Financial Category (IDR/month)</b>',
                'title_font': {'size': 13, 'color': '#34495e'},
                'tickfont': {'size': 11, 'color': '#34495e'},
                'gridcolor': 'rgba(189, 195, 199, 0.2)'
            },
            template='plotly_white',
            height=480,
            autosize=True,
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5,
                font={'size': 12, 'color': '#2c3e50'},
                bgcolor='rgba(255, 255, 255, 0.9)',
                bordercolor='#bdc3c7',
                borderwidth=1
            ),
            plot_bgcolor='rgba(250, 250, 250, 1)',
            paper_bgcolor='white',
            margin=dict(l=140, r=30, t=80, b=60),
            hoverlabel=dict(
                bgcolor='white',
                font_size=12,
                font_family='Arial, sans-serif'
            )
        )
        
        # Convert to HTML
        chart_html = fig.to_html(
            include_plotlyjs='cdn',
            div_id='diverging-bar-chart',
            config={
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
        )
        
        return chart_html
    
    @staticmethod
    def create_profession_chart(profession_data):
        """
        Create a stacked bar chart for Profession vs Financial Standing
        
        Args:
            profession_data (dict): Dictionary containing profession data with financial standing
        
        Returns:
            str: HTML div containing the Plotly chart
        """
        fig = go.Figure()
        
        categories = profession_data['categories']
        colors = profession_data['colors']
        
        # Add bars for each financial standing (stacked)
        for standing in ['Surplus', 'Break-even', 'Deficit']:
            if standing in profession_data['data']:
                values = profession_data['data'][standing]
                
                # Create hover text with actual counts
                hover_text = []
                for i, cat in enumerate(categories):
                    count = profession_data['total_counts'].get(cat, 0)
                    pct = values[i]
                    actual_count = int((pct / 100) * count)
                    hover_text.append(f"{cat}<br>{standing}: {pct:.1f}% ({actual_count} people)")
                
                fig.add_trace(go.Bar(
                    name=standing,
                    x=categories,
                    y=values,
                    marker=dict(
                        color=colors.get(standing, '#95a5a6'),
                        line=dict(color='rgba(255,255,255,0.5)', width=1)
                    ),
                    hovertext=hover_text,
                    hoverinfo='text',
                    text=[f'{v:.0f}%' if v > 8 else '' for v in values],
                    textposition='inside',
                    textfont=dict(size=9, color='white')
                ))
        
        fig.update_layout(
            title={
                'text': '<b>👔 Employment vs Financial Standing</b>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 14, 'color': '#2c3e50'}
            },
            xaxis={
                'tickfont': {'size': 8, 'color': '#34495e'},
                'showgrid': False,
                'tickangle': -45
            },
            yaxis={
                'title': '<b>%</b>',
                'title_font': {'size': 10, 'color': '#34495e'},
                'tickfont': {'size': 8, 'color': '#34495e'},
                'gridcolor': 'rgba(189, 195, 199, 0.2)',
                'range': [0, 100]
            },
            barmode='stack',
            template='plotly_white',
            height=480,
            autosize=True,
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=-0.35,
                xanchor='center',
                x=0.5,
                font={'size': 9}
            ),
            plot_bgcolor='rgba(250, 250, 250, 1)',
            paper_bgcolor='white',
            margin=dict(l=35, r=15, t=60, b=110),
            hoverlabel=dict(bgcolor='white', font_size=10)
        )
        
        chart_html = fig.to_html(
            include_plotlyjs=False,
            div_id='profession-chart',
            config={'displayModeBar': False, 'responsive': True}
        )
        
        return chart_html
    
    @staticmethod
    def create_education_chart(education_data):
        """
        Create a stacked bar chart for Education Level vs Financial Standing
        
        Args:
            education_data (dict): Dictionary containing education data with financial standing
        
        Returns:
            str: HTML div containing the Plotly chart
        """
        fig = go.Figure()
        
        categories = education_data['categories']
        colors = education_data['colors']
        
        # Abbreviate long category names for better display
        abbreviated_cats = []
        for cat in categories:
            if len(cat) > 15:
                if 'Bachelor' in cat:
                    abbreviated_cats.append('Bachelor/D4')
                elif 'Diploma I' in cat:
                    abbreviated_cats.append('Diploma I-III')
                elif 'Senior High' in cat:
                    abbreviated_cats.append('High School')
                elif 'Junior High' in cat:
                    abbreviated_cats.append('Junior High')
                elif 'Elementary' in cat:
                    abbreviated_cats.append('Elementary')
                elif 'Postgraduate' in cat:
                    abbreviated_cats.append('Postgrad')
                else:
                    abbreviated_cats.append(cat[:15])
            else:
                abbreviated_cats.append(cat)
        
        # Add bars for each financial standing (stacked)
        for standing in ['Surplus', 'Break-even', 'Deficit']:
            if standing in education_data['data']:
                values = education_data['data'][standing]
                
                # Create hover text with actual counts
                hover_text = []
                for i, cat in enumerate(categories):
                    count = education_data['total_counts'].get(cat, 0)
                    pct = values[i]
                    actual_count = int((pct / 100) * count)
                    hover_text.append(f"{cat}<br>{standing}: {pct:.1f}% ({actual_count} people)")
                
                fig.add_trace(go.Bar(
                    name=standing,
                    x=abbreviated_cats,
                    y=values,
                    marker=dict(
                        color=colors.get(standing, '#95a5a6'),
                        line=dict(color='rgba(255,255,255,0.5)', width=1)
                    ),
                    hovertext=hover_text,
                    hoverinfo='text',
                    text=[f'{v:.0f}%' if v > 8 else '' for v in values],
                    textposition='inside',
                    textfont=dict(size=9, color='white')
                ))
        
        fig.update_layout(
            title={
                'text': '<b>🎓 Education vs Financial Standing</b>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 14, 'color': '#2c3e50'}
            },
            xaxis={
                'tickfont': {'size': 8, 'color': '#34495e'},
                'showgrid': False,
                'tickangle': -45
            },
            yaxis={
                'title': '<b>%</b>',
                'title_font': {'size': 10, 'color': '#34495e'},
                'tickfont': {'size': 8, 'color': '#34495e'},
                'gridcolor': 'rgba(189, 195, 199, 0.2)',
                'range': [0, 100]
            },
            barmode='stack',
            template='plotly_white',
            height=480,
            autosize=True,
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=-0.35,
                xanchor='center',
                x=0.5,
                font={'size': 9}
            ),
            plot_bgcolor='rgba(250, 250, 250, 1)',
            paper_bgcolor='white',
            margin=dict(l=35, r=15, t=60, b=110),
            hoverlabel=dict(bgcolor='white', font_size=10)
        )
        
        chart_html = fig.to_html(
            include_plotlyjs=False,
            div_id='education-chart',
            config={'displayModeBar': False, 'responsive': True}
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
