import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


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
    col1, col2 = st.columns([3, 1], gap='large')
    with col1:
        # Add the title and description
        st.title("Product Analysis")
        st.write("Welcome to the Product Analysis app!")

    with col2:
        # Add a logo
        logo_image = "scripts/img/on-running-logo-vector.png"  # Replace with the path to your logo image
        st.image(logo_image, width=75)  # Adjust the width as per your requirements

    st.divider()

    # Create the three tabs for different product types
    tabs = ["Performance Running", "Performance Outdoor", "Performance All Day", ]
    st.sidebar.markdown("<h3 style>Navigation</h3>", unsafe_allow_html=True)
    selected_tab = st.sidebar.radio("Select your product branch", tabs, )

    # Create two columns
    col1, col2 = st.columns([2,1], gap='large')

    # First section: Histogram plot with sliders for retail price and actual cost
    with col1:
        # Retrieve the selected product data for the current tab
        selected_product_data_histo = data[selected_tab]

        st.subheader("Section 1: Histogram Plot")

        # Create two columns
        col1_slider, col2_slider = st.columns([1, 1], gap='large')

        with col1_slider:
            retail_price = st.slider("Increase retail price (0% - 100%)", 1, 100, 1, step=10)
        with col2_slider:
            actual_cost = st.slider("Increase cost (0% - 100%)", 1, 100, 1, step=10)

        retail_fraction = (retail_price / 100) + 1
        actual_fraction = (actual_cost / 100) + 1

        selected_product_data_histo['Target Retail Price $'] = selected_product_data_histo['Target Retail Price $'] * retail_fraction
        selected_product_data_histo['Actual FOB $'] = selected_product_data_histo['Actual FOB $'] * actual_fraction

        # Calculate the margin based on the retail price and actual cost
        margin = (selected_product_data_histo['Target Retail Price $'] - selected_product_data_histo['Actual FOB $']).round(0)

        # Extract the 'Style Name' index values
        style_names = selected_product_data_histo['Style Name'].unique()

        # Plot the histogram
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(style_names, margin, color='darkgrey', edgecolor='white')

        # Set labels and title
        ax.set_xlabel("Product", fontsize=12, fontweight='bold')
        ax.set_ylabel("Margin", fontsize=12, fontweight='bold')

        # Rotate the x-axis labels if needed
        plt.xticks(rotation=45, ha='right')

        # Remove spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Add grid lines
        ax.grid(axis='y', linestyle='--', alpha=0.5)

        # Add data labels
        for i, v in enumerate(margin):
            ax.text(i, v + 2, str(v), color='black', ha='center', fontsize=5)

        # Adjust layout
        plt.tight_layout()

        # Display the histogram
        st.pyplot(fig)

    # Second section: Dropdown menu and sliders for specific product margin
    with col2:
        # Retrieve the selected product data for the current tab
        selected_product_data = data[selected_tab]

        st.subheader("Section 2: Product Margin")
        selected_product = st.selectbox("Select a Product", selected_product_data['Style Name'].unique())

        # Retrieve the current margin for the selected product
        selected_product_data_filtered = selected_product_data[selected_product_data['Style Name'] == selected_product]

        st.write("Current Retail Price:", selected_product_data_filtered['Target Retail Price $'].round(0).item())
        st.write("Current FOB:", selected_product_data_filtered['Actual FOB $'].round(0).item())

        # Subracting two columns results in series, therefore item() method must be applied to get the float value
        margin = (selected_product_data_filtered['Target Retail Price $'] - selected_product_data_filtered[
            'Actual FOB $']).round(0).item()
        st.write("**Current Margin:**", margin)

        # Sliders for retail price and actual cost of the selected product
        new_retail_price = st.slider("New Retail Price", 0, 500, int(selected_product_data_filtered['Target Retail Price $'].item()), step=10)
        new_actual_cost = st.slider("New Actual Cost", 0, 500, int(selected_product_data_filtered['Actual FOB $'].item()), step=10)

        # Calculate the new margin based on the sliders' values
        new_margin = new_retail_price - new_actual_cost

        st.write("New Margin:", new_margin)