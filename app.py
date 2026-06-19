from pathlib import Path
# pyrefly: ignore [missing-import]
from src.data_loader import load_all_documents
# pyrefly: ignore [missing-import]
from src.embedding import EmbeddingPipeline
# pyrefly: ignore [missing-import]
from src.vectorstore import FaissVectorStore
# pyrefly: ignore [missing-import]
from src.search import RAGSearch

## Example usage 

if __name__ == "__main__":
    # data_path = Path(__file__).parent / "RAG" / "data"
    # docs = load_all_documents(str(data_path))
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()
    # print(store.query("what is state of art ?",top_k=3))
    # emb_pipe = EmbeddingPipeline()
    # chunks = emb_pipe.chunk_documents(docs)
    # chunkvectors = emb_pipe.embed_chunks(chunks)
    # print(chunkvectors)

    rag_search = RAGSearch()
    query = "what is state of art ?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
