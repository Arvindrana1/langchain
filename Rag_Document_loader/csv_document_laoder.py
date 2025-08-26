from langchain_community.document_loaders import CSVLoader  

load_documents=CSVLoader('Rag_Document_loader\\rag.csv')
docs=load_documents.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)