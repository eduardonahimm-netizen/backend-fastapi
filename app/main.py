from fastapi import FastAPI

app = FastAPI(
    title="Backend Profesional",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
