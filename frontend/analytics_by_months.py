import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_months_tab():
    selected_year = st.selectbox(
        "Select Year",
        options=range(2020, 2031),
        index=5 
    )
    
    try:
        response = requests.get(f"{API_URL}/monthly_summary/{selected_year}")
        response.raise_for_status()  # Raise error for bad status codes
        monthly_summary = response.json()
        
        # Check if data is empty or not in expected format
        if not monthly_summary:
            st.warning(f"No expense data found for year {selected_year}")
            return
        
        # If it's a single dict instead of a list, wrap it in a list
        if isinstance(monthly_summary, dict):
            monthly_summary = [monthly_summary]
        
        df = pd.DataFrame(monthly_summary)
        
        # Check if dataframe has the expected columns
        if df.empty or not all(col in df.columns for col in ["expense_month", "month_name", "total"]):
            st.warning(f"No valid expense data found for year {selected_year}")
            return
        
        df.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        }, inplace=True)
        
        df_sorted = df.sort_values(by="Month Number", ascending=False)
        df_sorted_display = df_sorted.copy()
        df_sorted_display.set_index("Month Number", inplace=True)

        st.title("Expense Breakdown By Months")

        st.bar_chart(
            data=df_sorted.set_index("Month Name")['Total'], 
            use_container_width=True
        )

        df_sorted_display["Total"] = df_sorted_display["Total"].map("{:.2f}".format)

        st.table(df_sorted_display)
        
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to API. Please ensure the server is running.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")