from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
text = """
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=5,
    separators=["\n\n", "\n", " ", ""]
)

"""
text_splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=1000,
    chunk_overlap=200,
    language=Language.PYTHON
)
chunks = text_splitter.split_text(text)

print(len(chunks))
print(chunks[0])

