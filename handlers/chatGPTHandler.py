import textwrap
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
import os

prompt_template = """Please summarize the following text:\n{text}"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
refine_template = (
    "Your job is to produce a final summary of text.\n"
    "We have provided an existing summary up to this point: {existing_answer}"
    "Please refine the existing summary with the additional context from the next part of the text, provided below: \n"
    "---------\n"
    "{text}"
    "---------\n"
    "Given this new context for the text, refine the original summary, keeping in mind recency bias."
    "If the newly provided context isn't useful in relation to the subject matter, please return the original summary"
)
refine_prompt = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template = refine_template
)



def summarizeText(docs): # takes in an array of documents
    
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature = 0.3) # currently liking some variability, needs to be initialized on function call otherwise the environment var hasn't been established yet
    '''
    text_splitter = CharacterTextSplitter(chunk_size=3000)
    
    print(len(text))
    texts = text_splitter.split_text(text)
    print(len(texts))
    '''
    docs = [Document(page_content=t) for t in texts]
    
    print(len(docs))
    
    # summarize_prompt = PromptTemplate(template = prompt, input_variables=["text"])
    chain = load_summarize_chain(
        llm = llm, 
        chain_type = "refine",
        return_intermediate_steps= True,
        question_prompt = prompt,
        refine_prompt = refine_prompt
    )
    
    output_summary = chain({"input_documents": docs}, return_only_outputs = True)
    return textwrap.fill(output_summary, width=100, break_long_words=False, replace_whitespace=False)