# pdf-summarizer-cli

A CLI tool written in Python to summarize PDF's text. Uses Python's PyPDF package to open and extract the text, and LangChain to use OpenAI's GPT-3.5 Turbo model for the backing LLM. Refine-chaining is used to minimize information loss and maximize correctness of summaries.

## To Do

- Compare run times with parallelization in divide-and-conquer strategy
