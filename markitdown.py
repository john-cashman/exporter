import streamlit as st
from _markitdown import process_file  # Import your function from _markitdown.py
import tempfile
import os

# Streamlit app
st.title("PDF to Markdown Converter")
st.write("Upload a PDF file, and we'll convert it to a Markdown file!")

# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Save uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
    
    # Process the file using the _markitdown script
    try:
        st.write("Processing the uploaded file...")
        markdown_content = process_file(temp_pdf_path)
        
        # Display the Markdown output
        st.markdown("### Converted Markdown")
        st.code
