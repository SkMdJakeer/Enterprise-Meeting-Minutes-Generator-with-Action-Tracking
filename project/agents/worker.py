from typing import Dict, Any
from project.tools.tools import summarize_text, extract_actions, extract_decisions, normalize_date
from project.core.observability import get_logger
from project.memory.session_memory import SessionMemory
from datetime import datetime

logger = get_logger()

class Worker:
    def __init__(self, memory: SessionMemory = None):
        self.memory = memory or SessionMemory()

    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        ttype = task.get('task_type')
        chunk = task.get('chunk','')
        logger.info(f'Worker: executing task {task.get("task_id")} type={ttype}')
        if ttype == 'summarize':
            summary = summarize_text(chunk, max_sentences=3)
            return {'task_id': task.get('task_id'), 'type': ttype, 'summary': summary}
        elif ttype == 'extract_actions':
            actions = extract_actions(chunk)
            # normalize dates
            for a in actions:
                a['due_normalized'] = normalize_date(a.get('due'), base_date=datetime.utcnow())
            return {'task_id': task.get('task_id'), 'type': ttype, 'actions': actions}
        elif ttype == 'extract_decisions':
            decisions = extract_decisions(chunk)
            return {'task_id': task.get('task_id'), 'type': ttype, 'decisions': decisions}
        else:
            logger.warning(f'Worker: unknown task type {ttype}')
            return {'task_id': task.get('task_id'), 'type': ttype, 'result': None}

if __name__ == '__main__':
    from project.memory.session_memory import SessionMemory
    w = Worker(SessionMemory())
    print(w.execute({'task_id':'1','task_type':'summarize','chunk':'This is an example. We will send the report.'}))
