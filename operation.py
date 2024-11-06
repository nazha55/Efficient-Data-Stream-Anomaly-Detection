import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plots
import numpy as np
import matplotlib.pyplot as plt
import time

# Step 1: Simulate the Data Stream
def simulate_data_stream(n_points=1000):
    """Simulate a data stream with regular patterns, peaks, and noise."""
    try:
        base_value = 500  # average transaction amount
        seasonal_pattern = 100 * np.sin(np.linspace(0, 10 * np.pi, n_points))  # periodic peaks
        random_noise = np.random.normal(0, 50, n_points)  # small random noise

        # Introduce occasional large transactions (anomalies)
        anomalies = np.random.choice([0, 1], size=n_points, p=[0.98, 0.02])
        anomaly_values = anomalies * np.random.uniform(3000, 10000, n_points)

        # Combine all components
        transaction_stream = base_value + seasonal_pattern + random_noise + anomaly_values
        
        # Validate data stream points are numeric and non-null
        if not np.all(np.isfinite(transaction_stream)):
            raise ValueError("Data stream contains non-numeric or infinite values.")

        return transaction_stream
    except Exception as e:
        print(f"Error during data simulation: {e}")
        return np.array([])  # Return an empty array in case of error

# Step 2: Real-Time Anomaly Detection Using Z-Score
def detect_anomalies(data_stream, threshold=3):
    """Detect anomalies in a data stream using Z-score."""
    anomalies = []
    try:
        # Check for empty data stream
        if len(data_stream) == 0:
            print("Empty data stream received for anomaly detection.")
            return anomalies
        
        mean = np.mean(data_stream)
        std_dev = np.std(data_stream)
        
        # Check if standard deviation is zero to prevent division by zero
        if std_dev == 0:
            print("Standard deviation is zero. Unable to calculate Z-scores.")
            return anomalies

        for index, value in enumerate(data_stream):
            # Ensure each value is numeric before processing
            if not np.isfinite(value):
                print(f"Skipping non-numeric or infinite value at index {index}.")
                continue
            
            z_score = (value - mean) / std_dev
            if np.abs(z_score) > threshold:  # Detect anomaly if Z-score exceeds threshold
                anomalies.append((index, value))

    except Exception as e:
        print(f"Error during anomaly detection: {e}")
    
    return anomalies

# Step 3: Real-Time Visualization of Data Stream with Anomalies
def plot_data_stream(data_stream, anomalies):
    """Plot the data stream with anomalies marked in real time."""
    try:
        plt.ion()  # enable interactive mode
        fig, ax = plt.subplots()
        ax.set_title("Real-Time Transaction Data with Anomalies")
        ax.set_xlabel("Time")
        ax.set_ylabel("Transaction Amount")

        batch_size = 20  # Number of points to simulate real-time streaming
        for i in range(0, len(data_stream), batch_size):
            # Plot each batch of data
            ax.plot(range(i, i + batch_size), data_stream[i:i + batch_size], color="blue")
            
            # Plot anomalies within the current batch
            for anomaly in anomalies:
                if i <= anomaly[0] < i + batch_size:
                    ax.plot(anomaly[0], anomaly[1], 'ro')  # red dot for anomaly
            
            plt.pause(0.05)  # slight pause to simulate real-time update

        plt.ioff()
        plt.show()

    except Exception as e:
        print(f"Error during plotting: {e}")
