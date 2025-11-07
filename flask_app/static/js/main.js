// static/js/main.js
import { 
    initializeLoanChart, 
    updateLoanPanel, 
    initializeLoanPurposeChart,
    updateLoanPurposeChart
} from './modules/loan_panel.js';
import {
    initializeDigitalTimeChart,
    updateDigitalTimeChart
} from './modules/digital_time_chart.js';

// Global state
let currentFilterCategory = null;

/**
 * Initializes all dashboard event listeners.
 */
function initializeDashboard() {
    console.log('Dashboard initialized, setting up event listeners...');
    
    // Initialize all charts
    initializeLoanChart();
    initializeLoanPurposeChart();
    initializeDigitalTimeChart(); // <-- ADDED
    
    // Listen for custom events dispatched from other charts or components
    document.addEventListener('categoryFiltered', handleCategoryFilter);
    document.addEventListener('categoryFilterReset', handleFilterReset);
    
    // Expose the reset function to the global scope for the clear button
    window.resetCategoryFilter = () => {
        console.log('Manual filter reset triggered');
        if (window.chartResetFilter) {
            window.chartResetFilter(); // Assumes the main chart exposes this
        }
        document.dispatchEvent(new CustomEvent('categoryFilterReset', { bubbles: true }));
    };
}

/**
 * Handles the 'categoryFiltered' event.
 * @param {CustomEvent} e - The event object containing the category detail.
 */
function handleCategoryFilter(e) {
    const category = e.detail.category;
    console.log('Category filtered event received in main.js:', category);
    
    currentFilterCategory = category;
    
    // Show the filter status indicator
    const statusDiv = document.getElementById('filter-status');
    const categorySpan = document.getElementById('filter-category');
    if (statusDiv && categorySpan) {
        categorySpan.textContent = category;
        statusDiv.style.display = 'block';
        setTimeout(() => statusDiv.classList.add('show'), 10);
    }
    
    // Update all dependent components
    updateLoanPanel(category);
    updateLoanPurposeChart(category);
    updateDigitalTimeChart(category); // <-- ADDED SYNCHRONIZATION
}

/**
 * Handles the 'categoryFilterReset' event.
 */
function handleFilterReset() {
    console.log('Category filter reset event received in main.js');
    
    currentFilterCategory = null;
    
    // Hide the filter status indicator
    const statusDiv = document.getElementById('filter-status');
    if (statusDiv) {
        statusDiv.classList.remove('show');
        setTimeout(() => statusDiv.style.display = 'none', 300);
    }
    
    // Reset all dependent components to show all data
    updateLoanPanel(null);
    updateLoanPurposeChart(null);
    updateDigitalTimeChart(null); // <-- ADDED SYNCHRONIZATION
}

// Initialize the dashboard when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeDashboard);