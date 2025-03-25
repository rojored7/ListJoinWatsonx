from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

API_KEY = "miclave123"  # cámbiala por la que tú quieras

class RequestData(BaseModel):
    fileIds: List[str]
    contents: List[str]

@app.get("/")
async def root():
    print("Hola mundo ")

@app.post("/emparejar")
async def emparejar(data: RequestData, x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    result = []
    for i in range(min(len(data.fileIds), len(data.contents))):
        result.append({
            "fileId": data.fileIds[i],
            "content": data.contents[i]
        })

    return {"archivosConContenido": result}

