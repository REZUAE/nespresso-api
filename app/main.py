from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}


@app.get("/unhealthy")
def healthcheck():
    return {"status": "healthy"}

def healthcheck():
    return {"status": "healthy"}