from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path=r"D:\langchains\doc_loader\employees_30.csv")

docs=loader.load()

text=docs[0].page_content

print(text)
