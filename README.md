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

### Latest Error

 python3 main.py -f ./examples/AirControlSatia.pdf -start 2 -dst ./examples/summary
1
Traceback (most recent call last):
  File "/home/cglavin50/coding-work/pdf-summarizer-cli/main.py", line 24, in <module>
    main()
  File "/home/cglavin50/coding-work/pdf-summarizer-cli/main.py", line 13, in main
    summary = summarizeText(text)
  File "/home/cglavin50/coding-work/pdf-summarizer-cli/handlers/chatGPTHandler.py", line 41, in summarizeText
    return textwrap.fill(output_summary, width=100, break_long_words=False, replace_whitespace=False)
  File "/usr/lib/python3.10/textwrap.py", line 399, in fill
    return w.fill(text)
  File "/usr/lib/python3.10/textwrap.py", line 371, in fill
    return "\n".join(self.wrap(text))
  File "/usr/lib/python3.10/textwrap.py", line 359, in wrap
    chunks = self._split_chunks(text)
  File "/usr/lib/python3.10/textwrap.py", line 345, in _split_chunks
    text = self._munge_whitespace(text)
  File "/usr/lib/python3.10/textwrap.py", line 154, in _munge_whitespace
    text = text.expandtabs(self.tabsize)
AttributeError: 'dict' object has no attribute 'expandtabs'
