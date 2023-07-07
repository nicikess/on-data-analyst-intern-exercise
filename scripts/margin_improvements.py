from .margin_calculation import add_margin_columns


def margin_calculation_statistics(data):
    temp_data = data

    # Margin vertical
    temp_data_season = temp_data.loc[
        :,
        [
            "Season",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_season = temp_data_season.groupby("Season").mean()

    # Margin vertical
    temp_data_gender = temp_data.loc[
        :,
        [
            "Gender",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_gender = temp_data_gender.groupby("Gender").mean()

    # Margin per factory
    temp_data_factory = temp_data.loc[
        :,
        [
            "Factory",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_factory = temp_data_factory.groupby("Factory").mean()

    # Margin per style update
    temp_data_style_update = temp_data.loc[
        :,
        [
            "Style Update",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_style_update = temp_data_style_update.groupby("Style Update").mean()

    # Margin per color update
    temp_data_color_update = temp_data.loc[
        :,
        [
            "Color Update",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_color_update = temp_data_color_update.groupby("Color Update").mean()

    # Margin vertical
    temp_data_vertical = temp_data.loc[
        :,
        [
            "Vertical",
            "Target Volume",
            "Target FOB $",
            "Target Retail Price $",
            "Actual FOB $",
            "target_margin",
            "actual_margin",
            "target_margin_per_piece",
            "actual_margin_per_piece",
        ],
    ]
    margin_data_vertical = temp_data_vertical.groupby("Vertical").mean()

    return [
        margin_data_season,
        margin_data_gender,
        margin_data_factory,
        margin_data_style_update,
        margin_data_color_update,
        margin_data_vertical,
    ]


def cost_calculation_statistics(data):
    temp_data = data

    # Margin vertical
    temp_data_season = temp_data.loc[
        :,
        [
            "Season",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_season = temp_data_season.groupby("Season").mean()

    # Margin vertical
    temp_data_gender = temp_data.loc[
        :,
        [
            "Gender",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_gender = temp_data_gender.groupby("Gender").mean()

    # Margin per factory
    temp_data_factory = temp_data.loc[
        :,
        [
            "Factory",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_factory = temp_data_factory.groupby("Factory").mean()

    # Margin per style update
    temp_data_style_update = temp_data.loc[
        :,
        [
            "Style Update",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_style_update = temp_data_style_update.groupby(
        "Style Update", dropna=False
    ).mean()

    # Margin per color update
    temp_data_color_update = temp_data.loc[
        :,
        [
            "Color Update",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_color_update = temp_data_color_update.groupby("Color Update").mean()

    # Margin vertical
    temp_data_vertical = temp_data.loc[
        :,
        [
            "Vertical",
            "UPPER Cost",
            "Other Cost",
            "BOTTOM Cost",
            "LABOR Cost",
            "OVERHEAD Cost",
            "Tooling Cost",
            "Actual FOB $",
        ],
    ]
    cost_data_vertical = temp_data_vertical.groupby("Vertical").mean()

    print(cost_data_style_update.to_string())

    return [
        cost_data_season,
        cost_data_gender,
        cost_data_factory,
        cost_data_style_update,
        cost_data_color_update,
        cost_data_vertical,
    ]


def margin_improvements(data):
    # Calculation costs statistics
    cost_calculation_statistics(data)

    # Add margin information to data
    temp_data = add_margin_columns(data)
    # Calculation margin statistics
    margin_calculation_statistics(temp_data)

    return [cost_calculation_statistics(data), margin_calculation_statistics(temp_data)]


"""

# Findings;

1)  When you look at the margin Men and Women Shoes have the highest margin.
    The costs however are similar to the other genders. This could indicate that the 
    Retail price could be raised for Kids and Youth shoes
    
2)  Factory 2 has the lowest costs from all the factory -> produce more at this factory
    Factory 5 has the highest costs of all factory -> produce less at this factory
    
3)  When you look more closely at the different style updates it seems odd that 'Carry Over'
    introduces the highest avg costs (Actual FOB $ -> costs). Intuitively you would expect that
    using new materials, new upper parts and creating a totally new shoe would introduce higher costs.
    
Just as info: vertical (All day, outdoor, running has the same cost-margin rank/relation

"""
