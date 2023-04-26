from fastapi import FastAPI
import tensorflow_hub as hub

app = FastAPI()
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/api/embedding")
async def api_embedding(body: dict):
    query_list = body.get("query")
    if not query_list:
        return {"result": []}
    res = model(query_list)
    return {"result": res.numpy().tolist()}
