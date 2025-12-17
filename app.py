import pandas as pd
import streamlit as st
from src.scoring import calculate_score
from src.sheets import push_to_sheets

st.set_page_config(page_title="3D In-Vitro Lead Scoring Agent", layout="wide")

st.title("🧪 3D In-Vitro Lead Scoring Agent")
st.caption("Automated lead qualification based on role, funding, publications & geography")

# Load data
df = pd.read_csv("data/leads_raw.csv")

# Score leads
df["Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values("Score", ascending=False)

# Display
st.subheader("Qualified Leads")
st.dataframe(df, use_container_width=True)

# Actions
st.divider()

if st.button("📤 Push results to Google Sheet"):
    push_to_sheets(df, "3D In-Vitro Lead Scoring Output")
    st.success("✅ Google Sheet updated successfully")

st.download_button(
    label="⬇️ Download Qualified Leads CSV",
    data=df.to_csv(index=False),
    file_name="qualified_leads.csv",
    mime="text/csv"
)
