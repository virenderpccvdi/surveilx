from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def notify_root():
    return {"message": "Notification service running!"}
