import pandas as pd

# Import for cost break down task (Task 1)
from scripts.CostBreakdown import cost_breakdown_overview
from scripts.MarginCalculation import margin_calculation
from scripts.SpecificMargin import specific_margin_calculation


def read_data(file):
    return pd.read_csv(file)


def run_cost_breakdown_task(data):
    # Cost breakdown overview
    break_down_results = cost_breakdown_overview(data)
    print(break_down_results[1].to_string(float_format='%.2f'))


def run_margin_calculation_task(data):
    return margin_calculation(data)


def run_specific_margin_calulation_task(margin_data):
    return specific_margin_calculation(margin_data)


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
    margin_data = run_margin_calculation_task(data)

    # Task 3
    lowest_and_highest_margin = specific_margin_calculation(data, margin_data)

    # Task 4









