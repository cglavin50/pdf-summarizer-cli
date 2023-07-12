# pdf-summarizer-cli

A CLI tool written in Python to summarize PDF's text. Uses Python's PyPDF package to open and extract the text, and LangChain to use OpenAI's ChatGPT model to summarize the text.

## To Do

- Investigate prompt splitter
- Learn how to use LangChain to train ChatGPT on given text
- Split PDF text into multiple strings for memory utilization
    - Python strings are immutable, so the += operation currently used is really sub-optimized
    - They are array of characters (same as C), so appending not useable. Instead maybe create a string for each page? Or an array of strings?
- Likely not needed, but could investigate use of concurrency when extracting text from PDF's. As we go on a per-page basis, we could have multiple threads reading different pages to optimize
    - Becomes more important after I map this to a web application
- Likely switching to have flow come from fileHandler instead of PDF handler
    - First build out PDF capabilities, then expand from there
    - Using LangChain Document loaders
    - rm pdfHandler?
