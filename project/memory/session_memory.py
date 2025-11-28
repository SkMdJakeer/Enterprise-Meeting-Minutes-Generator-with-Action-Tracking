from typing import Dict, Any
from datetime import datetime

class SessionMemory:
    """A very small in-memory session store for demo purposes."""
    def __init__(self):
        self.store = {}

    def create_session(self, meeting_id: str) -> None:
        self.store[meeting_id] = {'created_at': datetime.utcnow().isoformat(), 'data': {}}

    def write(self, meeting_id: str, key: str, value: Any) -> None:
        if meeting_id not in self.store:
            self.create_session(meeting_id)
        self.store[meeting_id]['data'][key] = value

    def read(self, meeting_id: str, key: str):
        return self.store.get(meeting_id, {}).get('data', {}).get(key)

    def dump(self, meeting_id: str):
        return self.store.get(meeting_id)

if __name__ == '__main__':
    m = SessionMemory()
    m.create_session('m1')
    m.write('m1','a',123)
    print(m.dump('m1'))
