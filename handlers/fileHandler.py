# this file is responsible for taking in a file name and return a langchain document (or array of documents depending on text size)
from langchain.document_loaders import PyPDFLoader

def extractText(filename, minPage = 0, maxPage = 0):
    extension = filename.split(".")[1]
    
    if extension == ".pdf":
        return extractPDF(filename, minPage, maxPage)
    if extension == ".csv":
        return extractCSV(filename, minPage, maxPage)
    if extension == ".txt":
        return extractTXT(filename, minPage, maxPage)
    if extension == ".md":
        return extractMD(filename, minPage, maxPage)
# pass to corresponding file types
    
        
        
def extractPDF(filename, minPage = 0, maxPage = 0, dst = ""):
    print("To Do")
    
def extractTXT(filename, minPage = 0, maxPage = 0, dst = ""):
    print("To Do")
    
def extractMD(filename, minPage = 0, maxPage = 0, dst = ""):
    print("To Do")

def extractCSV(filename, minPage = 0, maxPage = 0, dst = ""):
    print("To Do")
