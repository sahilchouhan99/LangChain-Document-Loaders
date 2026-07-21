from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader=DirectoryLoader(
    path=r"D:\langchains\doc_loader\notes",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()

text=docs[0].page_content
text2=docs[0].metadata

print(text)
print(text2)

# if you have lager and big amount of pdf than we use lazy_loader() function