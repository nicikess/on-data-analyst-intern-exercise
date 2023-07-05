from .MarginCalculation import add_margin_columns


def lowest_and_highest_margin_calculation(margin_data):

    temp_data = margin_data

    # Highest and least margin over including volume
    temp_data_sorted = temp_data.sort_values(by=['actual_margin'], ascending=False)
    # Select top 1 and bottom 1 actual margin
    highest_and_lowest_margin = temp_data_sorted.iloc[[0, -1]]

    # Highest and least margin per piece
    temp_data_sorted = temp_data.sort_values(by=['actual_margin_per_piece'], ascending=False)
    # Select top 1 and bottom 1 actual margin
    highest_and_lowest_margin_per_piece = temp_data_sorted.iloc[[0, -1]]

    return highest_and_lowest_margin, highest_and_lowest_margin_per_piece


def seasonal_margin_calculation(data):
    # Add margin columns and aggregate by style name
    temp_data = add_margin_columns(data)

    season_one = 'FW23'
    season_two = 'SS23'
    temp_data_season_one = temp_data[temp_data['Season'] == season_one]
    temp_data_season_two = temp_data[temp_data['Season'] == season_two]

    season_temp_data = [temp_data_season_one, temp_data_season_two]

    season_results = []

    for season_data in season_temp_data:
        # Select relevant columns (Style, Target volume, Target FOB $, Target Retail Price $, Actual FOB $)
        temp_data = season_data.loc[:,
                    ['Style Name', 'Target Volume', 'Target FOB $', 'Target Retail Price $', 'Actual FOB $',
                     'target_margin', 'actual_margin', 'target_margin_per_piece', 'actual_margin_per_piece']]
        # Group by season and style name and calculate mean
        temp_data = temp_data.groupby(['Style Name']).mean()
        lowest_and_highest_margin, lowest_and_highest_margin_per_piece = lowest_and_highest_margin_calculation(temp_data)
        season_results.append([lowest_and_highest_margin, lowest_and_highest_margin_per_piece])

    return season_results

def specific_margin_calculation(data, margin_data):

    highest_and_lowest_margin, highest_and_lowest_margin_per_piece = lowest_and_highest_margin_calculation(margin_data)
    test = seasonal_margin_calculation(data)
    print(test)

