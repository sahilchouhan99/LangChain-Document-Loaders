from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r"D:\langchains\doc_loader\Synopsis Minor-2.pdf")

docs=loader.load()

text=docs[0].page_content
text2=docs[1].metadata

print(text)
print(text2)

'''
pdf with table-> PDFPlumberLoader

scanned/image-> UnstructuredPDFLoader,AmazonTextractPDFLoader

layout/and image data-> PyMuPDFLoader

best structure extraction -> UnstructuredPDFLoader
'''