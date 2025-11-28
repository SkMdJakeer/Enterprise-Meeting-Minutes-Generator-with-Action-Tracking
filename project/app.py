from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from project.main_agent import run_agent

app = FastAPI(title='Meeting Minutes Agent')

class TranscriptIn(BaseModel):
    transcript: str

@app.post('/process')
def process_transcript(body: TranscriptIn):
    if not body.transcript:
        raise HTTPException(status_code=400, detail='Empty transcript')
    result = run_agent(body.transcript)
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
