from PyPDF2 import PdfReader

def extractText(filename, minPage = 0, maxPage = 0, dst = ""):
    reader = PdfReader(filename)
    text = ""
    max = len(reader.pages)
    
    # assign pages to extract from
    if maxPage == 0 or maxPage > max:
        maxPage = max
        
    # extract text
    for i in range(minPage, maxPage):
        page = reader.pages[i]
        text += page.extract_text()

    return text
# end extractText function