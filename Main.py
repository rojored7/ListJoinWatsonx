from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

API_KEY = "miclave123"  # cámbiala por la que tú quieras

class FileMeta(BaseModel):
    id: str

class RequestData(BaseModel):
    fileIds: List[str]
    fileMetas: List[FileMeta]
@app.get("/")
async def root():
    print("Hola mundo ")
    
@app.post("/emparejar")
async def emparejar(data: RequestData, x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    paired = []
    for i in range(min(len(data.fileIds), len(data.fileMetas))):
        paired.append({
            "fileId": data.fileMetas[i].id,
            "content": data.fileIds[i]
        })

    return {"archivosConContenido": paired}
