import pypdf
import re
import warnings
reader = pypdf.PdfReader("resume1.pdf")

num_of_pages = len(reader.pages)

#define key terms
string1 = "experience"
string2 = "graduate"
string3 = "Computer Science"
string4 = "Engineering"

for page in reader.pages:
    text = page.extract_text()
    res_search = re.search(string1, text)
    print(text)
    res_search = re.search(string2, text)
    print(text)
    res_search = re.search(string3, text)
    print(text)
    res_search = re.search(string4, text)
    print(text)