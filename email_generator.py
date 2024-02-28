from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import api_key

llm = OpenAI(
    openai_api_key=api_key.api_key,
    temperature=0.0,
)

prompt = PromptTemplate(
    input_variables=[],
    template=""""
    """,
)
