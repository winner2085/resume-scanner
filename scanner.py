import pypdf
import re
import warnings
reader = pypdf.PdfReader("resume1.pdf")

points = [0, 0, 0, 0, 0, 0]
index = 0

#define key terms pt 2
exp = ["computer science", "engineering", "research", "intern", "tutor", "project", "software engineering", "associate", "app", "years"]
lead = ["host", "capitan", "tutor", ]
edu = ["Ph.D", "B.S.", "bachelor", "graduate", "4.0", "computer science", "engineering"]
skls = ["java", "javascript", "python", "html", "css", "c++", "c#", "C", "SQL"]

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

print()