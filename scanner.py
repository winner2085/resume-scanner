import pypdf
import re
import warnings
reader = pypdf.PdfReader("sample-local-pdf.pdf")

# Filter out all warnings, including those from pypdf
warnings.filterwarnings("ignore")

# To specifically ignore UserWarnings which often include the "wrong pointing object" messages
warnings.filterwarnings("ignore", category=UserWarning)

num_of_pages = len(reader.pages)

#define key terms
string1 = "three"

for page in reader.pages:
    text = page.extract_text()
    res_search = re.search(string1, text)
    print(res_search)