from typing import List, Dict, Tuple
import re
import uuid
from datetime import datetime, timedelta

def summarize_text(text: str, max_sentences: int = 3) -> str:
    """Naive summarizer: pick top N sentences by length as a simple heuristic."""
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    sents = [s.strip() for s in sents if s.strip()]
    sents_sorted = sorted(sents, key=lambda s: len(s), reverse=True)
    top = sents_sorted[:max_sentences]
    return ' '.join(top)

def extract_actions(text: str) -> List[Dict]:
    """Very simple action extractor using regex for imperative sentences and keywords."""
    actions = []
    # split into sentences
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    for s in sents:
        s_clean = s.strip()
        if not s_clean:
            continue
        # look for action verbs patterns or 'will'/'shall'
        if re.search(r'\b(send|share|create|update|submit|prepare|follow up|assign|schedule|book)\b', s_clean, re.I) or re.search(r"\bwill\b", s_clean, re.I):
            # try to find owner by 'to X' or 'by X' or '@Name'
            owner = None
            m = re.search(r'by ([A-Z][a-zA-Z]+)', s_clean)
            if m:
                owner = m.group(1)
            m2 = re.search(r'to ([A-Z][a-zA-Z]+)', s_clean)
            if m2:
                owner = owner or m2.group(1)
            # try due date
            due = None
            m3 = re.search(r'by (\bnext\b|\bthis\b|\bnext\s+\w+\b|\bFriday\b|\bMonday\b)', s_clean, re.I)
            if m3:
                due = m3.group(0)
            actions.append({
                'id': str(uuid.uuid4()),
                'text': s_clean,
                'owner': owner,
                'due': due,
                'confidence': 0.7
            })
    return actions

def extract_decisions(text: str) -> List[Dict]:
    decisions = []
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    for s in sents:
        s_clean = s.strip()
        if not s_clean:
            continue
        if re.search(r'\b(decide|decision|agreed|approve|approved|adopt)\b', s_clean, re.I):
            decisions.append({'id': str(uuid.uuid4()), 'text': s_clean, 'confidence': 0.8})
    return decisions

def normalize_date(rel_text: str, base_date: datetime = None) -> str:
    """Very naive normalization: handles 'next Friday', 'Friday', 'tomorrow'."""
    if base_date is None:
        base_date = datetime.utcnow()
    if not rel_text:
        return None
    t = rel_text.lower()
    if 'tomorrow' in t:
        return (base_date + timedelta(days=1)).date().isoformat()
    weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for i,w in enumerate(weekdays):
        if w in t:
            # find next weekday
            days_ahead = (i - base_date.weekday() + 7) % 7
            if 'next' in t or days_ahead == 0:
                days_ahead = days_ahead if days_ahead !=0 else 7
            return (base_date + timedelta(days=days_ahead)).date().isoformat()
    return None

if __name__ == '__main__':
    text = 'Alice: Please send the report by next Friday. Bob: We decided to adopt the new schema.'
    print(summarize_text(text))
    print(extract_actions(text))
    print(extract_decisions(text))
    print(normalize_date('next Friday'))
