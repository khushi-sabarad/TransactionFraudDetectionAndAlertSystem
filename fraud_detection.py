import pandas as pd
import datetime

def load_data(filepath):
    """Loads transaction data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def detect_high_value_transactions(df, threshold=5000):
    """Detects transactions exceeding a given threshold."""
    high_value = df[df['transaction_amount'] > threshold]
    return high_value

def detect_location_anomalies(df, user_location_history):
    """Detects transactions from unusual locations based on user history."""
    anomalies = []
    for index, row in df.iterrows():
        user_id = row['user_id']
        location = row['location']
        if user_id in user_location_history:
            if location not in user_location_history[user_id]:
                anomalies.append(row)
    return pd.DataFrame(anomalies)

def generate_report(high_value, location_anomalies):
    """Generates a fraud detection report."""
    report = "Fraud Detection Report\n"
    if not high_value.empty:
        report += "\nHigh-Value Transactions:\n" + high_value.to_string() + "\n"
    if not location_anomalies.empty:
        report += "\nLocation Anomalies:\n" + location_anomalies.to_string() + "\n"
    if high_value.empty and location_anomalies.empty:
        report += "\nNo fraudulent activity detected."
    return report

def generate_alerts(high_value, location_anomalies):
    """Generates fraud alerts."""
    alerts = []
    if not high_value.empty:
        alerts.append("High-value transactions detected.")
    if not location_anomalies.empty:
        alerts.append("Location anomalies detected.")
    if high_value.empty and location_anomalies.empty:
        alerts.append("No suspicious activity detected.")
    return alerts

def main():
    """Main function to execute fraud detection."""
    df = load_data('transactions.csv')
    if df is None:
        return

    # Dummy user location history for demonstration
    user_location_history = {
        101: ['New York'],
        102: ['London', 'New York'],
        103: ['Paris'],
        104: ['Mumbai'],
        105: ['Berlin']
    }

    high_value = detect_high_value_transactions(df)
    location_anomalies = detect_location_anomalies(df, user_location_history)

    report = generate_report(high_value, location_anomalies)
    alerts = generate_alerts(high_value, location_anomalies)

    print(report)
    print("\nAlerts:")
    for alert in alerts:
        print(f"- {alert}")

if __name__ == "__main__":
    main()