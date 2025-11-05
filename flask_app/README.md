# 📊 GenZ Financial Dashboard - Flask Web Application

A Flask-based interactive web dashboard for analyzing GenZ financial behavior, income patterns, and spending habits. This application visualizes the relationship between income and expense categories using an interactive Diverging Bar Chart.

![Dashboard Preview](https://img.shields.io/badge/Flask-3.0-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![Plotly](https://img.shields.io/badge/Plotly-5.18-orange)

## 🎯 Features

- **Interactive Visualization**: Diverging Bar Chart showing Income vs Expense comparison
- **Dataset Statistics**: Comprehensive overview of data quality and distribution
- **Key Metrics Dashboard**: Quick insights into financial patterns
- **Financial Standing Analysis**: Breakdown of Surplus, Deficit, and Break-even categories
- **RESTful API**: JSON endpoints for programmatic data access
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
- **Extensible Architecture**: Clean code structure for easy additions

## 📁 Project Structure

```
flask_app/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/
│   └── dataset_gelarrasa_genzfinancialprofile.csv
├── utils/
│   ├── __init__.py
│   ├── data_loader.py     # Data processing module
│   └── chart_generator.py # Visualization module
├── templates/
│   ├── base.html          # Base template
│   ├── dashboard.html     # Main dashboard
│   ├── about.html         # About page
│   └── error.html         # Error page
└── static/
    └── css/
        └── style.css      # Custom styles
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation Steps

#### 1. Navigate to the Flask App Directory

```powershell
cd flask_app
```

#### 2. Create a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

#### 4. Verify Data File

Ensure the CSV file exists:
```
data/dataset_gelarrasa_genzfinancialprofile.csv
```

#### 5. Run the Application

```powershell
python app.py
```

#### 6. Access the Dashboard

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📊 Available Routes

| Route | Description |
|-------|-------------|
| `/` or `/dashboard` | Main dashboard with visualization |
| `/about` | Project information and documentation |
| `/api/stats` | JSON API - Dataset statistics |
| `/api/metrics` | JSON API - Key metrics |
| `/api/chart-data` | JSON API - Chart data |

## 🔧 Configuration

### Changing Port or Host

Edit `app.py` at the bottom:

```python
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
```

### Debug Mode

- **Development**: Keep `debug=True` for auto-reload and detailed error messages
- **Production**: Set `debug=False` for security

## 📈 Understanding the Visualization

### Diverging Bar Chart

The main visualization shows income vs expense distribution:

- **Blue bars (right side)**: Income distribution by category
- **Red bars (left side)**: Expense distribution by category
- **Bar length**: Percentage of population in each category
- **Hover**: Shows exact counts and percentages

### Interpretation

- **Symmetry**: Balanced income and expense patterns
- **Longer expense bars**: More people spending in that range
- **Longer income bars**: More people earning in that range
- **Diagonal pattern**: People spending within their means

## 🔌 API Usage Examples

### Get Dataset Statistics

```bash
curl http://127.0.0.1:5000/api/stats
```

### Get Key Metrics

```bash
curl http://127.0.0.1:5000/api/metrics
```

### Get Chart Data

```bash
curl http://127.0.0.1:5000/api/chart-data
```

## 🛠 Technology Stack

### Backend
- **Flask 3.0**: Web framework
- **Pandas 2.1**: Data manipulation
- **Plotly 5.18**: Interactive visualizations
- **NumPy 1.26**: Numerical operations

### Frontend
- **Bootstrap 5.3**: Responsive UI framework
- **Font Awesome 6.4**: Icons
- **Plotly.js**: Chart rendering

## 📝 Dataset Information

### Required Columns

The CSV file must contain these columns:

- `avg_monthly_income`: Average monthly income (numerical)
- `avg_income_category`: Income category (e.g., <2jt, 2-4jt, etc.)
- `avg_monthly_expense`: Average monthly expense (numerical)
- `avg_expense_category`: Expense category (e.g., <2jt, 2-4jt, etc.)
- `financial_standing`: Financial status (Surplus, Deficit, Break-even)

### Category Order

Categories are displayed in this order:
```
N/A, <2jt, 2-4jt, 4-6jt, 6-10jt, 10-15jt, >15jt
```

## 🔮 Future Extensions

### Planned Features

1. **Dynamic Filters**
   - Filter by province, age, gender
   - Date range selection
   - Employment status filter

2. **Additional Visualizations**
   - Sankey diagram (flow visualization)
   - Heatmap (cross-category analysis)
   - Treemap (hierarchical view)
   - Grouped bar chart (side-by-side comparison)

3. **Export Functionality**
   - Download charts as PNG/PDF
   - Export filtered data as CSV
   - Generate PDF reports

4. **User Features**
   - Save custom views
   - Bookmark favorite filters
   - Share dashboard links

### How to Extend

#### Adding a New Chart

1. Add chart method to `utils/chart_generator.py`:

```python
@staticmethod
def create_new_chart(data):
    # Your chart code here
    return chart_html
```

2. Add route in `app.py`:

```python
@app.route('/new-chart')
def new_chart():
    chart_html = ChartGenerator.create_new_chart(data)
    return render_template('new_chart.html', chart_html=chart_html)
```

3. Create template in `templates/new_chart.html`

#### Adding Filters

Modify `utils/data_loader.py` to accept filter parameters:

```python
def get_filtered_data(self, province=None, age_min=None, age_max=None):
    filtered_df = self.df.copy()
    if province:
        filtered_df = filtered_df[filtered_df['province'] == province]
    # Add more filters...
    return filtered_df
```

## 🐛 Troubleshooting

### Common Issues

#### 1. CSV File Not Found

**Error**: `FileNotFoundError: CSV file not found`

**Solution**: Ensure the CSV file is in the `data/` folder:
```powershell
ls data\dataset_gelarrasa_genzfinancialprofile.csv
```

#### 2. Import Errors

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**: Activate virtual environment and install dependencies:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 3. Port Already in Use

**Error**: `Address already in use`

**Solution**: Change port in `app.py` or kill the process:
```powershell
# Find process using port 5000
netstat -ano | findstr :5000
# Kill the process
taskkill /PID <process_id> /F
```

#### 4. Charts Not Displaying

**Solution**:
- Check browser console for JavaScript errors
- Ensure internet connection (Plotly CDN required)
- Clear browser cache

## 📚 Development

### Running in Development Mode

```powershell
# Enable Flask debug mode
$env:FLASK_ENV = "development"
python app.py
```

### Code Style

This project follows PEP 8 guidelines. Format code using:

```powershell
pip install black
black .
```

### Testing

Add tests in a `tests/` folder:

```python
# tests/test_data_loader.py
import unittest
from utils.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = DataLoader('data/dataset_gelarrasa_genzfinancialprofile.csv')
        df = loader.load_data()
        self.assertIsNotNone(df)
```

Run tests:
```powershell
python -m unittest discover tests
```

## 📄 License

This project is created for educational and competition purposes.

## 🤝 Contributing

To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues or questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the [API Documentation](#-api-usage-examples)
3. Check Flask documentation: https://flask.palletsprojects.com/

## ✅ Checklist for Deployment

- [ ] Set `debug=False` in `app.py`
- [ ] Change `SECRET_KEY` to a random string
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Set up proper logging
- [ ] Configure environment variables
- [ ] Use a reverse proxy (Nginx, Apache)
- [ ] Enable HTTPS
- [ ] Set up monitoring and error tracking

## 🎉 Acknowledgments

- Original Jupyter Notebook analysis
- Flask documentation and community
- Plotly for amazing visualization library
- Bootstrap team for responsive framework

---

**Built with ❤️ for the Dashboard Analysis Competition**

**Version**: 1.0.0  
**Last Updated**: November 2025
