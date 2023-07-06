
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

    return margin_data
