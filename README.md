# similarity_search
This takes pdfs, creates embeddings and stores those in chromadb.

Install

Docker
You can run a Chroma server in a Docker container.

You can get the Chroma Docker image from Docker Hub, or from the Chroma GitHub Container Registry

docker pull chromadb/chroma
docker run -p 8000:8000 chromadb/chroma

You can also build the Docker image yourself from the Dockerfile in the Chroma GitHub repository

git clone git@github.com:chroma-core/chroma.git
cd chroma
docker-compose up -d --build
