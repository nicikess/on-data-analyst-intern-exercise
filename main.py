import pandas as pd

# Import different tasks
from scripts.CostBreakdown import cost_breakdown_overview
from scripts.MarginCalculation import margin_calculation
from scripts.SpecificMargin import specific_margin_calculation
from scripts.ToolTargetMargin import tool_target_margin
from scripts.MarginImprovements import margin_improvements
from scripts.AnomalyDetection import anomaly_handler


def read_data(file):
    return pd.read_csv(file)


def run_cost_breakdown_task(data):
    # Cost breakdown overview
    break_down_results = cost_breakdown_overview(data)
    print(break_down_results[1].to_string(float_format='%.2f'))
    return break_down_results


def run_margin_calculation_task(data):
    print(margin_calculation(data).to_string(float_format='%.2f'))
    return data


def run_specific_margin_calculation_task(data, margin_data):
    return specific_margin_calculation(data, margin_data)


def run_margin_improvements(data):
    return margin_improvements(data)


def run_anomaly_detection(data):
    return anomaly_handler(data)


def run_tool_target_margin(data):
    return tool_target_margin(data)


if __name__ == "__main__":
    # Read the data
    file_name = "product_creation_analyst_intern_case_study.csv"
    data_location = "dataset/"
    file = data_location + file_name
    data = read_data(file)

    # Handle anomalies

    # Task 1
    #run_cost_breakdown_task(data)

    # Task 2
    #margin_data = run_margin_calculation_task(data)

    # Task 3
    #lowest_and_highest_margin = specific_margin_calculation(data, margin_data)

    # Task 4
    #margin_improvement = run_margin_improvements(data)

    # Task 5
    # -> See task 4

    # Task 6
    #run_anomaly_detection(data)


    # Task X
    tool = run_tool_target_margin(data)








