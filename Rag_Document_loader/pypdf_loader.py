from langchain_community.document_loaders import PyPDFLoader

load_documents=PyPDFLoader('Rag_Document_loader\\dl-curriculum (1).pdf')
docs=load_documents.load()

print(len(docs))

print(docs[0].page_content)

print(docs[1].metadata)

    