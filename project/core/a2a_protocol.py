import uuid
from datetime import datetime
from typing import Dict, Any

def make_envelope(from_agent: str, to_agent: str, msg_type: str, payload: Dict[str, Any], trace_id: str = None) -> Dict:
    return {
        'message_id': str(uuid.uuid4()),
        'trace_id': trace_id or str(uuid.uuid4()),
        'from': from_agent,
        'to': to_agent,
        'type': msg_type,
        'payload': payload,
        'meta': {'timestamp': datetime.utcnow().isoformat()}
    }
