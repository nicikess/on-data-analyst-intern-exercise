import pandas as pd

# Import different tasks
from scripts.tool_margin import tool_target_margin
from scripts.anomaly_detection import anomaly_handler


def read_data(file):
    return pd.read_csv(file)


if __name__ == "__main__":
    # Read the data
    file_name = "product_creation_analyst_intern_case_study.csv"
    data_location = "dataset/"
    file = data_location + file_name
    data = read_data(file)

    # Remove anomalies
    data = anomaly_handler(data)

    # Run tool
    tool = tool_target_margin(data)
