from bs4 import BeautifulSoup
import re
import ai

class ResumeGen:

    @staticmethod
    def reduceText(text):
        headers = []

        soup = BeautifulSoup(text, features=['lxml'])
        for header in soup.findAll(re.compile("^h[1-6]$")):
            headers.append(header.contents[0])

        return "\n".join(headers)

    @staticmethod
    def generate (text):
        
        return ai.get_resume(text)
