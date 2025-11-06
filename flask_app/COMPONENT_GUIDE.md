# 🧩 Component Usage Guide

**Quick Reference for Using Dashboard Components Independently**

---

## 📖 Table of Contents

1. [Visual Analytics Panel](#visual-analytics-panel)
2. [Loan Overview Panel](#loan-overview-panel)
3. [Summary Cards](#summary-cards)
4. [Financial Standing](#financial-standing)
5. [Insights Section](#insights-section)
6. [Cross-Component Communication](#cross-component-communication)

---

## 🎨 Visual Analytics Panel

### Overview
The main 60/20/20 layout showing:
- **60%**: Diverging bar chart (Income vs Expense)
- **20%**: Profession breakdown
- **20%**: Education breakdown

### Files Required
```
templates/components/visual_analytics.html
static/css/dashboard.css
utils/data_loader.py
utils/chart_generator.py
```

### Backend Setup

```python
from flask import render_template
from utils.data_loader import DataLoader
from utils.chart_generator import ChartGenerator

@app.route('/my-analytics')
def my_analytics():
    # Initialize data loader
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    # Get chart data
    chart_data = data_loader.get_chart_data()
    profession_data = data_loader.get_profession_chart_data()
    education_data = data_loader.get_education_chart_data()
    
    # Generate charts
    chart_html = ChartGenerator.create_diverging_bar_chart(chart_data)
    profession_chart = ChartGenerator.create_profession_chart(profession_data)
    education_chart = ChartGenerator.create_education_chart(education_data)
    
    return render_template('my_template.html',
        chart_html=chart_html,
        profession_chart=profession_chart,
        education_chart=education_chart
    )
```

### Frontend Template

```html
{% extends "base.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
{% endblock %}

{% block content %}
<div class="container-fluid">
    <h2>My Analytics Dashboard</h2>
    
    <!-- Include the visual analytics component -->
    {% include 'components/visual_analytics.html' %}
</div>
{% endblock %}
```

### Events Dispatched

```javascript
// When user clicks a category bar
document.addEventListener('categoryFiltered', function(e) {
    const category = e.detail.category;
    console.log('Category selected:', category);
    // Your custom logic here
});

// When user clears the filter
document.addEventListener('categoryFilterReset', function(e) {
    console.log('Filter cleared');
    // Your custom logic here
});
```

### Customization Options

**Change colors**:
```python
# In utils/chart_generator.py
COLORS = {
    'income': '#your_color',
    'expense': '#your_color'
}
```

**Adjust layout**:
```css
/* In static/css/dashboard.css */
.viz-main {
    flex: 0 0 70%; /* Change from 60% to 70% */
}
.viz-side {
    flex: 0 0 15%; /* Change from 20% to 15% */
}
```

---

## 💳 Loan Overview Panel

### Overview
Displays loan statistics with:
- 4 KPI cards (Total, Average, Total Outstanding, Maximum)
- Interactive donut chart
- Real-time filtering

### Files Required
```
templates/components/loan_overview.html
static/css/loan_panel.css
static/js/modules/loan_panel.js
routes/api.py (for /api/loan-filtered/<category>)
utils/data_loader.py
```

### Backend Setup

#### 1. Page Route
```python
from flask import render_template
from utils.data_loader import DataLoader

@app.route('/my-loans')
def my_loans():
    # Load data
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    # Get loan statistics
    loan_overview = data_loader.get_loan_overview_data()
    loan_stats = loan_overview['statistics']
    
    return render_template('my_template.html', loan_stats=loan_stats)
```

#### 2. API Endpoint (REQUIRED for dynamic updates)
```python
from flask import Blueprint, jsonify
import urllib.parse

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/loan-filtered/<category>')
def api_loan_filtered(category):
    decoded_category = urllib.parse.unquote(category)
    
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    filtered_data = data_loader.get_filtered_loan_overview(decoded_category)
    return jsonify(filtered_data)

# Register blueprint in app.py
app.register_blueprint(api_bp)
```

### Frontend Template

```html
{% extends "base.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/loan_panel.css') }}">
{% endblock %}

{% block content %}
<div class="container-fluid">
    <h2>Loan Overview</h2>
    
    <!-- Include the loan overview component -->
    {% include 'components/loan_overview.html' %}
</div>
{% endblock %}

{% block extra_js %}
<!-- Load Plotly (required for donut chart) -->
<script src="https://cdn.plotly.ly/plotly-latest.min.js"></script>

<!-- Load loan panel module -->
<script type="module">
    import { initializeLoanChart } from '{{ url_for('static', filename='js/modules/loan_panel.js') }}';
    
    document.addEventListener('DOMContentLoaded', function() {
        initializeLoanChart();
    });
</script>
{% endblock %}
```

### Standalone Usage (No Filtering)

If you don't need category filtering:

```javascript
// Simplified initialization
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/loan-filtered/All')
        .then(response => response.json())
        .then(data => {
            // Render chart (reuse the renderLoanChart function from loan_panel.js)
            // Or copy just the chart rendering code
        });
});
```

### Manual Filtering

```javascript
import { updateLoanPanel } from '/static/js/modules/loan_panel.js';

// Update to specific category
updateLoanPanel('4-6jt');

// Reset to all
updateLoanPanel(null);
```

### Customization Options

**Change KPI card colors**:
```css
/* In static/css/loan_panel.css */
.loan-kpi-card.primary { border-color: #your_color; }
.loan-kpi-card.success { border-color: #your_color; }
.loan-kpi-card.warning { border-color: #your_color; }
.loan-kpi-card.danger { border-color: #your_color; }
```

**Change donut chart colors**:
```python
# In utils/loan_processor.py
LOAN_CATEGORY_COLORS = {
    'No Loan': '#your_color',
    'Small': '#your_color',
    'Medium': '#your_color',
    'Large': '#your_color'
}
```

---

## 📊 Summary Cards

### Overview
4 KPI cards showing:
- Total Records
- Top Income Category
- Top Expense Category
- Matching Categories

### Files Required
```
templates/components/summary_cards.html
```

### Backend Setup

```python
from utils.data_loader import DataLoader

@app.route('/my-summary')
def my_summary():
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    stats = data_loader.get_dataset_stats()
    metrics = data_loader.get_key_metrics()
    
    return render_template('my_template.html',
        stats=stats,
        metrics=metrics
    )
```

### Frontend Template

```html
{% include 'components/summary_cards.html' %}
```

### Expected Data Structure

```python
stats = {
    'total_rows': 1000
}

metrics = {
    'most_common_income': '4-6jt',
    'most_common_income_pct': 25.5,
    'most_common_expense': '2-4jt',
    'most_common_expense_pct': 30.2,
    'matching_categories': {
        'percentage': 45.8
    }
}
```

### Customization

**Change card colors**:
```html
<!-- In templates/components/summary_cards.html -->
<!-- Change bg-primary, bg-success, bg-danger, bg-info to your preferred Bootstrap colors -->
```

---

## 📈 Financial Standing

### Overview
Breakdown of:
- Surplus (green)
- Deficit (red)
- Break-even (yellow)

### Files Required
```
templates/components/financial_standing.html
```

### Backend Setup

```python
from utils.data_loader import DataLoader

@app.route('/financial-standing')
def financial_standing():
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    metrics = data_loader.get_key_metrics()
    
    return render_template('my_template.html', metrics=metrics)
```

### Frontend Template

```html
{% include 'components/financial_standing.html' %}
```

### Expected Data Structure

```python
metrics = {
    'financial_standing': {
        'Surplus': {
            'count': 450,
            'percentage': 45.0
        },
        'Deficit': {
            'count': 350,
            'percentage': 35.0
        },
        'Break-even': {
            'count': 200,
            'percentage': 20.0
        }
    }
}
```

---

## 💡 Insights Section

### Overview
- Active filter indicator
- 3 insight cards with bullet points
- Clear filter button

### Files Required
```
templates/components/insights.html
```

### Backend Setup

```python
from utils.data_loader import DataLoader

@app.route('/insights')
def insights():
    data_loader = DataLoader('data/your_data.csv')
    data_loader.load_data()
    
    metrics = data_loader.get_key_metrics()
    
    return render_template('my_template.html', metrics=metrics)
```

### Frontend Template

```html
{% include 'components/insights.html' %}

<!-- If using filter functionality -->
<script>
window.resetCategoryFilter = function() {
    // Your reset logic
    document.dispatchEvent(new CustomEvent('categoryFilterReset', { bubbles: true }));
};
</script>
```

### Filter Status Control

```javascript
// Show filter status
const statusDiv = document.getElementById('filter-status');
const categorySpan = document.getElementById('filter-category');

categorySpan.textContent = 'Your Category';
statusDiv.style.display = 'block';

// Hide filter status
statusDiv.style.display = 'none';
```

---

## 🔗 Cross-Component Communication

### Use Case: Link Visual Analytics with Loan Panel

When a user clicks a category in the main chart, automatically filter the loan panel.

### Full Setup

#### 1. Include Both Components
```html
{% extends "base.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/loan_panel.css') }}">
{% endblock %}

{% block content %}
<div class="container-fluid">
    <!-- Visual Analytics -->
    {% include 'components/visual_analytics.html' %}
    
    <!-- Loan Overview -->
    {% include 'components/loan_overview.html' %}
    
    <!-- Insights (shows active filter) -->
    {% include 'components/insights.html' %}
</div>
{% endblock %}

{% block extra_js %}
<script src="https://cdn.plotly.ly/plotly-latest.min.js"></script>
<script type="module" src="{{ url_for('static', filename='js/main.js') }}"></script>
{% endblock %}
```

#### 2. The Orchestrator (`main.js`) Handles Communication

The `static/js/main.js` file automatically:
- Listens for `categoryFiltered` events from the chart
- Calls `updateLoanPanel(category)` to filter loan data
- Shows the filter status indicator
- Handles reset events

#### 3. Event Flow

```
User clicks category bar
  ↓
Chart dispatches 'categoryFiltered' event
  ↓
main.js receives event
  ↓
main.js calls updateLoanPanel(category)
  ↓
Loan panel fetches filtered data from API
  ↓
Loan chart and KPIs update
  ↓
Filter status indicator appears
```

### Custom Event Handling

If you want to add your own logic:

```javascript
// In your custom script
document.addEventListener('categoryFiltered', function(e) {
    const category = e.detail.category;
    
    // Your custom logic
    console.log('Category changed to:', category);
    
    // Example: Update another chart
    updateMyCustomChart(category);
    
    // Example: Send analytics
    gtag('event', 'category_filter', { 'category': category });
});
```

### Dispatching Events from Your Code

```javascript
// Trigger a category filter programmatically
const event = new CustomEvent('categoryFiltered', {
    bubbles: true,
    detail: { category: '4-6jt' }
});
document.dispatchEvent(event);

// Trigger a reset programmatically
const resetEvent = new CustomEvent('categoryFilterReset', { bubbles: true });
document.dispatchEvent(resetEvent);
```

---

## 🎯 Quick Integration Recipes

### Recipe 1: Minimal Loan Panel Only

**Scenario**: You only need the loan donut chart

```python
# route
@app.route('/loans')
def loans():
    data_loader = DataLoader('data.csv')
    data_loader.load_data()
    loan_stats = data_loader.get_loan_overview_data()['statistics']
    return render_template('loans.html', loan_stats=loan_stats)
```

```html
<!-- loans.html -->
{% extends "base.html" %}
{% block content %}
    {% include 'components/loan_overview.html' %}
{% endblock %}
{% block extra_css %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/loan_panel.css') }}">
{% endblock %}
{% block extra_js %}
    <script src="https://cdn.plotly.ly/plotly-latest.min.js"></script>
    <script type="module">
        import { initializeLoanChart } from '{{ url_for('static', filename='js/modules/loan_panel.js') }}';
        document.addEventListener('DOMContentLoaded', initializeLoanChart);
    </script>
{% endblock %}
```

### Recipe 2: Visual Analytics Only

**Scenario**: You only need the 60/20/20 chart layout

```python
# route
@app.route('/analytics')
def analytics():
    data_loader = DataLoader('data.csv')
    data_loader.load_data()
    
    chart_html = ChartGenerator.create_diverging_bar_chart(data_loader.get_chart_data())
    profession_chart = ChartGenerator.create_profession_chart(data_loader.get_profession_chart_data())
    education_chart = ChartGenerator.create_education_chart(data_loader.get_education_chart_data())
    
    return render_template('analytics.html',
        chart_html=chart_html,
        profession_chart=profession_chart,
        education_chart=education_chart
    )
```

```html
<!-- analytics.html -->
{% extends "base.html" %}
{% block content %}
    {% include 'components/visual_analytics.html' %}
{% endblock %}
{% block extra_css %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
{% endblock %}
```

### Recipe 3: Full Dashboard with Filtering

**Scenario**: Complete dashboard with all components communicating

```python
# route
@app.route('/full-dashboard')
def full_dashboard():
    data_loader = DataLoader('data.csv')
    data_loader.load_data()
    
    # All data
    stats = data_loader.get_dataset_stats()
    metrics = data_loader.get_key_metrics()
    chart_html = ChartGenerator.create_diverging_bar_chart(data_loader.get_chart_data())
    profession_chart = ChartGenerator.create_profession_chart(data_loader.get_profession_chart_data())
    education_chart = ChartGenerator.create_education_chart(data_loader.get_education_chart_data())
    loan_stats = data_loader.get_loan_overview_data()['statistics']
    
    return render_template('full_dashboard.html',
        stats=stats,
        metrics=metrics,
        chart_html=chart_html,
        profession_chart=profession_chart,
        education_chart=education_chart,
        loan_stats=loan_stats
    )
```

```html
<!-- full_dashboard.html -->
{% extends "base.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/loan_panel.css') }}">
{% endblock %}

{% block content %}
<div class="container-fluid">
    {% include 'components/summary_cards.html' %}
    {% include 'components/financial_standing.html' %}
    {% include 'components/visual_analytics.html' %}
    {% include 'components/loan_overview.html' %}
    {% include 'components/insights.html' %}
</div>
{% endblock %}

{% block extra_js %}
<script src="https://cdn.plotly.ly/plotly-latest.min.js"></script>
<script type="module" src="{{ url_for('static', filename='js/main.js') }}"></script>
{% endblock %}
```

---

## 🔧 Troubleshooting

### Chart not displaying
- ✅ Check if Plotly CDN is loaded: `<script src="https://cdn.plotly.ly/plotly-latest.min.js"></script>`
- ✅ Check browser console for errors
- ✅ Ensure chart data is not empty

### Loan panel not updating
- ✅ Verify API endpoint `/api/loan-filtered/<category>` is registered
- ✅ Check Network tab in browser DevTools
- ✅ Ensure `loan_panel.js` is loaded as ES6 module (`type="module"`)

### CSS not applying
- ✅ Check if CSS file is linked correctly
- ✅ Clear browser cache (Ctrl+Shift+R)
- ✅ Check for CSS conflicts with existing styles

### Events not firing
- ✅ Ensure `main.js` is loaded
- ✅ Check that event listeners are added after DOM is loaded
- ✅ Use `addEventListener` instead of inline `onclick` for custom events

---

## 📚 Additional Resources

- **Main Codebase Review**: See `CODEBASE_REVIEW.md`
- **Project README**: See `README.md`
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Plotly Documentation**: https://plotly.com/python/

---

**Document Version**: 1.0  
**Last Updated**: November 6, 2025
