import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'daily_temp.csv'  # Ensure the correct path to the CSV file
data = pd.read_csv(file_path)

# Data preprocessing
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')
data.set_index('날짜', inplace=True)

data['Year'] = data.index.year
annual_data = data.groupby('Year').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'min',
    '최고기온(℃)': 'max'
}).reset_index()

annual_data.columns = ['Year', 'Average Temperature (℃)', 'Minimum Temperature (℃)', 'Maximum Temperature (℃)']

# Streamlit app
st.title('Annual Temperature Changes')

# Option to choose the type of plot
plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

# Create plots
fig, ax = plt.subplots(figsize=(10, 6))
if plot_type == 'Line Plot':
    ax.plot(annual_data['Year'], annual_data['Average Temperature (℃)'], label='Average Temperature (℃)')
    ax.plot(annual_data['Year'], annual_data['Minimum Temperature (℃)'], label='Minimum Temperature (℃)')
    ax.plot(annual_data['Year'], annual_data['Maximum Temperature (℃)'], label='Maximum Temperature (℃)')
elif plot_type == 'Bar Plot':
    width = 0.25
    x = annual_data['Year']
    ax.bar(x - width, annual_data['Average Temperature (℃)'], width, label='Average Temperature (℃)')
    ax.bar(x, annual_data['Minimum Temperature (℃)'], width, label='Minimum Temperature (℃)')
    ax.bar(x + width, annual_data['Maximum Temperature (℃)'], width, label='Maximum Temperature (℃)')

ax.set_xlabel('Year')
ax.set_ylabel('Temperature (℃)')
ax.set_title('Annual Average, Minimum, and Maximum Temperature Changes')
ax.legend()

st.pyplot(fig)
