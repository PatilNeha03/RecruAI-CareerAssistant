from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import base64

# === IMPORT YOUR LOGIC ===
from final import (
    save_uploaded_file,
    upload_rejected_resume_local_to_df,
    run_formatting_compliance_last,
    run_ats_scoring_with_embedding,
    get_resume_feedback,
    get_job_recommendations,
    generate_cover_letter,
    get_chatbot_response,
    plain_resumes_df
)

app = FastAPI()

class ResumeRequest(BaseModel):
    mode: str
    resume_file: Optional[str] = None
    file_bytes: Optional[str] = None
    job_description: Optional[str] = None
    application_status: Optional[str] = None
    user_query: Optional[str] = None

@app.post("/analyze")
def analyze(payload: ResumeRequest):
    mode = payload.mode.lower()
    resume_file = payload.resume_file
    jd = payload.job_description or ""
    status = payload.application_status or "rejected"
    file_bytes = base64.b64decode(payload.file_bytes) if payload.file_bytes else None

    if mode == "upload":
        save_uploaded_file(resume_file, file_bytes)
        return upload_rejected_resume_local_to_df(resume_file, jd, status)
    elif mode == "formatting":
        return run_formatting_compliance_last()
    elif mode == "ats_score":
        return run_ats_scoring_with_embedding()
    elif mode == "resume_feedback":
        resume = plain_resumes_df[~plain_resumes_df["Resume File"].str.startswith("jd_")].iloc[-1]
        return get_resume_feedback(resume["Plain Text Resume"])
    elif mode == "job_recommendation":
        resume = plain_resumes_df[~plain_resumes_df["Resume File"].str.startswith("jd_")].iloc[-1]
        return get_job_recommendations(resume["Plain Text Resume"])
    elif mode == "cover_letter":
        text, path = generate_cover_letter()
        return {"cover_letter": text, "path": path}
    elif mode == "chatbot" and payload.user_query:
        return {"response": get_chatbot_response(payload.user_query)}
    return {"error": "Invalid mode or missing parameters"}

@app.get("/")
def health():
    return {"status": "FastAPI app is live!"}