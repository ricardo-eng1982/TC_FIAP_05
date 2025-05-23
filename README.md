# Sistema de Recomendação de Vagas - TC FIAP 05

Sistema inteligente de recomendação de vagas de emprego utilizando Machine Learning com algoritmo K-Means para clustering e análise de similaridade.

## 📋 Sobre o Projeto

Este projeto implementa um sistema de recomendação que analisa vagas de emprego e sugere as mais adequadas baseadas em critérios como localização, salário, tecnologias e outros fatores relevantes. Utiliza algoritmos de clustering para agrupar vagas similares e facilitar a busca.

## 🚀 Funcionalidades

- **Clustering de Vagas**: Agrupa vagas similares usando K-Means
- **Sistema de Recomendação**: Sugere vagas baseadas em perfil do usuário
- **API REST**: Interface para consulta e recomendações
- **Containerização**: Deploy facilitado com Docker
- **Análise de Dados**: Processamento e análise de datasets de vagas

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Scikit-learn** - Machine Learning
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Flask/FastAPI** - API REST
- **Docker** - Containerização
- **JSON** - Armazenamento de dados

## 📦 Estrutura do Projeto

```
TC_5-FIAP/
├── main.py              # Aplicação principal
├── train.py             # Script de treinamento do modelo
├── requirements.txt     # Dependências Python
├── Dockerfile          # Configuração Docker
├── vagas.json          # Dataset completo de vagas
├── vagas_small.json    # Dataset reduzido para testes
├── kmeans_model.pkl    # Modelo treinado (gerado)
└── README.md           # Documentação
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip
- Docker (opcional)

### Instalação Local

1. **Clone o repositório:**
```bash
git clone https://github.com/ricardo-eng1982/TC_FIAP_05.git
cd TC_5-FIAP
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Treine o modelo:**
```bash
python train.py
```

5. **Execute a aplicação:**
```bash
python main.py
```

### Instalação com Docker

1. **Build da imagem:**
```bash
docker build -t tc-fiap-05 .
```

2. **Execute o container:**
```bash
docker run -p 8000:8000 tc-fiap-05
```

## 📊 Uso da API

### Endpoints Disponíveis

#### GET /vagas
Retorna todas as vagas disponíveis
```bash
curl http://localhost:8000/vagas
```

#### POST /recomendar
Solicita recomendações baseadas em critérios
```bash
curl -X POST http://localhost:8000/recomendar \
  -H "Content-Type: application/json" \
  -d '{"localizacao": "São Paulo", "salario_minimo": 5000}'
```

#### GET /clusters
Visualiza os clusters de vagas
```bash
curl http://localhost:8000/clusters
```

## 🤖 Como Funciona o Algoritmo

O sistema segue um pipeline completo de Machine Learning com as seguintes etapas:

### 1. 📊 Análise Exploratória
- **Exploração inicial dos dados**: Verificação da estrutura, tipos de dados e qualidade
- **Identificação de padrões**: Análise de distribuições salariais, localização mais comum
- **Detecção de outliers**: Identificação de valores extremos ou inconsistentes
- **Estatísticas descritivas**: Média, mediana, desvio padrão das variáveis numéricas
- **Análise de correlações**: Relacionamento entre diferentes variáveis

### 2. 🔧 Engenharia de Features - Geração de Embeddings
- **Processamento de texto**: Limpeza e normalização de títulos e descrições
- **Tokenização**: Quebra do texto em tokens relevantes
- **Vetorização TF-IDF**: Conversão de texto em representações numéricas
- **Encoding categórico**: Transformação de variáveis categóricas (localização, nível)
- **Normalização numérica**: Padronização de salários e outras variáveis numéricas
- **Feature Selection**: Seleção das características mais relevantes para o modelo

### 3. 🎯 Clusterização com K-Means
- **Determinação do K ótimo**: Utilização do método Elbow e Silhouette Score
- **Inicialização K-Means++**: Algoritmo otimizado para centróides iniciais
- **Treinamento iterativo**: Convergência até estabilização dos clusters
- **Validação dos clusters**: Análise da coesão intra-cluster e separação inter-cluster
- **Interpretação dos grupos**: Caracterização de cada cluster encontrado

### 4. 📈 Visualização com t-SNE
- **Redução de dimensionalidade**: Projeção dos dados de alta dimensão para 2D/3D
- **Preservação de estrutura local**: Manutenção de relações de proximidade
- **Visualização interativa**: Plots coloridos por cluster para interpretação
- **Análise de separabilidade**: Verificação visual da qualidade dos clusters
- **Identificação de padrões**: Descoberta de agrupamentos naturais nos dados

### 5. 🎯 Sistema de Recomendação
- **Cálculo de similaridade**: Distância euclidiana e cosine similarity
- **Ranking personalizado**: Ordenação baseada no perfil do usuário
- **Filtragem colaborativa**: Recomendações baseadas em clusters similares
- **Ajuste de pesos**: Priorização de critérios importantes (salário, localização)

### Parâmetros do Modelo
- **Número de Clusters**: 5-8 (determinado via análise exploratória)
- **Algoritmo**: K-Means++ com inicialização otimizada
- **Métricas de Avaliação**: Silhouette Score, Inertia, Davies-Bouldin Index
- **Dimensões t-SNE**: Perplexity=30, Learning Rate=200
- **Features Principais**: Salário, Localização, Skills, Senioridade

## 📈 Datasets

### vagas.json
Dataset completo com todas as vagas coletadas contendo:
- Título da vaga
- Empresa
- Localização
- Salário
- Tecnologias requeridas
- Descrição

### vagas_small.json
Versão reduzida para testes e desenvolvimento rápido.

## 🧪 Testes

Execute os testes unitários:
```bash
python -m pytest tests/
```

## 📝 Exemplos de Uso

### Exemplo 1: Busca por Localização
```python
import requests

response = requests.post('http://localhost:8000/recomendar', 
                        json={'localizacao': 'São Paulo'})
print(response.json())
```

### Exemplo 2: Filtro por Salário
```python
response = requests.post('http://localhost:8000/recomendar', 
                        json={'salario_minimo': 8000})
print(response.json())
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Ricardo de Souza Santos** - *Desenvolvimento inicial* - [ricardo-eng1982](https://github.com/ricardo-eng1982)

## Informações

- **Projeto**: [TC_FIAP_05](https://github.com/ricardo-eng1982/TC_FIAP_05)
- **Instituição**: FIAP - Faculdade de Informática e Administração Paulista

## 🔄 Roadmap

- [ ] Implementação de mais algoritmos de ML
- [ ] Interface web para visualização
- [ ] Integração com APIs de vagas reais
- [ ] Sistema de feedback dos usuários
- [ ] Deployment em cloud (AWS/Azure)

---

**Desenvolvido como parte do Trabalho de Conclusão - FIAP 2025**