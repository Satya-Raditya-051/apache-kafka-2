from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict_model1")
def predict(input: UserInput):
    return {"model": 1, "result": "Prediksi A"}

@app.post("/predict_model2")
def predict2(input: UserInput):
    return {"model": 2, "result": "Prediksi B"}

@app.post("/cluster_model3")
def cluster(input: UserInput):
    return {"model": 3, "cluster": "Cluster 1"}
