import streamlit as st
from markitdown._markitdown import process_file  # Assuming the function processes PDFs to Markdown
import tempfile
import os

# Streamlit app
st.title("PDF to Markdown Converter")
st.write("Upload a PDF file, and we'll convert it to a Markdown file using Markitdown!")

# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Save uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
    
    # Process the file using Markitdown
    try:
        st.write("Processing the uploaded file...")
        markdown_content = process_file(temp_pdf_path)
        
        # Display the Markdown output
        st.markdown("### Converted Markdown")
        st.code(markdown_content, language="markdown")

        # Allow user to download the Markdown file
        markdown_filename = uploaded_file.name.replace(".pdf", ".md")
        st.download_button(
            label="Download Markdown File",
            data=markdown_content,
            file_name=markdown_filename,
            mime="text/markdown",
        )

    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")
    finally:
        # Clean up temporary file
        os.unlink(temp_pdf_path)

