# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import resources.constants as constants
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter  
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
import chromadb




os.environ["OPENAI_API_KEY"] = constants.APIKEY


loader = TextLoader("./state_of_the_union.txt", encoding='utf8')
data = loader.load()

student_info = """
Alexandra Thompson, a 19-year-old computer science sophomore with a 3.7 GPA,
is a member of the programming and chess clubs who enjoys pizza, swimming, and hiking
in her free time in hopes of working at a tech company after graduating from the University of Washington.
"""

club_info = """
The university chess club provides an outlet for students to come together and enjoy playing
the classic strategy game of chess. Members of all skill levels are welcome, from beginners learning
the rules to experienced tournament players. The club typically meets a few times per week to play casual games,
participate in tournaments, analyze famous chess matches, and improve members' skills.
"""

university_info = """
The University of Washington, founded in 1861 in Seattle, is a public research university
with over 45,000 students across three campuses in Seattle, Tacoma, and Bothell.
As the flagship institution of the six public universities in Washington state,
UW encompasses over 500 buildings and 20 million square feet of space,
including one of the largest library systems in the world.
"""


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)


# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")



chroma_client = chromadb.HttpClient(host='localhost', port=8000)
collection = client.create_collection(name="Students")

collection.add(
    documents = [student_info, club_info, university_info],
    metadatas = [{"source": "student info"},{"source": "club info"},{'source':'university info'}],
    ids = ["id1", "id2", "id3"]
)


#collection = chroma_client.get_collection(name="test_collection")

#collection.add(
#    documents=["This is a document", "This is another document"],
#    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#    ids=["id1", "id2"]
#)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

result = collection.similarity_search("This is  a query document")


#db = Chroma.from_documents(texts, embedding_function)

#query = "What do you know about the ukraine war?"
#docs = db.similarity_search(query)

print("ANSWERS")
print(results)

#print(docs[0].page_content)
print("!!!")