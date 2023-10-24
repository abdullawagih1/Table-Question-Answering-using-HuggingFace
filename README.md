# Table Question Answering with Streamlit

A Streamlit application that uses the Hugging Face Transformers library to perform table-based question answering. Users can upload a CSV file, ask questions about the data in the table, and get answers using the TAPAS model.

## Features

- Upload a CSV file.
- Ask questions about the table data.
- Get answers using the TAPAS model.

## Usage

1. Start the Streamlit app.

2. Upload a CSV file: Click the "Upload a CSV file" button and select a CSV file from your local machine. The app will read and load the data from the CSV file into a DataFrame.

3. View the uploaded data: The uploaded CSV data is displayed in a table format, allowing you to review its contents.

4. Enter your question: In the "Enter your question" text input field, type a question related to the data in the uploaded table.

5. Ask the question: Click the "Ask" button to submit your question.

6. Get the answer: The TAPAS model will process the table and your question to provide an answer. The answer is displayed under the "Answer" subheader.

## Installation

To run the app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   
