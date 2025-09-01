from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse;


app = FastAPI()

@app.get("/users/{user_id}page={page}&size={size}")
def get_user(user_id: int, page: int = 1, size: int = 20):
    user_data = {
        "id": user_id,
        "page": page,
        "size": size,
        }
    return JSONResponse(content=user_data, status_code=200);
    return JSONResponse(content="Bad type for provided querry parameters", status_code=404);

