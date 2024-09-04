import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Airbnb Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Airbnb Data Analysis")

# Sidebar for file upload
uploaded_file = st.sidebar.file_uploader("Upload your Airbnb dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    
    # Sidebar filters
    st.sidebar.header("Filter the data")
    neighborhood_group = st.sidebar.multiselect("Select Neighborhood Group", df["neighbourhood_group"].unique())
    neighborhood = st.sidebar.multiselect("Select Neighborhood", df["neighbourhood"].unique())
    room_type = st.sidebar.multiselect("Select Room Type", df["room_type"].unique())
   
    
    # Apply filters
    if neighborhood_group:
        df = df[df["neighbourhood_group"].isin(neighborhood_group)]
    if neighborhood:
        df = df[df["neighbourhood"].isin(neighborhood)]
    if room_type:
        df = df[df['room_type'].isin(room_type)]

    # Display filtered data
    st.write("Filtered Data", df.head())

    # Visualization 1: Price by room type
    st.subheader("Price by Room Type")
    room_type_df = df.groupby("room_type")["price"].sum().reset_index()
    fig1 = px.bar(room_type_df, x="room_type", y="price", title="Total Price by Room Type")
    st.plotly_chart(fig1)

    # Visualization 2: Price distribution by neighborhood group
    st.subheader("Price Distribution by Neighborhood Group")
    fig2 = px.pie(df, names="neighbourhood_group", values="price", title="Price Distribution")
    st.plotly_chart(fig2)

    # Visualization 3: Map view of listings
    st.subheader("Map View of Listings")
    st.map(df[['latitude', 'longitude']])

else:
    st.write("Please upload a CSV file to start the analysis.")

