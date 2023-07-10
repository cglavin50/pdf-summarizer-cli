from PyPDF2 import PdfReader

def extractText(filename, minPage = 0, maxPage = 0, dst = ""):
    reader = PdfReader(filename)
    text = ""
    max = maxPage = len(reader.pages)
    
    # assign pages to extract from
    if maxPage == 0 or maxPage > max:
        maxPage = max
        
    # extract text
    for i in range(minPage, maxPage):
        page = reader.pages[i]
        text += page.extract_text()
        
    # write text to destination file
    if dst == "": # print to CLI
        print(text, flush = True)
    else:
        file = open(dst, 'w')
        count = file.write(text)
        if count == 0:
            raise Exception("Error, no text was found from the PDF provided. Exiting...")
        file.close()
# end extractText function