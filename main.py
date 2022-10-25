from fastapi import FastAPI
from tasks import add

app = FastAPI()


@app.get("/", status_code=202)
async def root():
    task_resp = add.apply_async((1, 2))
    resp = {"asyncTaskId": task_resp.id, "status_code": 202}
    return resp

@app.get("/w", status_code=200)
async def withoutCelery():
    resp = add(1,2)
    return resp