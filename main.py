from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import joblib
import numpy as np

app = FastAPI()

# Carregar modelo de embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Carregar modelo de cluster treinado
kmeans = joblib.load('kmeans_model.pkl')

class VagaInput(BaseModel):
    principais_atividades: str
    competencia_tecnicas_e_comportamentais: str

@app.post("/predict")
def predict(vaga: VagaInput):
    texto = f"{vaga.principais_atividades} {vaga.competencia_tecnicas_e_comportamentais}"
    embedding = model.encode([texto])
    cluster = kmeans.predict(embedding)
    return {"cluster": int(cluster[0])}
