from operation import simulate_data_stream,detect_anomalies, detect_anomalies,plot_data_stream

if __name__ == "__main__":
    # Simulate data stream
    data_stream = simulate_data_stream(1000)
    
    # Detect anomalies in the simulated stream
    anomalies = detect_anomalies(data_stream)
    
    # Plot the data stream in real-time with anomalies
    plot_data_stream(data_stream, anomalies)