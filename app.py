import streamlit as st
from scanner import scan_code

st.title("SUPREME")

code_snip = st.text_area("Please enter your code")
submit = st.button("SUBMIT")

if submit:
    st.write("Scanning...")

    # Run the scanner
    result = scan_code(code_snip)

    # Display the result
    st.markdown(result)