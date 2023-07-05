
def add_margin_columns(data):

    temp_data = data

    # Calculate margin and round to 2 decimal places
    temp_data['target_margin'] = (temp_data['Target Retail Price $'] - temp_data['Target FOB $']) * temp_data['Target Volume']
    temp_data['actual_margin'] = (temp_data['Target Retail Price $'] - temp_data['Actual FOB $']) * temp_data['Target Volume']

    temp_data['target_margin_per_piece'] = (temp_data['Target Retail Price $'] - temp_data['Target FOB $'])
    temp_data['actual_margin_per_piece'] = (temp_data['Target Retail Price $'] - temp_data['Actual FOB $'])

    return temp_data


def margin_calculation(data):

    temp_data = add_margin_columns(data)

    # Select relevant columns (Style, Target volume, Target FOB $, Target Retail Price $, Actual FOB $)
    temp_data = temp_data.loc[:, ['Style Name', 'Target Volume', 'Target FOB $', 'Target Retail Price $', 'Actual FOB $', 'target_margin', 'actual_margin', 'target_margin_per_piece', 'actual_margin_per_piece']]

    # Group by style name and calculate mean
    margin_data = temp_data.groupby('Style Name').mean()

    # Round margins
    margin_data['target_margin'] = margin_data['target_margin'].round(2)
    margin_data['actual_margin'] = margin_data['actual_margin'].round(2)
    margin_data['target_margin_per_piece'] = margin_data['target_margin_per_piece'].round(2)
    margin_data['actual_margin_per_piece'] = margin_data['actual_margin_per_piece'].round(2)

    return margin_data
