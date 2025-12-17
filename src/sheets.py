import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st


def push_to_sheets(df, sheet_name):
    """
    Push the final ranked DataFrame to a Google Sheet
    for easy review and reproducibility.
    """

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp"], scope
    )


    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1

    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
