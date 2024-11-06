# Efficient Data Stream Anomaly Detection

**Author**: Fathimathul Nazha Noufal  
**Date**: 06/11/2024

## Overview
This project provides a real-time anomaly detection tool for continuous data streams. It is designed to identify anomalies in various metrics, such as financial transactions or system monitoring data. The tool simulates a data stream, detects unusual data points in real-time, and visualizes the results for easy analysis.

## Features
- **Real-Time Anomaly Detection**: Detects and flags anomalies as data is streamed.
- **Simulated Data Stream**: Mimics realistic data patterns with periodic and random components.
- **Threshold-Based Detection**: Allows customizable sensitivity in detecting anomalies.
- **Visualization**: Generates a live graphical plot of the data stream, with anomalies highlighted.

## Installation

### Step 1: Clone the repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/nazha55/Efficient-Data-Stream-Anomaly-Detection.git
cd Efficient-Data-Stream-Anomaly-Detection
Step 2: Install dependencies
Ensure you have Python installed, then install the required dependencies with:

bash
Copy code
pip install -r requirements.txt
Running the Project
To run the anomaly detection and visualization tool, execute the main.py script:

bash
Copy code
python main.py
This will generate a real-time plot displaying the data stream, with anomalies highlighted in red.

Customization
Threshold Sensitivity: Modify the threshold parameter in operation.py to adjust the sensitivity of anomaly detection. Lower values make the system more sensitive to deviations, while higher values will detect fewer anomalies.

Data Patterns: Customize the behavior of the data stream (e.g., seasonal patterns, random noise) by adjusting the simulate_data_stream function in operation.py.

Conclusion
This project offers an efficient and flexible tool for real-time anomaly detection in continuous data streams. The detection parameters and data patterns can be adjusted to suit your specific use case, whether for monitoring financial transactions, system performance, or any other data stream analysis.
