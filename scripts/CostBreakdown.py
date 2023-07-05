import pandas as pd


def cost_breakdown_overview(data):
    # Set columns to break down
    break_down_columns = ['Vertical', 'Factory']

    # Select cost columns from dataframe
    data_cost = data.loc[:, ['UPPER Cost', 'Other Cost', 'BOTTOM Cost', 'LABOR Cost', 'OVERHEAD Cost', 'Tooling Cost',
                             'Actual FOB $']]

    # List of breakdown dataframes
    break_down_dfs = []

    # Avg data over break down columns
    for column in break_down_columns:
        temp_data = pd.concat([data.loc[:, column], data_cost], axis=1)
        temp_data = temp_data.groupby(column).mean()
        break_down_dfs.append(temp_data)

    return break_down_dfs
