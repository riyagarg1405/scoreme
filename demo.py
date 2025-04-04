import pdfplumber

pdf_path = "test3.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        print(page.extract_text())