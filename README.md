# pdf-summarizer-cli

A CLI tool written in Python to summarize PDF's text. Showcases LangChains map-reduce and refine chaining schemes to summarize longer pieces of text when stuffing isn't an option.

Currently, there is code in the modelHandler.py file to use both methods. As seen in the examples, Map Reduce creates longer, but arguably stronger, summaries, and is significantly faster, so that is what is currently being used (but can be modified). This repository can be configured to demonstrate both applications, and test them for yourself.

Running `$ python3 main.py` will print a help message with all the required command-line args for use.
