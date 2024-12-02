from fastapi import FastAPI

### Create FastAPI instance with custom docs and openapi url
app = FastAPI()

@app.get("/api/hello")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

# summarize text
@app.get("/api/summarize/{text}")
def summarize_text(text: str):
    return {"summary": text}