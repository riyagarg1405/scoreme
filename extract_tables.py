import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_excel):
    tables_list = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            if tables:  # Ensure tables exist on the page
                for table_index, table in enumerate(tables):
                    df = pd.DataFrame(table)
                    tables_list.append((f"Page_{page_num}_Table_{table_index+1}", df))
    
    if not tables_list:  # No tables found, create a dummy sheet
        print("⚠️ No tables found in the PDF. Creating an empty Excel file.")
        df_empty = pd.DataFrame(["No tables extracted"])
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            df_empty.to_excel(writer, sheet_name="No_Tables", index=False, header=False)
    else:
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            for sheet_name, table_df in tables_list:
                table_df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
    
    print(f"✅ Tables extracted and saved to {output_excel}")

# Example usage
pdf_path = "test3.pdf"  # Make sure the file is in the same directory
output_excel = "extracted_tables.xlsx"
extract_tables_from_pdf(pdf_path, output_excel)