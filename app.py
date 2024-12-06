import streamlit as st
import openai 

openai.api_key = "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"  # Replace with your actual OpenAI API key

st.title("GitHub Docs Assistant")  
st.write("Ask any question related to GitHub!") 
query = st.text_input("Your question:")  

if query:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": query}],  
    )
    st.write(response['choices'][0]['message']['content'].strip()) 