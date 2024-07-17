from bs4 import BeautifulSoup
import re

class ResumeGen:

    @staticmethod
    def reduceText (text):
        headers = []
        soup = BeautifulSoup(text, features=['lxml'])
        for header in soup.findAll(re.compile("^h[1-6]$")):
            headers.append(header)

        return "\n".join(headers)

    @staticmethod
    def generate (text):
        # you may write your logic here, or call your functions here
        return ""
