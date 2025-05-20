from fastapi import FastAPI, Header
from contextlib import asynccontextmanager
from fetchers.oai import OAIComplete
import os, aioredis, json

# Initial Setup

TTL_SECONDS = 60 * 60 * 2 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once per Uvicorn worker:
    #     1. Before the first request  -> create Redis pool
    #     2. After the worker shuts down -> close pool

    redis: aioredis.Redis = aioredis.from_url(
        os.environ["REDIS_URL"],
        decode_responses=True,
        encoding="utf-8",
    )

    app.state.redis = redis

    try:
        yield
    finally:
        await redis.close()


app = FastAPI(lifespan=lifespan)

# Routes

@app.post("/chat/oai")
async def chat(userInput: UserInput):
    messages = userInput.messages
    session_id = userInput.session_id
    
    redis: aioredis.Redis = app.state.redis
    key = f"chat:{session_id}"

    raw = await redis.get(key)
    history = json.loads(raw) if raw else []
    history.append(messages)

    responseMsg: OAIMsg = OAIComplete(history)
    history.append(responseMsg)
    
    await redis.set(key, json.dumps(history), ex=TTL_SECONDS)

    return {"reply": responseMsg["content"]}