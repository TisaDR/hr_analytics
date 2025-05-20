import streamlit as st
import pandas as pd
import plotly.express as px
import io
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
    return df

df = load_data()


# Title
st.title("💼 HR Analytics Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Attrition Rate", f"{df['Attrition'].mean():.2%}")
col2.metric("Avg. Monthly Income", f"${df['MonthlyIncome'].mean():,.0f}")
col3.metric("Avg. Age", f"{df['Age'].mean():.1f} years")

st.markdown("---")

# Sidebar Filters
st.sidebar.header("Filter Data")
department = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
education = st.sidebar.multiselect("Education Field", df["EducationField"].unique(), default=df["EducationField"].unique())
gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())

# Apply filters
filtered_df = df[
    (df["Department"].isin(department)) &
    (df["EducationField"].isin(education)) &
    (df["Gender"].isin(gender))
]

# Visual: Attrition by Job Role
fig1 = px.histogram(filtered_df, x="JobRole", color=filtered_df['Attrition'].map({1: 'Yes', 0: 'No'}),
                    barmode='group', title="Attrition by Job Role", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

# Visual: Monthly Income by Department
fig2 = px.box(filtered_df, x="Department", y="MonthlyIncome", color="Department",
              title="Monthly Income by Department")
st.plotly_chart(fig2, use_container_width=True)

# Visual: Satisfaction vs Attrition
fig3 = px.scatter(filtered_df, x="JobSatisfaction", y="EnvironmentSatisfaction",
                  color=filtered_df['Attrition'].map({1: 'Yes', 0: 'No'}),
                  title="Satisfaction vs Attrition", size="MonthlyIncome", hover_data=["JobRole"])
st.plotly_chart(fig3, use_container_width=True)

# Generate downloadable Excel file
output = io.BytesIO()
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    filtered_df.to_excel(writer, index=False, sheet_name='Filtered HR Data')

# Prepare binary data for download
processed_data = output.getvalue()

# Download button
st.download_button(
    label="📥 Download Filtered Data (Excel)",
    data=processed_data,
    file_name="filtered_hr_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)