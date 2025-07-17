import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Line Chart")

# Create sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Product A', 'Product B', 'Product C']
)

# Display the data
st.write("Raw Data:")
st.dataframe(chart_data)

# Create line chart
st.line_chart(chart_data)

# Line chart with specific columns
st.line_chart(chart_data, x=None, y=['Product A', 'Product B'])
