from fastapi import FastAPI, HTTPException
from google.cloud import firestore
from pydantic import BaseModel
from typing import Optional
import logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
db = firestore.Client.from_service_account_json("serviceAccountKey.json")
users_ref = db.collection("users")

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

@app.post("/users/")
async def create_user(user: User):
    doc_ref = users_ref.document()
    doc_ref.set(user.dict())
    return {"id": doc_ref.id, "message": "User created successfully"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    doc = users_ref.document(user_id).get()
    if doc.exists:
        return doc.to_dict()
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    doc_ref = users_ref.document(user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")
    doc_ref.update(user.dict())
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    doc_ref = users_ref.document(user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")
    doc_ref.delete()
    return {"message": "User deleted successfully"}

# Dokumentasi otomatis tersedia di http://127.0.0.1:8000/docs
