from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text generation"
)

model=ChatHuggingFace(llm=llm)

pro=PromptTemplate(
    template="write a summary on the following {poem}",
    input_variables=['poem']
)

parser=StrOutputParser()

chain= pro | model | parser

loader=TextLoader(r"D:\langchains\doc_loader\gym.txt",encoding="utf-8")
docs=loader.load()
text = docs[0].page_content
test1=docs[0].metadata

res=chain.invoke({"poem":text})
print(res)