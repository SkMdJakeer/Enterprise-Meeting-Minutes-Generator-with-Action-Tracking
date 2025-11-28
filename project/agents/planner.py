from typing import List, Dict
import uuid
from project.core.observability import get_logger

logger = get_logger()

class Planner:
    """Planner splits input into chunks and creates tasks.
    Simple heuristic planner for demo purposes.
    """
    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size

    def plan(self, transcript: str, metadata: Dict = None) -> List[Dict]:
        """Return a list of task dicts.
        Each task: {task_id, task_type, chunk}
        task_type in ['summarize','extract_actions','extract_decisions']
        """
        logger.info('Planner: starting planning')
        text = transcript.strip()
        if not text:
            return []
        # naive chunking by characters
        chunks = [text[i:i+self.chunk_size] for i in range(0, len(text), self.chunk_size)]
        tasks = []
        for idx, c in enumerate(chunks):
            tid = str(uuid.uuid4())
            tasks.append({
                "task_id": tid + "-sum",
                "task_type": "summarize",
                "chunk_index": idx,
                "chunk": c
            })
            tasks.append({
                "task_id": tid + "-act",
                "task_type": "extract_actions",
                "chunk_index": idx,
                "chunk": c
            })
            tasks.append({
                "task_id": tid + "-dec",
                "task_type": "extract_decisions",
                "chunk_index": idx,
                "chunk": c
            })
        logger.info(f'Planner: created {len(tasks)} tasks for {len(chunks)} chunks')
        return tasks

if __name__ == '__main__':
    p = Planner(chunk_size=200)
    tasks = p.plan('This is a sample meeting. Action: send report by Friday. Decision: adopt X.')
    print(tasks)
