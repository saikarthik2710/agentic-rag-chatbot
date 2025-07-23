# coordinator.py

import uuid
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

ingestor = IngestionAgent()
retriever = RetrievalAgent()
responder = LLMResponseAgent()

def process_document_and_query(file_path, user_query):
    trace_id = str(uuid.uuid4())
    mcp_ingestion = ingestor.handle(trace_id, file_path)
    mcp_retrieval = retriever.handle(trace_id, mcp_ingestion, user_query)
    mcp_response = responder.handle(trace_id, mcp_retrieval)
    return mcp_response
