// static/js/modules/digital_time_chart.js

/**
 * Renders the digital time spent histogram and KDE chart.
 * @param {object} responseData - The complete data object from the API.
 * @param {string} category - The active filter category.
 */
function renderDigitalTimeChart(responseData, category) {
    const chartDiv = document.getElementById('digital-time-chart');
    if (!chartDiv) {
        console.warn('Digital time chart container not found.');
        return;
    }

    const { filtered_data, baseline_kde } = responseData;
    const { stats, histogram, kde } = filtered_data;

    if (stats.count === 0) {
        chartDiv.innerHTML = `
            <div class="placeholder-content">
                <i class="fas fa-info-circle fa-2x text-muted"></i>
                <h6 class="mt-2">No Digital Engagement Data</h6>
                <small class="text-muted">No users found in this category.</small>
            </div>`;
        return;
    }

    // --- Chart Traces ---

    // 1. Histogram Trace
    const histogramTrace = {
        x: histogram.x.slice(0, -1).map((edge, i) => (edge + histogram.x[i+1]) / 2), // bin centers
        y: histogram.y,
        type: 'bar',
        name: 'Frequency',
        marker: {
            color: 'rgba(52, 152, 219, 0.2)',
            line: {
                color: 'rgba(52, 152, 219, 0.4)',
                width: 1
            }
        },
        hovertemplate: 'Time: %{x:.1f} hrs<br>Count: %{y}<extra></extra>',
    };

    // 2. Filtered KDE Trace (Main Curve)
    const kdeTrace = {
        x: kde.x,
        y: kde.y,
        type: 'scatter',
        mode: 'lines',
        name: 'Smoothed Trend',
        line: {
            color: '#3498db',
            width: 3
        },
        fill: 'tozeroy',
        fillcolor: 'rgba(52, 152, 219, 0.1)',
        hoverinfo: 'none' // Hover is handled by histogram
    };

    // 3. Baseline KDE "Ghost Line" Trace
    const baselineKdeTrace = {
        x: baseline_kde.x,
        y: baseline_kde.y,
        type: 'scatter',
        mode: 'lines',
        name: 'Overall Trend',
        line: {
            color: 'rgba(128, 128, 128, 0.5)',
            width: 2,
            dash: 'dash'
        },
        hoverinfo: 'none',
        visible: (category && category !== 'All') ? true : 'legendonly'
    };

    // --- Layout and Annotations ---
    const titleCategory = category && category !== 'All' ? `for ${category}` : 'Overall';
    const chartTitle = `<b>📱 Digital Time Spent Distribution</b><br><span style="font-size:12px; color:#7f8c8d;">${stats.count} Respondents ${titleCategory}</span>`;

    const layout = {
        title: {
            text: chartTitle,
            x: 0.5,
            xanchor: 'center',
            font: { size: 16, color: '#2c3e50' }
        },
        xaxis: {
            title: 'Digital Time Spent per Day (hours)',
            gridcolor: '#f0f0f0',
            zeroline: false
        },
        yaxis: {
            title: 'Number of Respondents',
            gridcolor: '#f0f0f0',
            zeroline: false
        },
        annotations: [{
            x: stats.mean,
            y: Math.max(...kde.y) * 0.95,
            xref: 'x',
            yref: 'y',
            text: `<b>Avg: ${stats.mean} hrs</b>`,
            showarrow: true,
            arrowhead: 2,
            ax: 0,
            ay: -40,
            font: { color: '#2c3e50', size: 12 },
            bordercolor: '#c7c7c7',
            borderwidth: 1,
            bgcolor: 'rgba(255, 255, 255, 0.8)'
        }],
        barmode: 'overlay',
        showlegend: true,
        legend: { orientation: 'h', y: -0.2, x: 0.5, xanchor: 'center' },
        height: 380,
        margin: { l: 60, r: 30, t: 70, b: 50 },
        template: 'plotly_white'
    };
    
    const config = { displayModeBar: false, responsive: true };

    Plotly.newPlot(chartDiv, [histogramTrace, kdeTrace, baselineKdeTrace], layout, config);
}

/**
 * Fetches and updates the digital time chart for a given category.
 * @param {string|null} category - The income category to filter by.
 */
export function updateDigitalTimeChart(category) {
    console.log('Updating digital time chart for category:', category || 'All');
    const chartDiv = document.getElementById('digital-time-chart');
    if (chartDiv) chartDiv.style.opacity = '0.6';

    const categoryParam = category || 'All';
    const apiUrl = `/api/digital-time/${encodeURIComponent(categoryParam)}`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
            return response.json();
        })
        .then(data => {
            renderDigitalTimeChart(data, category);
            if (chartDiv) chartDiv.style.opacity = '1';
        })
        .catch(error => {
            console.error('Error updating digital time chart:', error);
            if (chartDiv) {
                chartDiv.style.opacity = '1';
                chartDiv.innerHTML = `
                    <div class="placeholder-content text-danger">
                        <i class="fas fa-exclamation-triangle fa-2x"></i>
                        <h6 class="mt-2">Failed to Load Chart</h6>
                        <small>${error.message}</small>
                    </div>`;
            }
        });
}

/**
 * Initializes the chart with data for all categories.
 */
export function initializeDigitalTimeChart() {
    console.log('Initializing digital time chart...');
    updateDigitalTimeChart(null); // 'null' will default to 'All'
}