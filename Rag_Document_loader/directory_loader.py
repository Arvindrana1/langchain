from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from sympy import true

load_documents=DirectoryLoader(
    path ='Rag_Document_loader\\books',
    glob='*.pdf',
    loader_cls= PyPDFLoader
    )
docs=load_documents.lazy_load()

# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

for doc in docs:
    print(doc.metadata)
