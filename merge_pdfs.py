import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def get_pdf_files(input_dir):
    # Get all .pdf files in the directory
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    
    # Filter files that are numbered and sort them
    numbered_pdfs = [f for f in pdf_files if f[:-4].isdigit()]
    numbered_pdfs.sort(key=lambda x: int(x[:-4]))

    return numbered_pdfs

def merge_pdfs(input_dir, file_names, output_path):
    pdf_writer = PdfWriter()

    for file_name in file_names:
        file_path = os.path.join(input_dir, file_name)
        pdf_reader = PdfReader(file_path)
        
        # Skip the first page and add the rest
        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    
    # Write the output PDF
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    # Check if a directory is provided as an argument
    if len(sys.argv) > 1:
        input_directory = sys.argv[1]
    else:
        input_directory = os.getcwd()

    # Get the list of PDF files in the directory
    pdf_files = get_pdf_files(input_directory)

    # If no PDF files found, print an error and exit
    if not pdf_files:
        print("Error: No numbered PDF files found in the specified directory.")
        sys.exit(1)

    output_pdf = "merged.pdf"
    merge_pdfs(input_directory, pdf_files, output_pdf)
    print(f"Merged PDF saved as {output_pdf}")

