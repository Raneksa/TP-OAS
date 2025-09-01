
from fastapi import FastAPI;
from fastapi.responses import Response, JSONResponse;

app = FastAPI();

@app.Get("/ping")
def pong():
    return Response(content="pong", status_code=200, media_type="text/plain")