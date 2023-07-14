from langchain.chains import RefineDocumentsChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.prompts import PromptTemplate
import os

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
    "Given this additional context, refine the original summary, taking care to avoid recency bias."
    "If the newly provided context isn't useful in relation to the subject matter, please return the original summary."
)
refine_prompt = PromptTemplate(
    input_variables=["prev_answer", "text"],
    template = refine_template
)



def summarizeText(docs): # takes in an array of documents
    llm = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.3)
        
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
 