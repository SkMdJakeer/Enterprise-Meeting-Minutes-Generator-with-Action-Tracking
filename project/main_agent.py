from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.observability import get_logger
from typing import Dict
import uuid

logger = get_logger('main_agent')

class MainAgent:
    def __init__(self):
        self.memory = SessionMemory()
        self.planner = Planner()
        self.worker = Worker(self.memory)
        self.evaluator = Evaluator(self.memory)

    def handle_message(self, user_input: str) -> Dict:
        """Orchestrate the Planner->Worker->Evaluator flow and return a response dict."""
        meeting_id = str(uuid.uuid4())
        logger.info(f'MainAgent: new meeting {meeting_id}')
        self.memory.create_session(meeting_id)
        self.memory.write(meeting_id, 'raw_transcript', user_input)
        tasks = self.planner.plan(user_input, metadata={'meeting_id': meeting_id})
        worker_results = []
        for t in tasks:
            res = self.worker.execute(t)
            worker_results.append(res)
        final = self.evaluator.evaluate(worker_results)
        # write final minutes to memory
        self.memory.write(meeting_id, 'minutes', final)
        response = {
            'meeting_id': meeting_id,
            'response': final
        }
        return response

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result['response']

if __name__ == '__main__':
    print(run_agent('Alice: Please send the status report by next Friday. Bob: We decided to adopt the new schema.'))
