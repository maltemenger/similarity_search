"""
Spyder Editor

This is a temporary script file.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter  
from langchain_community.document_loaders import PyPDFLoader

class contract_service:

    def get_contracts(self):
        # os.environ["OPENAI_API_KEY"] = constants.APIKEY
        loader = PyPDFLoader("resources/data/power_purchase_agreement.pdf")
        pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=20)
        texts = text_splitter.split_documents(pages)

        # create the open-source embedding function
        #embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        return texts



