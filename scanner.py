import pypdf
from pypdf import PdfReader

reader = pypdf.PdfReader('Victoria Gjelaj - First Crusade Questions.pdf')

print(len(reader.pages))

print(reader.pages[0].extract_text())

text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)