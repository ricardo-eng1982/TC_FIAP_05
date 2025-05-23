import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import joblib

# Abrir o arquivo JSON
with open('vagas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

rows = []
for id_vaga, vaga in data.items():
    base = vaga.get('informacoes_basicas', {})
    perfil = vaga.get('perfil_vaga', {})
    beneficios = vaga.get('beneficios', {})
    row = {**base, **perfil, **beneficios}
    row['id_vaga'] = id_vaga
    rows.append(row)

df = pd.DataFrame(rows)
df['texto_completo'] = df['principais_atividades'].fillna('') + ' ' + df['competencia_tecnicas_e_comportamentais'].fillna('')

# Embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(df['texto_completo'].tolist())

# Treinar KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(embeddings)

# Salvar modelo
joblib.dump(kmeans, 'kmeans_model.pkl')
