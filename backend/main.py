from fastapi import FastAPI, HTTPException
from typing import Optional, List
from database import (
    create_gt,
    fetch_gt,
    export_gt
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]
# react localhost

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#  In order to make cross-origin requests 
# -- e.g., requests that originate from a different protocol, IP address, domain name, or port 
# -- you need to enable Cross Origin Resource Sharing (CORS).
# The above configuration will allow cross-origin requests from our frontend domain and port which will run at localhost:3000.


@app.post("/api/gt/{idx}/{label}")
async def post_gt(idx, label):
    response = await create_gt(idx, label) 
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/api/gt/{idx}") 
async def get_gt(idx):
    response = await fetch_gt(idx)
    return response

@app.put("/api/gt") 
async def export_all_gt():
    response = await export_gt()
    return response
