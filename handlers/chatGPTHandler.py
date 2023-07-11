from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
import os

prompt = PromptTemplate.from_template("Summarize the following content in {length} words: {content}")
llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature = 0.3) # currently liking some variability
# these both are initialized upon import and don't need to be recreated, check langchain docs for recommendations about model initialization

def summarizeText(text, length=250):
    text_splitter = CharacterTextSplitter()
    
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts]
    
    summarize_prompt = PromptTemplate(tempplate = prompt, inpout_variables=["content"])
    chain = load_summarize_chain(llm, chain_type = "stuff", prompt=summarize_prompt)