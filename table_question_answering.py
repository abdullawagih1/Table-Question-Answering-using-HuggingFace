import pandas as pd
import streamlit as st
from transformers import pipeline

model = pipeline(task="table-question-answering", 
               model="google/tapas-base-finetuned-wtq")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    df = df.astype(str)

    st.subheader("Uploaded CSV Data")
    st.write(df.head())

    question = st.text_input("Enter your question:")
    
    if st.button("Ask"):
        # Use the TAPAS model to answer the question
        answer = model(table=df, query=question)
        
        st.subheader("Answer:")
        st.write(answer['answer'])