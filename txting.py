import markdown as md

class MarkdownDoc:

    def __init__ (self, FILE):

        if(FILE is None or FILE.closed):
            raise RuntimeError("Passed file handler is closed or not valid")
        
        self.html = md.markdown(FILE.read(), output_format="html")
    
    def spit_html (self):
        return self.html
    
    # TODO: Create an HTML parser. Or maybe not cuz wx.HtmlWindow did everything for me
    # I'm not sure if feeling good or bad for this...
    # Geez, this language does everything for you XDDDD