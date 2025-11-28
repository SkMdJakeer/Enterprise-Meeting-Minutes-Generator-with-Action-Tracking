from typing import Dict
import json

DEFAULT_PROMPTS = {
    'planner': 'You are the Planner. Split transcript into chunks and create tasks.',
    'worker': 'You are the Worker. Execute task and return only structured JSON.',
    'evaluator': 'You are the Evaluator. Merge and validate worker outputs.'
}
def validate_minutes_schema(minutes: Dict) -> bool:
    required = ['summary','actions','decisions']
    for r in required:
        if r not in minutes:
            return False
    return True

def to_json(obj: Dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)
