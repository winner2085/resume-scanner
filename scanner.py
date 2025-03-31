import pypdf
import re
import warnings
reader = pypdf.PdfReader("resume1.pdf")
page = reader.pages[0]
text = page.extract_text()

points = [0, 0, 0, 0, 0, 0]
index = 0


print(text)

#define key terms

exp = ["computer science", "engineering", "research", "intern", "tutor", "project", "software engineering", "associate", "app", "years"]
lead = ["host", "capitan", "tutor"]
edu = ["Ph.D", "B.S.", "bachelor", "graduate", "4.0", "computer science", "engineering"]
skls = ["java", "javascript", "python", "html", "css", "c++", "c#", "C", "SQL"]




'''def find(exp, lead, edu, skls):
    found = []
    if keyword.lower() in text.lower():
        found.append(keyword)
    return found

found = find(exp, lead, edu, skls)'''

def points(exp, lead, edu, skls):
    global points
    if exp:
        points[index] += 2
    if lead:
        points[index] += 1
    if edu:
        points[index] += 1.5
    if skls:
        points[index] += 1

'''if ():
    print(exp)
    print(lead)
    print(edu)
    print(skls)'''

def find_keywords_in_pdf(pdf_path, keywords, exp, lead, edu, skls):
    """
    Finds keywords in a PDF file and prints their occurrences and page numbers.

    Args:
        pdf_path (str): The path to the PDF file.
        keywords (list): A list of keywords to search for.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                text += page.extract_text() + " "
            
            found_keywords = {}
            for keyword in keywords:
                count = text.lower().count(keyword.lower())
                if count > 0:
                    found_keywords[keyword] = {"count": count, "pages": []}
                    for page_num, page in enumerate(pdf_reader.pages):
                      if keyword.lower() in page.extract_text().lower():
                        found_keywords[keyword]["pages"].append(page_num + 1)

            if found_keywords:
              print("Keywords found:")
              for keyword, data in found_keywords.items():
                  print(f"  '{keyword}':")
                  print(f"    Count: {data['count']}")
                  print(f"    Pages: {', '.join(map(str, data['pages']))}")
            else:
                print("No keywords found in the PDF.")
                
    except FileNotFoundError:
        print(f"Error: File not found at '{pdf_path}'")
    except Exception as e:
         print(f"An error occurred: {e}")

# Example usage
pdf_file_path = 'resume1.pdf'
exp = ["computer science", "engineering", "research", "intern", "tutor", "project", "software engineering", "associate", "app", "years"]
lead = ["host", "capitan", "tutor"]
edu = ["Ph.D", "B.S.", "bachelor", "graduate", "4.0", "computer science", "engineering"]
skls = ["java", "javascript", "python", "html", "css", "c++", "c#", "C", "SQL"]

find_keywords_in_pdf(pdf_file_path, keywords, exp, lead, edu, skls)