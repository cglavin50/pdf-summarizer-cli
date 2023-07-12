# this file is responsible for taking in a file name and return a langchain document (or array of documents depending on text size)
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter

def extractText(filename, minPage = 1, maxPage = -1):
    slices = filename.split(".")
    extension = slices[len(slices)-1]
    
    loader = NotImplemented
    pages = NotImplemented
    
    if extension == "pdf":
        loader = PyPDFLoader(filename)
    if extension == "csv":
        loader = CSVLoader(filename, csv_args={
            'delimiter': ',',
        })
    if extension == "txt":
        text_splitter = CharacterTextSplitter()
        with open(filename) as f:
            text = f.read()
        pages = text_splitter.split_text(text)
    if extension == "md":
        loader = UnstructuredMarkdownLoader(filename)
       
    if type(pages) != NotImplemented: # as txt case is already handled
        pages = loader.load_and_split() 
    
    if maxPage > len(pages) or maxPage < 0:
        maxPage = len(pages)
    
    docs = []
    for page in range(minPage, maxPage):
        docs.append(pages[page-1])
        
    return docs
# end extractText function from various fileTypes
