import streamlit as st
import pandas as pd

st.set_page_config(page_title="ML Project", layout="wide")

st.title("📂 File Upload")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state["data"] = df

        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

        st.subheader("Data Preview")
        st.dataframe(df.head(10))

        st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

else:
    st.warning("⚠️ Please upload a CSV or Excel file to continue.")