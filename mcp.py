# utils/mcp.py

def create_mcp_message(sender, receiver, msg_type, trace_id, payload):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": msg_type,
        "trace_id": trace_id,
        "payload": payload
    }
