import sys
sys.path.append('./src')
from services.chroma_service import chroma_service
from services.contract_service import contract_service

# Get Texts from example PDF
contractService = contract_service()
texts = contractService.get_contracts()

# Connect to local chroma and add documents
chroma_connector = chroma_service(collection = "power_purchase_agreement6")
chroma_connector.add_documents(documents = texts)

#Query chroma for similarity
results = chroma_connector.query("Who has the right to install the facility?")

#Print results
print(results['documents'])




