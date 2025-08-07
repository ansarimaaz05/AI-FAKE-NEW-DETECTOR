
import streamlit as st
from predict import predict_news

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection App")
st.write("Enter a news headline or short article below to check if it's real or fake.")

user_input = st.text_area("Your News Text", height=150)

if st.button("Check"):
    if user_input.strip() != "":
        result = predict_news(user_input)
        st.subheader("Result:")
        st.success(result if "Real" in result else result)
    else:
        st.warning("Please enter some text.")
