# 檔名: main.py
from fastapi import FastAPI

app = FastAPI()

# 這是首頁，網址是 /
@app.get("/")
def read_root():
    return {"Hello": "World", "Status": "Success"}

# 這是另一個頁面，網址是 /items/{item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "q": "你剛剛輸入了上面的數字"}