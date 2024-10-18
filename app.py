import streamlit as st
import google.generativeai as genai
import os
import time

# Set up the Google Generative AI API key
os.environ["API_KEY"] = 'AIzaSyCyP-Dd4suFMt459CkpXhWTDZXuNcHVVCc'
genai.configure(api_key=os.environ["API_KEY"])

# Define a list of customer queries
customer_queries = [
    "I have a problem with my Citi credit card. The payment isn't reflected in my account.",
    "I lost my Citi debit card, and I need to block it immediately. Please help!",
    "I was charged twice for a transaction I made at a store. Can you reverse the duplicate charge?",
    "I applied for a personal loan a month ago, but I haven’t received any update. What’s the status?",
    "My account was debited incorrectly for an amount I didn’t authorize. How can I get a refund?",
    "I'm having trouble accessing my Citi account online. The login page keeps giving an error.",
    "My credit limit was reduced without any notification. I need to understand why.",
    "I made a payment through the Citi app, but it’s still showing as pending. Can you resolve this?",
    "I want to increase my credit card limit. What’s the procedure for this?",
    "There are unknown charges on my statement. I need assistance in investigating this."
]

# Set instruction for summarization
instruction = 'You are a text summarizer. Summarize the customer service conversation in 3 lines.'

# Set up the generative model with the instruction
model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)

# Create a button to start processing queries
st.title("Customer Query Summarizer")

# A button to start the automation process
if st.button("Start"):
    st.write("Processing summaries one by one...")
    
    # Loop through each customer query
    for idx, query in enumerate(customer_queries):
        st.write(f"Original Query {idx + 1}: {query}")
        
        # Generate the summary for each query
        response = model.generate_content(query)
        
        # Display the summary
        st.write(f"Summary {idx + 1}: {response.text}\n")
        
        # Delay to simulate processing one-by-one
        time.sleep(3)  # Adjust the delay as per your requirement