// static/js/modules/loan_panel.js

/**
 * Formats a number as currency in Rupiah (Rp).
 * @param {number} amount - The amount to format.
 * @returns {string} - The formatted currency string.
 */
function formatCurrency(amount) {
    if (!amount || amount === 0) return 'Rp 0';
    
    if (amount >= 1000000000) {
        return `Rp ${(amount / 1000000000).toFixed(1)}B`;
    } else if (amount >= 1000000) {
        return `Rp ${(amount / 1000000).toFixed(1)}M`;
    } else if (amount >= 1000) {
        return `Rp ${(amount / 1000).toFixed(1)}K`;
    } else {
        return `Rp ${amount.toFixed(0)}`;
    }
}

/**
 * Safely updates the text content of a KPI card element.
 * @param {string} elementId - The ID of the element to update.
 * @param {string|number} value - The new value.
 */
function updateKPICard(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = value;
    } else {
        console.warn(`Element not found: ${elementId}`);
    }
}

/**
 * Renders the loan distribution donut chart using Plotly.
 * @param {object} data - The data for the chart, including distribution and filter info.
 */
function renderLoanChart(data) {
    const chartDiv = document.getElementById('loan-overview-chart');
    if (!chartDiv) {
        console.warn('Loan overview chart container not found');
        return;
    }
    
    const distribution = data.distribution || [];
    const categories = distribution.map(d => d.category);
    const percentages = distribution.map(d => d.percentage);
    const counts = distribution.map(d => d.count);
    const colors = distribution.map(d => d.color);
    
    // Calculate total with loans from distribution (excluding 'No Loan')
    const totalWithLoans = distribution
        .filter(d => d.category !== 'No Loan')
        .reduce((sum, d) => sum + d.count, 0);
    
    // Dynamic title based on filter
    const filterText = data.filter_applied && data.filter_applied !== 'All'
        ? ` (${totalWithLoans} borrowers in ${data.filter_applied})`
        : ` (${totalWithLoans} borrowers)`;
    
    const centerText = data.filter_applied && data.filter_applied !== 'All'
        ? `<b style="font-size:22px">${data.with_loan}</b><br><span style='font-size:12px;color:#7f8c8d'>with loans</span><br><span style='font-size:10px;color:#95a5a6'>in ${data.filter_applied}</span>`
        : `<b style="font-size:22px">${data.with_loan}</b><br><span style='font-size:12px;color:#7f8c8d'>with loans</span>`;
    
    const chartData = [{
        labels: categories,
        values: percentages,
        hole: 0.60,
        type: 'pie',
        marker: {
            colors: colors,
            line: { color: '#ffffff', width: 2 }
        },
        textposition: 'outside',
        textfont: { size: 11, color: '#2c3e50', family: 'Arial, sans-serif' },
        hovertemplate: '<b>%{label}</b><br>%{value:.1f}% (%{customdata} people)<extra></extra>',
        customdata: counts,
        direction: 'clockwise',
        sort: false
    }];
    
    const layout = {
        title: {
            text: `<b>💳 Outstanding Loan Distribution${filterText}</b>`,
            x: 0.5,
            xanchor: 'center',
            font: { size: 16, color: '#2c3e50', family: 'Arial, sans-serif' }
        },
        annotations: [{
            text: centerText,
            x: 0.5,
            y: 0.5,
            font: { size: 16, color: '#2c3e50', family: 'Arial, sans-serif' },
            showarrow: false
        }],
        showlegend: true,
        legend: {
            orientation: 'v',
            yanchor: 'middle',
            y: 0.5,
            xanchor: 'left',
            x: 1.05,
            font: { size: 10, color: '#2c3e50' },
            bgcolor: 'rgba(255, 255, 255, 0.9)',
            bordercolor: '#dee2e6',
            borderwidth: 1
        },
        margin: { l: 40, r: 140, t: 60, b: 40 },
        paper_bgcolor: 'white',
        height: 340,
        template: 'plotly_white'
    };
    
    const config = { displayModeBar: false, responsive: true };
    
    Plotly.newPlot(chartDiv, chartData, layout, config);
}

/**
 * Renders the combined pie and bar chart for loan usage purposes.
 * @param {Array} data - Array of loan purpose objects from the API.
 * @param {string|null} category - The active filter category for the title.
 */
function renderLoanPurposeChart(data, category) {
    const chartDiv = document.getElementById('loan-purpose-chart');
    if (!chartDiv) {
        console.warn('Loan purpose chart container not found.');
        return;
    }

    // Clear previous content and handle no-data state
    if (!data || data.length === 0) {
        chartDiv.innerHTML = `
            <div class="placeholder-content" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 340px;">
                <i class="fas fa-info-circle fa-2x text-muted"></i>
                <h6 class="mt-2">No Loan Purpose Data</h6>
                <small class="text-muted">No borrowers found in this category.</small>
            </div>`;
        return;
    }

    try {
        // Prepare data for charts (sorted by count descending)
        const purposes = data.map(d => d.purpose);
        const counts = data.map(d => d.count);
        const percentages = data.map(d => d.percentage);
        const colors = data.map(d => d.color);
        const totalCount = counts.reduce((a, b) => a + b, 0);

        // Dynamic title based on filter
        const titleText = category && category !== 'All' 
            ? `Loan Usage (${totalCount} borrowers in ${category})` 
            : `Loan Usage Purpose (${totalCount} borrowers)`;

        // Create pie trace (FULL PIE - no hole)
        const pieTrace = {
            values: percentages,
            labels: purposes,
            type: 'pie',
            // REMOVED: hole: 0.4 to make it a full pie
            domain: { x: [0, 0.45], y: [0, 1] }, // Adjusted domain for better spacing
            marker: { 
                colors: colors, 
                line: { color: '#ffffff', width: 2 } 
            },
            textposition: 'auto', // Changed from 'inside' for better label positioning
            textinfo: 'label+percent',
            textfont: { size: 11, color: '#2c3e50', family: 'Arial, sans-serif' },
            hovertemplate: '<b>%{label}</b><br>%{value:.1f}%<br>(%{customdata} borrowers)<extra></extra>',
            customdata: counts,
            showlegend: false // Hide legend since we show labels on pie
        };

        // Create bar trace
        const barTrace = {
            y: purposes,
            x: counts,
            type: 'bar',
            orientation: 'h',
            xaxis: 'x2',
            yaxis: 'y2',
            marker: { color: colors },
            text: counts.map(c => `${c}`),
            textposition: 'outside',
            textfont: { size: 11, color: '#2c3e50', family: 'Arial, sans-serif' },
            hovertemplate: '<b>%{y}</b><br>Count: %{x}<extra></extra>',
        };

        const layout = {
            title: {
                text: `<b>🎯 ${titleText}</b>`,
                x: 0.5,
                xanchor: 'center',
                font: { size: 16, color: '#2c3e50', family: 'Arial, sans-serif' }
            },
            height: 340,
            template: 'plotly_white',
            margin: { l: 20, r: 20, t: 50, b: 40 }, // Increased margins
            showlegend: false, // Disabled legend to prevent overlap
            // Pie chart doesn't need axis config since we removed it
            
            // Bar chart axis (right side)
            xaxis2: {
                domain: [0.50, 1], // Adjusted domain for better spacing
                anchor: 'y2',
                showgrid: false,
                zeroline: false,
                showticklabels: true,
                range: [0, Math.max(...counts) * 1.15]
            },
            yaxis2: {
                domain: [0, 1],
                anchor: 'x2',
                autorange: 'reversed',
                showgrid: false,
                zeroline: false,
                tickfont: { size: 11, color: '#2c3e50' }
            }
        };

        const config = { displayModeBar: false, responsive: true };
        Plotly.newPlot(chartDiv, [pieTrace, barTrace], layout, config);
        
    } catch (error) {
        console.error('Error rendering loan purpose chart:', error);
        chartDiv.innerHTML = `
            <div class="placeholder-content text-danger" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 340px;">
                <i class="fas fa-exclamation-triangle fa-2x"></i>
                <h6 class="mt-2">Failed to Load Chart</h6>
                <small>Error: ${error.message}</small>
            </div>`;
    }
}

/**
 * Shows a loading overlay on the loan panel.
 */
function showLoadingState() {
    const cards = document.querySelectorAll('.loan-kpi-card');
    cards.forEach(card => {
        card.style.opacity = '0.6';
        card.style.pointerEvents = 'none';
    });
    document.querySelectorAll('.loan-chart-container > div').forEach(chartDiv => {
        chartDiv.style.opacity = '0.6';
    });
}

/**
 * Hides the loading overlay from the loan panel.
 */
function hideLoadingState() {
    const cards = document.querySelectorAll('.loan-kpi-card');
    cards.forEach(card => {
        card.style.opacity = '1';
        card.style.pointerEvents = 'auto';
    });
     document.querySelectorAll('.loan-chart-container > div').forEach(chartDiv => {
        chartDiv.style.opacity = '1';
    });
}


/**
 * Displays an error message in the filter status area.
 * @param {string} message - The error message to display.
 */
function showErrorState(message) {
    console.error('Loan panel error:', message);
    const statusDiv = document.getElementById('filter-status');
    if (statusDiv) {
        statusDiv.innerHTML = `
            <div class="d-flex align-items-center justify-content-between">
                <div class="d-flex align-items-center">
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    <span><strong>Error:</strong> Unable to load loan data. Please refresh.</span>
                </div>
                <button type="button" class="btn btn-sm btn-outline-dark" onclick="location.reload()">
                    <i class="fas fa-redo me-1"></i>Refresh
                </button>
            </div>`;
        statusDiv.className = 'alert alert-danger alert-dismissible mb-3';
        statusDiv.style.display = 'block';
    }
}

/**
 * Provides visual feedback when KPI cards are updated.
 */
function highlightKPICards() {
    const cards = document.querySelectorAll('.loan-kpi-card');
    cards.forEach(card => {
        card.style.transform = 'scale(1.03)';
        card.style.boxShadow = '0 4px 12px rgba(0,0,0,0.25)';
        setTimeout(() => {
            card.style.transform = 'scale(1)';
            card.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
        }, 300);
    });
}

/**
 * Fetches data and updates the entire loan panel.
 * @param {string|null} category - The category to filter by, or null for all data.
 */
export function updateLoanPanel(category) {
    console.log('Updating loan panel for category:', category || 'All');
    showLoadingState();
    
    const categoryParam = category || 'All';
    const apiUrl = `/api/loan-filtered/${encodeURIComponent(categoryParam)}`;
    
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            if (!data || typeof data.with_loan === 'undefined') {
                throw new Error('Invalid data structure received');
            }
            
            updateKPICard('loan-total-value', data.with_loan);
            updateKPICard('loan-total-subtext', `${data.with_loan_pct}% of ${data.total_respondents} respondents`);
            
            updateKPICard('loan-avg-value', formatCurrency(data.mean));
            
            updateKPICard('loan-third-label', 'Total Outstanding');
            updateKPICard('loan-third-value', formatCurrency(data.total_outstanding));
            updateKPICard('loan-third-subtext', category && category !== 'All' ? `In ${category}` : 'Sum of all loans');
            
            updateKPICard('loan-max-value', formatCurrency(data.max));
            
            renderLoanChart(data);
            highlightKPICards();
            hideLoadingState();
        })
        .catch(error => {
            console.error('Error updating loan panel:', error);
            hideLoadingState();
            showErrorState(error.message);
        });
}

/**
 * Fetches filtered loan purpose data and updates the chart.
 * @param {string|null} category - The income category to filter by.
 */
export function updateLoanPurposeChart(category) {
    console.log('Updating loan purpose chart for category:', category || 'All');
    const chartDiv = document.getElementById('loan-purpose-chart');
    if (chartDiv) chartDiv.style.opacity = '0.6';

    const categoryParam = category || 'All';
    const apiUrl = `/api/loan-purpose/${encodeURIComponent(categoryParam)}`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Loan purpose data received:', data);
            renderLoanPurposeChart(data, category);
            if (chartDiv) chartDiv.style.opacity = '1';
        })
        .catch(error => {
            console.error('Error updating loan purpose chart:', error);
            if (chartDiv) {
                chartDiv.style.opacity = '1';
                chartDiv.innerHTML = `
                    <div class="placeholder-content text-danger" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 340px;">
                        <i class="fas fa-exclamation-triangle fa-2x"></i>
                        <h6 class="mt-2">Failed to Load Chart</h6>
                        <small>${error.message}</small>
                    </div>`;
            }
        });
}

/**
 * Initializes the loan distribution chart with initial data.
 */
export function initializeLoanChart() {
    const chartContainer = document.getElementById('loan-overview-chart');
    if (!chartContainer) {
        console.error('Loan chart container not found');
        return;
    }
    
    try {
        fetch('/api/loan-filtered/All')
            .then(response => response.json())
            .then(data => {
                console.log('Initial distribution loaded:', data);
                renderLoanChart(data);
            })
            .catch(error => console.error('Error loading initial loan data:', error));
    } catch (error) {
        console.error('Error initializing loan chart:', error);
    }
}

/**
 * Initializes the loan purpose chart with initial, unfiltered data.
 */
export function initializeLoanPurposeChart() {
    const chartContainer = document.getElementById('loan-purpose-chart');
    if (!chartContainer) {
        console.error('Loan purpose chart container not found.');
        return;
    }

    console.log('Initializing loan purpose chart...');
    
    try {
        fetch('/api/loan-purpose/All')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Initial loan purpose data loaded:', data);
                renderLoanPurposeChart(data, 'All');
            })
            .catch(error => {
                console.error('Error loading initial loan purpose data:', error);
                chartContainer.innerHTML = `
                    <div class="placeholder-content text-danger" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 340px;">
                        <i class="fas fa-exclamation-triangle fa-2x"></i>
                        <h6 class="mt-2">Failed to Load Chart</h6>
                        <small>${error.message}</small>
                    </div>`;
            });
    } catch (error) {
        console.error('Fatal error initializing loan purpose chart:', error);
        chartContainer.innerHTML = `
            <div class="placeholder-content text-danger" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 340px;">
                <i class="fas fa-exclamation-triangle fa-2x"></i>
                <h6 class="mt-2">Failed to Load Chart</h6>
                <small>${error.message}</small>
            </div>`;
    }
}