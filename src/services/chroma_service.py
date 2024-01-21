import chromadb

class chroma_service:
    
    def __init__(self, collection):
      self.collection = collection

    def get_chroma_client(self):
        chroma_client = chromadb.HttpClient(host='localhost', port=8000)
        return chroma_client

    def add_documents(self, documents):
        # create the open-source embedding function
        #embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        chroma_client = self.get_chroma_client()
        collection = chroma_client.get_or_create_collection(name=self.collection)
        id = 1
        
        for dict in documents:
            content = dict.page_content
            page_number = dict.metadata
         
            collection.add(
                documents = [content],
                metadatas = [page_number],
                ids = [str(id)]
                )
            id += 1
            
            
    def query(self, queryString):
        chroma_client = self.get_chroma_client()   
        collection = chroma_client.get_or_create_collection(name=self.collection)
    
        results = collection.query(
            query_texts=[queryString],
            n_results=1
        )
        
        return results