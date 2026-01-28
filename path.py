import streamlit as st

st.title("Odd or Even Checker")

# Input number
num = st.number_input("Enter a number:", step=1)

# Button to check
if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{int(num)} is an Even number")
    else:
        st.info(f"{int(num)} is an Odd number")
