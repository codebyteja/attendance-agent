import streamlit as st
import pandas as pd
from agent import generate_attendance

st.set_page_config(page_title="College Attendance System", layout="wide")

st.title("📘 College Attendance System")

# Input box
absent_input = st.text_input("Enter Absent Roll Numbers (comma separated)", "")

if st.button("Generate Attendance"):
    try:
        if absent_input.strip() == "":
            absent_list = []
        else:
            absent_list = [int(x.strip()) for x in absent_input.split(",")]

        data = generate_attendance(absent_list)

        # Table for frontend with ✔ and ✘ with colors
        ui_df = pd.DataFrame([{
            "Roll": d["roll"],
            "Name": d["name"],
            "Status": f"<span style='color: green;'>✔</span>" if d["status_ui"] == "✔"
                      else "<span style='color: red;'>✘</span>"
        } for d in data])

        st.subheader("Attendance Sheet")
        st.write(ui_df.to_html(escape=False, index=False), unsafe_allow_html=True)

        # CSV output with P/A only
        csv_df = pd.DataFrame([{
            "Roll": d["roll"],
            "Name": d["name"],
            "Attendance": d["status_csv"]
        } for d in data])

        st.download_button(
            "Download CSV",
            csv_df.to_csv(index=False),
            "attendance.csv",
            mime="text/csv"
        )

        # SMS Simulation
        st.subheader("📩 SMS Simulation")
        for d in data:
            if d["sms"]:
                st.info(d["sms"])

    except Exception as e:
        st.error(f"Error: {e}")
