import pypdf
from pypdf import PdfReader
reader = PdfReader("dummy.pdf")
page = reader.pages[0]
print(page.extract_text(0))

pdf_document = "dummy.pdf"
file_name = pdf_document.split('.')

with open(pdf_document, "rb") as filehandle, open(pdf_document, mode='w', encoding='UTF-8') as output:
    pdf = PdfReader(filehandle)
    num_of_pages = len(pdf.pages)
    for page_number in range(num_of_pages):
        page = pdf.pages[page_number]
        print(f"Page: {page_number+1}", file=output)
        print('', file=output)
        print(page.extract_text(), file=output)
        print('', file=output)