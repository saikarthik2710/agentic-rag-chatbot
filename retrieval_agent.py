# agents/retrieval_agent.py

from embeddings.vector_store import VectorStore
from utils.mcp import create_mcp_message

class RetrievalAgent:
    def __init__(self):
        self.name = "RetrievalAgent"
        self.vs = VectorStore()

    def handle(self, trace_id, ingestion_msg, query):
        self.vs.add_document(ingestion_msg["payload"]["text"])
        top_chunks = self.vs.query(query)

        return create_mcp_message(
            sender=self.name,
            receiver="LLMResponseAgent",
            msg_type="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={"retrieved_context": top_chunks, "query": query}
        )
