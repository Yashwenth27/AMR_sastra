import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_navigation_bar import st_navbar

st.set_page_config(layout="wide")
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
navbar_html = '''
<style>
    .st-emotion-cache-h4xjwg{
        z-index: 100;
    }
    .css-hi6a2p {padding-top: 0rem;}
    .navbar {
        background-color: #007BFF;
        padding: 0.2rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        text-align: center;
    }
    .navbar h1 {
        color: white;
        font-size: 2rem;
        margin: 0;
    }
    .content {
        padding-top: 6rem;  /* Adjust this based on navbar height */
    }
</style>

<nav class="navbar">
    <h1>Antimicrobial Resistance Dashboard - SASTRA University, Thanjavur </h1>
</nav>

<div class="content">
'''

# Injecting the navigation bar and content padding into the Streamlit app
st.markdown(navbar_html, unsafe_allow_html=True)


# Load the CSV file (replace 'medical_recs.csv' with your actual file path)
df = pd.read_csv('medical_recs.csv')

# Set the header title with a green horizontal line below
# st.title("Antimicrobial Resistance Dashboard")
# st.markdown('<hr style="border:2px solid blue">', unsafe_allow_html=True)

# Organize plots in two columns
col1, col2 = st.columns(2)

# Function to generate plots with "All options" handling
def generate_plot(plot_type, df):
    if plot_type == "Geographical Map":
        st.write("Geographical Map: Number of Tests by Country")
        countries = ["All options"] + list(df['Country'].unique())
        selected_countries = st.multiselect("Select Countries", options=countries, default="All options")
        
        if "All options" in selected_countries:
            country_counts = df['Country'].value_counts().reset_index()
        else:
            filtered_df = df[df['Country'].isin(selected_countries)]
            country_counts = filtered_df['Country'].value_counts().reset_index()
        
        country_counts.columns = ['Country', 'Counts']
        if not country_counts.empty:
            fig_map = px.choropleth(country_counts, locations='Country', locationmode='country names', 
                                    color='Counts', hover_name='Country', title="Number of Tests by Country")
            st.plotly_chart(fig_map)
        else:
            st.write("No data available for the selected countries.")

    elif plot_type == "Gender Distribution":
        st.write("Gender Distribution")
        genders = ["All options"] + list(df['Gender'].unique())
        selected_genders = st.multiselect("Select Genders", options=genders, default="All options")
        
        if "All options" in selected_genders:
            gender_counts = df['Gender'].value_counts().reset_index()
        else:
            filtered_df = df[df['Gender'].isin(selected_genders)]
            gender_counts = filtered_df['Gender'].value_counts().reset_index()
        
        gender_counts.columns = ['Gender', 'Counts']
        if not gender_counts.empty:
            fig_gender = px.pie(gender_counts, values='Counts', names='Gender', title="Gender Distribution")
            st.plotly_chart(fig_gender)
        else:
            st.write("No data available for the selected genders.")

    elif plot_type == "Age Group Distribution":
        st.write("Age Group Distribution")
        age_groups = ["All options"] + list(df['Age Group'].unique())
        selected_age_groups = st.multiselect("Select Age Groups", options=age_groups, default="All options")
        
        if "All options" in selected_age_groups:
            age_group_counts = df['Age Group'].value_counts().reset_index()
        else:
            filtered_df = df[df['Age Group'].isin(selected_age_groups)]
            age_group_counts = filtered_df['Age Group'].value_counts().reset_index()
        
        age_group_counts.columns = ['Age Group', 'Counts']
        if not age_group_counts.empty:
            fig_age_group = px.bar(age_group_counts, x='Age Group', y='Counts', 
                                   title="Age Group Distribution",
                                   labels={'Counts': 'Number of Tests', 'Age Group': 'Age Group'})
            st.plotly_chart(fig_age_group)
        else:
            st.write("No data available for the selected age groups.")

    elif plot_type == "Speciality Distribution":
        st.write("Speciality Distribution")
        specialities = ["All options"] + list(df['Speciality'].unique())
        selected_specialities = st.multiselect("Select Specialities", options=specialities, default="All options")
        
        if "All options" in selected_specialities:
            speciality_counts = df['Speciality'].value_counts().reset_index()
        else:
            filtered_df = df[df['Speciality'].isin(selected_specialities)]
            speciality_counts = filtered_df['Speciality'].value_counts().reset_index()
        
        speciality_counts.columns = ['Speciality', 'Counts']
        if not speciality_counts.empty:
            fig_speciality = px.bar(speciality_counts, x='Speciality', y='Counts', 
                                    title="Speciality Distribution",
                                    labels={'Counts': 'Number of Tests', 'Speciality': 'Medical Speciality'})
            st.plotly_chart(fig_speciality)
        else:
            st.write("No data available for the selected specialities.")

    elif plot_type == "Yearly Distribution":
        st.write("Yearly Distribution")
        years = ["All options"] + list(df['Year'].unique())
        selected_years = st.multiselect("Select Years", options=years, default="All options")
        
        if "All options" in selected_years:
            year_counts = df['Year'].value_counts().reset_index()
        else:
            filtered_df = df[df['Year'].isin(selected_years)]
            year_counts = filtered_df['Year'].value_counts().reset_index()
        
        year_counts.columns = ['Year', 'Counts']
        if not year_counts.empty:
            fig_year = px.bar(year_counts, x='Year', y='Counts', 
                              title="Yearly Distribution",
                              labels={'Counts': 'Number of Tests', 'Year': 'Year'})
            st.plotly_chart(fig_year)
        else:
            st.write("No data available for the selected years.")

    elif plot_type == "Source of Infection":
        st.write("Source of Infection")
        age_groups = ["All options"] + list(df['Age Group'].unique())
        genders = ["All options"] + list(df['Gender'].unique())
        selected_age_groups = st.multiselect("Select Age Groups", options=age_groups, default="All options")
        selected_genders = st.multiselect("Select Genders", options=genders, default="All options")
        
        if "All options" in selected_age_groups and "All options" in selected_genders:
            filtered_df = df
        elif "All options" in selected_age_groups:
            filtered_df = df[df['Gender'].isin(selected_genders)]
        elif "All options" in selected_genders:
            filtered_df = df[df['Age Group'].isin(selected_age_groups)]
        else:
            filtered_df = df[(df['Age Group'].isin(selected_age_groups)) & (df['Gender'].isin(selected_genders))]
        
        if 'Source of Infection' in filtered_df.columns and not filtered_df.empty:
            fig_source = px.scatter(filtered_df, x='Source of Infection', y='Age Group', color='Gender',
                                    title="Source of Infection by Age Group and Gender", 
                                    size_max=60, hover_data=['Gender', 'Speciality'])
            st.plotly_chart(fig_source)
        else:
            st.write("No data available for the selected filters.")

# Create expanders for each plot in columns
try:
    with col1:
        with st.container(border=True):
            st.header("Geographical Map")
            #with st.expander("Apply filters"):
            generate_plot("Geographical Map", df)
            st.write("---")

        with st.container(border=True):
            st.header("Gender Distribution")
            #with st.expander("Apply filters"):
            generate_plot("Gender Distribution", df)
            st.write("---")

        with st.container(border=True):
            st.header("Age Group Distribution")
            # with st.expander("Apply filters"):
            generate_plot("Age Group Distribution", df)
            st.write("---")

    with col2:
        with st.container(border=True):
            st.header("Speciality Distribution")
            #with st.expander("Apply filters"):
            generate_plot("Speciality Distribution", df)
            st.write("---")

        with st.container(border=True):
            st.header("Yearly Distribution")
            #with st.expander("Apply filters"):
            generate_plot("Yearly Distribution", df)
            st.write("---")

        with st.container(border=True):
            st.header("Source of Infection")
            #with st.expander("Apply filters"):
            generate_plot("Source of Infection", df)
            st.write("---")
except:
    print(":)")
