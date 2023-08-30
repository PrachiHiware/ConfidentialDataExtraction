# Required Libraries
import pandas as pd
import PyPDF2
from docx import Document
import re
import hashlib 
# File Reading
def read_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
            return pdf_text
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None

def read_docx(file_path):
    try:
        doc = Document(file_path)
        doc_text = ""
        for para in doc.paragraphs:
            doc_text += para.text + "\n"
        return doc_text
    except Exception as e:
        print(f"Error reading DOCX file: {e}")
        return None

# Data Extraction
def extract_data(text):
    # Use regular expressions or other methods to extract key data points
    # Example: Extract phone numbers using regex
    phone_numbers = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    return phone_numbers

# Security Measures
#def secure_data(data):
    # Implement data anonymization techniques if required
    # For example, hashing or encryption of sensitive information
    # On-premises processing can be achieved by keeping the processing local

# Security Measures
# Example secure_data function with simple substitution "encryption"
def secure_data(data):
    encrypted_data = []
    for item in data:
        encrypted_item = ""
        for char in item:
            encrypted_char = chr(ord(char) + 1)  # Shift each character by 1
            encrypted_item += encrypted_char
        encrypted_data.append(encrypted_item)
    return encrypted_data


# Example usage
# phone_numbers = ["123-456-7890", "555-123-4567", "987-654-3210"]
# hashed_phone_numbers = secure_data(phone_numbers)
# print("Original Phone Numbers:", phone_numbers)
# print("Hashed Phone Numbers:", hashed_phone_numbers)

# Main Function
def process_confidential_data(file_path, file_type):
    if file_type == "excel":
        data = read_excel(file_path)
    elif file_type == "pdf":
        text = read_pdf(file_path)
        data = extract_data(text)
    elif file_type == "docx":
        text = read_docx(file_path)
        data = extract_data(text)
    
    if data:
        secure_data(data)
        return data
    else:
        return None

# Example usage
file_path = "resume.pdf"
file_type = "pdf"  # or "excel" or "docx"
extracted_data = process_confidential_data(file_path, file_type)

if extracted_data:
    print("Original Data:", extracted_data)
    encrypted_data = secure_data(extracted_data)
    print("Encrypted Data:", encrypted_data)
else:
    print("No data extracted or an error occurred.")

