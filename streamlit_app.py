import streamlit as st

st.set_page_config(page_title="Model Demo", layout="centered")

st.title("🧠 Model Demo")
st.write("Welcome! This is a simple Streamlit app to demonstrate my model.")

# Example user input
user_input = st.text_input("Enter some text:")

if st.button("Predict"):
    if user_input.strip():
        # Replace this with your real prediction code
        st.success(f"Prediction for '{user_input}': ✅ Example output")
    else:
        st.warning("Please enter some text first.")

st.write("---")
st.caption("Made with ❤️ using Streamlit")
