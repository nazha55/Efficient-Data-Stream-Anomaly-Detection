# Efficient Data Stream Anomaly Detection

**Author**: Fathimathul Nazha Noufal  
**Date**: 06/11/2024  

## Overview
This project provides a real-time anomaly detection tool for continuous data streams. It is designed to detect anomalies in various metrics, such as financial transactions or system monitoring data. The tool simulates a data stream, flags unusual data points in real-time, and visualizes the results for easy analysis.

## Features
- **Real-Time Anomaly Detection**: Detects and flags anomalies as data is streamed.
- **Simulated Data Stream**: Mimics realistic data patterns with periodic and random components.
- **Threshold-Based Detection**: Allows for customizable sensitivity in detecting anomalies.
- **Visualization**: Provides a live graphical plot of the data stream, highlighting detected anomalies.

## Installation

### Step 1: Clone the repository
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/nazha55/Efficient-Data-Stream-Anomaly-Detection.git
cd Efficient-Data-Stream-Anomaly-Detection

Step 2: Install dependencies
Ensure you have Python installed and then install the required dependencies:

pip install -r requirements.txt
Running the Project
To run the anomaly detection and visualization tool, simply execute the main.py script:
python main.py
This will generate a real-time plot where the data stream is displayed, and anomalies are highlighted in red.

Customization
Threshold Sensitivity: Modify the threshold parameter in operation.py to adjust the sensitivity of the anomaly detection. Lower values will make the system more sensitive to deviations, while higher values will detect fewer anomalies.
Data Patterns: You can customize the data stream's behavior (e.g., seasonal patterns, random noise) by modifying the simulate_data_stream function in operation.py.
Conclusion
This project provides an efficient and flexible tool for real-time anomaly detection in continuous data streams. You can adjust the detection parameters and data patterns to fit your specific use case, whether it's for financial transaction monitoring, system performance tracking, or any other type of data stream analysis.
