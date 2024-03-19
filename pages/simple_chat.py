import streamlit as st

st.title("simple chat")

user_message = st.text_input(label="どうしました？")

if user_message:
    ai_message = "こんにちは！"
    st.write(ai_message)
