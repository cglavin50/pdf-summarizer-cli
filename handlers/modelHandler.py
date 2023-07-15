from langchain.chains import RefineDocumentsChain, StuffDocumentsChain, LLMChain, ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.prompts import PromptTemplate
import os


document_prompt = PromptTemplate(
    input_variables=["page_content"],
     template="{page_content}"
) # for formatting documents
prompt_template = """Please summarize the following text:\n{text}"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
refine_template = (
    "Your job is to produce a final summary of text.\n"
    "We have provided an existing summary up to this point: {prev_answer}\n"
    "We have the opportunity to refine the existing summary " 
    "(only if needed) with the additional context from the next part of the text, provided below: \n"
    "---------\n"
    "{text}"
    "---------\n"
    "Given this additional context, refine the original summary, weighing the original summary more than the next piece to avoid recency bias between inputs."
    "If the newly provided context isn't useful in relation to the subject matter, please return the original summary."
)
refine_prompt = PromptTemplate(
    input_variables=["prev_answer", "text"],
    template = refine_template
)
reduce_template = (
    "Given smaller summaries from different parts of a larger piece of work,"
    " please combine them, creating one cohesive summary."
    "These summaries are all related, so make sure to connect contexts between them."
    "The summaries are below:"
    "---------\n"
    "{text}"
    "---------\n"
)
reduce_prompt = PromptTemplate(
    input_variables=["text"],
    template = reduce_template
)



def summarizeText(docs): # takes in an array of documents
    llm = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.3)

    return mapReduceSummary(docs, llm)
    
    
def mapReduceSummary(docs, llm):
    llm_chain = LLMChain(llm=llm, prompt = prompt)
    reduce_llm_chain = LLMChain(llm = llm, prompt = reduce_prompt)
    combine_documents_chain = StuffDocumentsChain(
        llm_chain = reduce_llm_chain,
        document_prompt=document_prompt,
        document_variable_name="text",
    )
    reduce_documents_chain = ReduceDocumentsChain(
        combine_documents_chain=combine_documents_chain,
    ) # breaks the documents down recursively, formats using the document prompt, and combines them using the StuffDocumentsChain
    
    chain = MapReduceDocumentsChain(
        llm_chain=llm_chain,
        reduce_documents_chain=reduce_documents_chain,
        verbose=True,
    )
    
    result = chain(
        inputs = docs,
        return_only_outputs = True,
    )
    return result["output_text"]  
    
def refineSummary(docs, llm):
    llm_chain = LLMChain(llm=llm, prompt = prompt)
    llm_chain_refine = LLMChain(llm=llm, prompt=refine_prompt)
    chain = RefineDocumentsChain(
        initial_llm_chain=llm_chain,
        refine_llm_chain=llm_chain_refine,
        document_variable_name="text",
        verbose=True,
        initial_response_name = "prev_answer"
    )
        
    result = chain(
        inputs = docs,
        return_only_outputs = True,
    )
    return result["output_text"]
# using the refine method
 