# agents/llm_response_agent.py

from utils.mcp import create_mcp_message
import openai

openai.api_key = "your-openai-key"

class LLMResponseAgent:
    def __init__(self):
        self.name = "LLMResponseAgent"

    def handle(self, trace_id, retrieval_msg):
        context = "\n".join(retrieval_msg["payload"]["retrieved_context"])
        query = retrieval_msg["payload"]["query"]

        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        return create_mcp_message(
            sender=self.name,
            receiver="UI",
            msg_type="FINAL_ANSWER",
            trace_id=trace_id,
            payload={"answer": response["choices"][0]["text"].strip()}
        )
