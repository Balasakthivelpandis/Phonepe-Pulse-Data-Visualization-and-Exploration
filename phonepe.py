import pandas as pd
import streamlit as st
import PIL 
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import geopandas as gpd



# connect to the database
import sqlite3

#establishing the connection
conn = sqlite3.connect("phonepe.db")

# create a cursor object
cursor = conn.cursor()

#with st.sidebar:
SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})


#---------------------Basic Insights -----------------#


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]
    
               #1
               
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Transaction_Year', 'Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df,x="Transaction_Amount",y="States")
            
            #2
            
    elif select=="List 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Total_Transaction'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="Total_Transaction",y="States")
            
            #3
            
    elif select=="Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute("SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_Type','Transaction_Amount '])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df,x="Transaction_Type",y="Amount")
            
            #4
            
    elif select=="Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df,x="State",y="RegisteredUsers")
            
            #5
            
    elif select=="Top 10 Districts based on states and Count of transaction":
        cursor.execute("SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Count")
            
            #6
            
    elif select=="List 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Transaction_year','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Amount")
            
            #7
            
    elif select=="List 10 Transaction_Count based on Districts and states":
        cursor.execute("SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            st.bar_chart(data=df,x="States",y="Transaction_Count")
            
            #8
             
    elif select=="Top 10 RegisteredUsers based on states and District":
        cursor.execute("SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns = ['States','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df,x="States",y="RegisteredUsers")

#----------------Home----------------------#
cursor = conn.cursor()

# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()

if SELECT == "Home":
    st.image(Image.open("phonepe.png"), width=600)  
    col1,col2, = st.columns(2)
        
    with col1:                   
        st.subheader("PhonePe, an Indian digital payments platform, was founded in 2015 and expanded to include bill payments, recharges, and wallet services. Acquired by Flipkart in 2016, it spun off in 2020, enabling innovations like SuperApps and digital banking.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    
    with col2:         
        st.video("upi.mp4", format="video/mp4")    
        
    df = pd.DataFrame(rows, columns=['States', 'Transaction_Year', 'Quarters', 'Transaction_Type', 'Transaction_Count','Transaction_Amount'])
    fig = px.choropleth(df, locations="States", scope="asia", color="States", hover_name="States",
        title="Live Geo Visualization of India")
    st.plotly_chart(fig)


#----------------About-----------------------#

if SELECT == "About":
    col1,col2 = st.columns(2)

    with col1:
        st.video("pulse-video.mp4", format="video/mp4")

    with col2:
        img = Image.open("phonepe.png")
        st.image(img, width=500) 
        st.write("---")
        st.subheader("Indian digital payments revolution is driven by mobile phones, internet, and infrastructure. PhonePe, founded in 2015, has been a beneficiary of API-driven digitisation. PhonePe Pulse provides granular data on digital payments in India, aiming to contribute to the ecosystem.")
        st.write("---")

    col1,col2 = st.columns(2)
    with col1:
        st.title("THE BEAT OF PHONEPE")
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        st.image("top (1).jpeg")
        with open("annual report.pdf","rb") as f:
            data = f.read()
        st.download_button("DOWNLOAD REPORT",data,file_name="annual report.pdf")
    with col2:
        st.image("report (1).jpeg")    

#----------------------Contact---------------#




if SELECT == "Contact":
    name = "Balasakthivelpandi s"
    mail = (f'{"Mail :"}  {"balasakthivelpandi@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "GITHUB": "https://github.com/Balasakthivelpandis",
        "LINKEDIN": "https://www.linkedin.com/in/balasakthivelpandi-subramanian"}
    
    col1, col2 = st.columns(2)
    with col2:
        st.title('Phonepe Pulse data visualisation')
        st.write("The project aims to extract data from Phonepe pulse Github repository, transform it, insert it into a SQLite3 database, and create a live geo visualization dashboard using Streamlit and Plotly in Python, providing interactive, user-friendly insights.")
        st.write("---")
        st.subheader(mail)
        st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")

