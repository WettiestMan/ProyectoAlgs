from bs4 import BeautifulSoup
import markdown
import re

with open("TEST.md") as file:
  
    html = markdown.markdown(file.read(), extensions=["toc"])
    soup = BeautifulSoup(html, features='lxml')
    for header in soup.findAll(re.compile("^h[1-6]$")):
        print(header.name)
        print(header.contents[0])
        print(header.get("id"))