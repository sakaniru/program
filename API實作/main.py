from typing import Union
from fastapi import FastAPI, Depends, HTTPException # 記得加上 HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# --- 這裡原本寫錯了 ---
# ❌ 錯誤寫法 (你現在的樣子)：
# from sqlalchemy import sessionmaker, declarative_base, Session 
load_dotenv("secret.env")
# ✅ 正確寫法 (請改成這樣)：
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
# ---------------------

# ... (後面的程式碼都不用動)
# ================= 1. 資料庫連線設定 (MySQL) =================
# 格式：mysql+pymysql://帳號:密碼@IP:Port/資料庫名稱
# ★★★ 請將 'root:123456' 改成你的 MySQL 帳號密碼 ★★★
# ✅ 帳號通常是 root
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# 建立引擎 (Engine)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 建立 Session (負責執行對話的窗口)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立 Base (所有資料表的基底)
Base = declarative_base()

# ================= 2. 定義資料庫模型 (Table) =================
# 這是真正存進 MySQL 資料表裡的結構
class DBItem(Base):
    __tablename__ = "items"  # 資料庫裡的表名會叫 items

    id = Column(Integer, primary_key=True, index=True) # 自動產生 ID
    name = Column(String(50)) # 限制名字最長 50 字
    price = Column(Float)
    is_offer = Column(Boolean, default=True)

class DBgayItem(Base):
    __tablename__ = "gay_items"  # 資料庫裡的表名會叫 gay_items

    id = Column(Integer, primary_key=True, index=True) # 自動產生 ID
    name = Column(String(50)) # 限制名字最長 50 字
    nickname = Column(String(50))
    is_offer = Column(Boolean, default=False)

class DBtestItem(Base):
    __tablename__ = "test_only"  # 資料庫裡的表名會叫 test_only

    id = Column(Integer, primary_key=True, index=True) # 自動產生 ID
    test_name = Column(String(50)) # 限制名字最長 50 字
    test_tester = Column(String(50))
    is_offer = Column(Boolean, default=False)

# 讓程式啟動時，自動去資料庫檢查有沒有 'items' 表，沒有就建立
Base.metadata.create_all(bind=engine)

# ================= 3. 定義 Pydantic 模型 (Schema) =================
# 這是前端傳進來的 JSON 格式 (不用傳 ID，ID 是資料庫產生的)
class ItemSchema(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class GayItemSchema(BaseModel):
    name: str
    nickname: str
    is_offer: Union[bool, None] = None

class TestItemSchema(BaseModel):
    test_name: str
    test_tester: str
    is_offer: Union[bool, None] = None

app = FastAPI()

# 依賴函式：每次請求進來時打開資料庫，請求結束後關閉
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "MySQL World"}

# [POST] 新增商品 (真的寫入 MySQL)
@app.post("/item/")
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    # 1. 把前端傳來的資料 (ItemSchema) 轉成 資料庫格式 (DBItem)
    db_item = DBItem(
        name=item.name, 
        price=item.price, 
        is_offer=item.is_offer
    )
    
    # 2. 存入資料庫
    db.add(db_item)
    db.commit()         # 確認交易
    db.refresh(db_item) # 重新抓取資料 (為了拿到自動生成的 id)
    
    return db_item

# [GET] 讀取所有商品 (真的從 MySQL 拿)
@app.get("/item/")
def read_items(db: Session = Depends(get_db)):
    # 翻譯：SELECT * FROM items;
    items = db.query(DBItem).all()
    return items

@app.post("/gay/")
def create_gay_item(item: GayItemSchema, db: Session = Depends(get_db)):
    db_item = DBgayItem(
    name=item.name, 
    nickname=item.nickname, 
    is_offer=item.is_offer
    )
    
    # 2. 存入資料庫
    db.add(db_item)
    db.commit()         # 確認交易
    db.refresh(db_item) # 重新抓取資料 (為了拿到自動生成的 id)
    
    return db_item
@app.get("/gay/")
def read_gay_items(db: Session = Depends(get_db)):
    # 翻譯：SELECT * FROM gay_items;
    items = db.query(DBgayItem).all()
    return items

@app.post("/test/")
def test_endpoint(item: TestItemSchema, db: Session = Depends(get_db)):
    db_item = DBtestItem(
        test_name=item.test_name,
        test_tester=item.test_tester,
        is_offer=item.is_offer
    )

    # 2. 存入資料庫
    db.add(db_item)
    db.commit()         # 確認交易
    db.refresh(db_item) # 重新抓取資料 (為了拿到自動生成的 id)

    return db_item
@app.get("/test/")
def read_test_items(db: Session = Depends(get_db)):
    # 翻譯：SELECT * FROM test_only;
    items = db.query(DBtestItem).all()
    return items

# ================= 5. 啟動 FastAPI 伺服器 =================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
