import pandas as pd

# Import different tasks
from scripts.cost_breakdown import cost_breakdown_overview
from scripts.margin_calculation import margin_calculation
from scripts.specific_margin import specific_margin_calculation
from scripts.margin_improvements import margin_improvements
from scripts.anomaly_detection import anomaly_handler


def read_data(file):
    return pd.read_csv(file)


def run_cost_breakdown_task(data):
    # Cost breakdown overview
    break_down_results = cost_breakdown_overview(data)
    print(break_down_results[1].to_string(float_format="%.2f"))
    return break_down_results


def run_margin_calculation_task(data):
    data = margin_calculation(data)

    # Select columns to print
    data_print = data.loc[
        :,
        [
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]

    # Rename columns
    data_print = data_print.rename(
        columns={
            "target_margin": "Target Margin",
            "actual_margin": "Actual Margin",
            "target_margin_per_piece": "Target Margin per Piece",
            "actual_margin_per_piece": "Actual Margin per Piece",
        }
    )

    # Order by Actual Maring per Piece
    data_print = data_print.sort_values(by=["Actual Margin per Piece"], ascending=False)

    # Save dataframe to txt file
    print("Save dataframe to txt file")
    data_print.to_csv(
        "scripts/output/margin_calculation.csv", index=True, float_format="%.2f"
    )
    return data


def run_specific_margin_calculation_task(data, margin_data):
    margin_results = specific_margin_calculation(data, margin_data)

    # Print the lowest margin
    lowest_and_highest_margin = margin_results[0][["target_margin", "actual_margin"]]
    lowest_and_highest_margin_per_piece = margin_results[1][
        ["target_margin_per_piece", "actual_margin_per_piece"]
    ]

    # Rename columns
    lowest_and_highest_margin = lowest_and_highest_margin.rename(
        columns={"target_margin": "Target Margin", "actual_margin": "Actual Margin"}
    )
    lowest_and_highest_margin_per_piece = lowest_and_highest_margin_per_piece.rename(
        columns={
            "target_margin_per_piece": "Target Margin per Piece",
            "actual_margin_per_piece": "Actual Margin per Piece",
        }
    )

    # Seasonal results

    # FW23
    season_fw23_values = margin_results[2][0]
    season_fw23_lowest_and_highest_margin = season_fw23_values[0][
        ["target_margin", "actual_margin"]
    ]
    season_fw23_lowest_and_highest_margin_per_piece = season_fw23_values[1][
        ["target_margin_per_piece", "actual_margin_per_piece"]
    ]
    season_fw23_lowest_and_highest_margin = season_fw23_lowest_and_highest_margin.rename(
        columns={"target_margin": "Target Margin", "actual_margin": "Actual Margin"}
    )
    season_fw23_lowest_and_highest_margin_per_piece = season_fw23_lowest_and_highest_margin_per_piece.rename(
        columns={
            "target_margin_per_piece": "Target Margin per Piece",
            "actual_margin_per_piece": "Actual Margin per Piece",
        }
    )

    # SS23
    season_fw24_values = margin_results[2][1]
    season_fw24_lowest_and_highest_margin = season_fw24_values[0][
        ["target_margin", "actual_margin"]
    ]
    season_fw24_lowest_and_highest_margin_per_piece = season_fw24_values[1][
        ["target_margin_per_piece", "actual_margin_per_piece"]
    ]
    season_fw24_lowest_and_highest_margin = season_fw24_lowest_and_highest_margin.rename(
        columns={"target_margin": "Target Margin", "actual_margin": "Actual Margin"}
    )
    season_fw24_lowest_and_highest_margin_per_piece = season_fw24_lowest_and_highest_margin_per_piece.rename(
        columns={
            "target_margin_per_piece": "Target Margin per Piece",
            "actual_margin_per_piece": "Actual Margin per Piece",
        }
    )

    return margin_results


def run_margin_improvements(data):
    return margin_improvements(data)


def run_anomaly_detection(data):
    return anomaly_handler(data)


def run_analysis(data):

    # Remove anomalies
    data = run_anomaly_detection(data)

    # Uncommet a specific task to get the analysis results

    # Task 1
    run_cost_breakdown_task(data)

    # Task 2
    # margin_data = run_margin_calculation_task(data)

    # Task 3
    # lowest_and_highest_margin = run_specific_margin_calculation_task(data, margin_data)

    # Task 4
    # margin_improvement = run_margin_improvements(data)


if __name__ == "__main__":
    # Read the data
    file_name = "product_creation_analyst_intern_case_study.csv"
    data_location = "dataset/"
    file = data_location + file_name
    data = read_data(file)

    # Run analysis
    run_analysis(data)
