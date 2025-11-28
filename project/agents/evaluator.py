from typing import List, Dict
from project.core.observability import get_logger
from project.memory.session_memory import SessionMemory

logger = get_logger()

class Evaluator:
    def __init__(self, memory: SessionMemory = None):
        self.memory = memory or SessionMemory()

    def evaluate(self, worker_results: List[Dict]) -> Dict:
        """Merge worker results, validate and produce final minutes JSON."""
        logger.info('Evaluator: starting evaluation')
        summary_parts = []
        actions = []
        decisions = []
        for r in worker_results:
            if r.get('type') == 'summarize' and r.get('summary'):
                summary_parts.append(r.get('summary'))
            if r.get('type') == 'extract_actions' and r.get('actions'):
                for a in r.get('actions'):
                    actions.append(a)
            if r.get('type') == 'extract_decisions' and r.get('decisions'):
                for d in r.get('decisions'):
                    decisions.append(d)
        # simple merging: join summaries and deduplicate actions by text
        summary = '\n'.join(summary_parts).strip()
        seen_texts = set()
        uniq_actions = []
        for a in actions:
            txt = a.get('text')
            if txt not in seen_texts:
                seen_texts.add(txt)
                uniq_actions.append(a)
        result = {
            'summary': summary,
            'actions': uniq_actions,
            'decisions': decisions,
            'confidence_overall': 0.8
        }
        logger.info('Evaluator: evaluation complete')
        return result

if __name__ == '__main__':
    ev = Evaluator()
    print(ev.evaluate([{'type':'summarize','summary':'A quick summary.'}]))
