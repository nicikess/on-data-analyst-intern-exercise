import streamlit as st
import matplotlib.pyplot as plt


def data_for_visualisation(data):
    temp_data = data

    temp_data = temp_data.loc[:, ['Style Name', 'Vertical', 'Target Retail Price $', 'Actual FOB $']]

    data_allday = temp_data[temp_data['Vertical'] == 'Performance All Day']
    data_running = temp_data[temp_data['Vertical'] == 'Performance Running']
    data_outdoor = temp_data[temp_data['Vertical'] == 'Performance Outdoor']

    temp_data = {
        'Performance All Day': data_allday,
        'Performance Running': data_running,
        'Performance Outdoor': data_outdoor
    }

    for key, value in temp_data.items():
        temp_data[key] = value.groupby(['Style Name', 'Vertical'], as_index=False).mean()

    return temp_data


def tool_target_margin(data):

    data = data_for_visualisation(data)

    st.set_page_config(layout="wide")

    # Set up the app title and description
    st.title("Product Analysis")
    st.write("Welcome to the Product Analysis app!")

    st.divider()

    # Create the three tabs for different product types
    tabs = ["Performance All Day", "Performance Running", "Performance Outdoor"]
    st.sidebar.markdown("<h3 style>Navigation</h3>", unsafe_allow_html=True)
    selected_tab = st.sidebar.radio("Select your product branch", tabs, )

    # Create two columns
    col1, col2 = st.columns([2,1], gap='large')

    # First section: Histogram plot with sliders for retail price and actual cost
    with col1:
        # Retrieve the selected product data for the current tab
        selected_product_data = data[selected_tab]

        st.subheader("Section 1: Histogram Plot")
        retail_price = st.slider("Retail Price", 0, 500, 100)
        actual_cost = st.slider("Actual Cost", 0, 500, 70)

        # Calculate the margin based on the retail price and actual cost
        margin = (selected_product_data['Target Retail Price $'] - selected_product_data['Actual FOB $']).round(0)

        # Extract the 'Style Name' index values
        style_names = selected_product_data['Style Name'].unique()

        # Plot the histogram
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(style_names, margin, color='grey')
        ax.set_xlabel("Product")
        ax.set_ylabel("Margin")

        # Rotate the x-axis labels if needed
        plt.xticks(rotation=90)

        st.pyplot(fig)

    # Second section: Dropdown menu and sliders for specific product margin
    with col2:
        # Retrieve the selected product data for the current tab
        selected_product_data = data[selected_tab]

        st.subheader("Section 2: Product Margin")
        selected_product = st.selectbox("Select a Product", selected_product_data['Style Name'].unique())

        # Retrieve the current margin for the selected product
        selected_product_data_filtered = selected_product_data[selected_product_data['Style Name'] == selected_product]

        # Subracting two columns results in series, therefore item() method must be applied to get the float value
        margin = (selected_product_data_filtered['Target Retail Price $'] - selected_product_data_filtered[
            'Actual FOB $']).round(0).item()
        st.write("Current Margin:", margin)

        # Sliders for retail price and actual cost of the selected product
        new_retail_price = st.slider("New Retail Price", 0.0, 500.0, selected_product_data_filtered['Target Retail Price $'].item())
        new_actual_cost = st.slider("New Actual Cost", 0.0, 500.0, selected_product_data_filtered['Actual FOB $'].item())

        # Calculate the new margin based on the sliders' values
        new_margin = new_retail_price - new_actual_cost

        st.write("New Margin:", new_margin)