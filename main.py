from fastapi import FastAPI
from pydantic import BaseModel, Field
from mimath import calcular_z

app = FastAPI(
  title ="Simple Math API",
  description = "Takes two numbers (x,y) and returns some z calculation.",
  version="1.0.0"
)

# Request Model

class CalcRequest(BaseModel):
  x: float = Field(...,description="First number")
  y:float = Field(...,description="Second number")

@app.post("/calc")
def calc(req:CalcRequest):
  result = calcular_z(req.x,req.y)
  return {
    "inputs":{"x":req.x,"y":req.y},
    "result":result
  }

@app.get("/")
def home():
  return {"message": "Our API is ready!"}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)