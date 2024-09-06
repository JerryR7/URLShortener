from fastapi import FastAPI
from app.api.routes import short_url
from app.config import Config

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the URL Shortener API"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(short_url.router, prefix="/api/v1")

# 如果有其他初始化步驟，這裡可以添加
@app.on_event("startup")
async def startup_event():
    from app.infrastructure.database import setup_database
    setup_database()
    if Config.DEBUG:
        print("Application is running in DEBUG mode")

# 如果需要，也可以定義應用的關閉事件
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down application...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)