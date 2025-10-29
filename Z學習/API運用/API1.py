from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # 定義一個 GET 路由
def read_root():
    return {"柚子是藍梁"}

@app.get("/items/{item_id}")  
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("APITEST:app", host="127.0.0.1", port=8000, reload=True) 
