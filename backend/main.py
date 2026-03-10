from fastapi import FastAPI

app = FastAPI()

@app.get("")
def read_root():
    return {"Hello": "World"}

# Google Vision API integration would go here
