from langchain.llms import OpenAI
import os

llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])

def summarizeText(text):
    print(text) # leaving this here for now