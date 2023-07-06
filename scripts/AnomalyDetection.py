import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def anomaly_detection(data):

    '''

    Numerical:

    1) No outlier in the target volume column
        - There are some values that high, but does might be shoes that are sold in high volume
    2) Outliers in the Target FOB $ column -> there are some 0 values
        - There are some values that are high, but it should be high because its a premium shoe (target retail price is 330)
        - There are some 0 values, which is not possible
        - The 22.1 value is from a Kids shoe so its not an outlier
    3) Outliers in the Target Retail Price $ column -> there are some 0 values
        - There are some values that are high, but it should be high because its a premium shoe (target retail price is 330)
        - There are some 0 values, which is not possible (there are no free shoes)
    4) Outliers in the Actual FOB $ column -> there are some 0 values
        - Strange that a lot of the values are higher than the target values
        - There are some 0 values, which is not possible (no shoes can be produced for free)
        - There are some odd values that come from the Cloudamazing shoe (Man/Women) where there are only other costs which is strange
            - But most of the time its a Carry Over, which might introduce fewer costs
            - And for each of these shoes there is a corresponding shoe that has "regular values"
            - All of these outlier come from the same factory (factory 2) which might give a hint, why the behaviour exists

    Therefore, I remove all the 0 values

    Category:
        - There is outlier in the Style Update column (but I left them in the dataset),
        because the group_by operation by pandas can handle the values and print them separately
        - There is also a blank row in color update
    '''

    # Select the columns for boxplots
    columns_to_plot = ['Target Volume', 'Target FOB $', 'Target Retail Price $', 'Actual FOB $']

    # Create a figure and axes for subplots
    fig, axes = plt.subplots(1, len(columns_to_plot), figsize=(12, 4))

    # Iterate over columns and create boxplots
    for ax, column in zip(axes, columns_to_plot):
        sns.boxplot(data=data[column], ax=ax)
        ax.set_title(column)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()



def remove_anomaly(data):

    temp_data = data

    print("Number of data points before anomaly removal: "+str(len(temp_data)))

    # Remove rows with zero values in the 'Actual FOB $' column
    temp_data = temp_data[temp_data['Target FOB $'] != 0]
    temp_data = temp_data[temp_data['Target Retail Price $'] != 0]
    temp_data = temp_data[temp_data['Actual FOB $'] != 0]

    print("Number of data points before anomaly removal: "+str(len(temp_data)))

    cleaned_data = temp_data

    return cleaned_data


def anomaly_handler(data):
    #anomaly_detection(data)
    return remove_anomaly(data)