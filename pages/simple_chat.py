import streamlit as st
from openai import OpenAI

st.title("simple chat")

user_message = st.text_input(label="どうしました？")

if user_message:
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    st.write(completion)
