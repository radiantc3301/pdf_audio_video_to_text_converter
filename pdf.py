from PyPDF2 import PdfReader
import time

def extract_text_data(pdf_path, txt_path):
    reader = PdfReader(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            f.write(text + '\n')

start_time = time.time()

pdf_path = 'example3.pdf'
txt_path = 'pdf.txt'
extract_text_data(pdf_path, txt_path)

end_time = time.time()

time_taken = end_time - start_time
print(f'Time taken: {time_taken} seconds')