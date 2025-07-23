# agents/ingestion_agent.py

import os
from utils.mcp import create_mcp_message
from utils.document_loader import extract_text_from_file

class IngestionAgent:
    def __init__(self):
        self.name = "IngestionAgent"

    def handle(self, trace_id, file_path):
        content = extract_text_from_file(file_path)
        return create_mcp_message(
            sender=self.name,
            receiver="RetrievalAgent",
            msg_type="INGESTION_RESULT",
            trace_id=trace_id,
            payload={"text": content, "source": file_path}
        )
