from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from .travel_agent import TravelAgent
from .tools import agent_tools

load_dotenv()

app = FastAPI(
    title="Agente de viagens",
    description="API para interagir com nosso agente pessoal de viagens",
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query:str

class AgentResponse(BaseModel):
    answer:str

agent = TravelAgent(provider="ollama", tool_list=agent_tools, model_name="llama3.2", verbose=False)

@app.get("/")
def home():
    return{"status":"O agente de viagens está no ar."}

@app.post("/api/ask-agent")
def ask_agent(request: QueryRequest):
    """Recebe uma query do usuário e processa pelo agente."""
    response = agent.ask(request.query)
    return {"Resposta":response}



