from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import agent_tools

class TravelAgent:
    def __init__(self, tool_list: list, provider: str = "ollama", model_name: str = "llama3", verbose: bool = True):
        """
        Inicializa o agente de viagens
        Args:
            tool_list (list): lista de funções chamáveis pelo agente
            provider   (str): provedor do llm (ollama, openai, google, etc...)
            model_name (str): nome do modelo a ser invocado.
            verbose   (bool): indica se o agente deve exibir os passos intermediários do processo.
        """
        self.provider = provider
        self.model_name    = model_name
        
        self.llm      = self._get_llm()
        self.tool_list = tool_list
        self.verbose = verbose

        self.agent_executor = self._create_agent_executor()
    
    def _get_llm(self):
        """Seleciona e instancia a llm de acordo com o provedor e modelo do construtor"""
        if self.provider == "ollama":
            return ChatOllama(model=self.model_name, temperature=0.3)
        else:
            raise("só temos ollama por enquanto, depois modificaremos")

    def _create_agent_executor(self):
        "Método para montar o prompt, agente e o executor."

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Você é um agente de viagens prestativo. Seu objetivo é ajudar o usuário a planejar suas viagens usando as ferramentas disponíveis."),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}")
            ]
        )

        agent = create_tool_calling_agent(self.llm, tools=self.tool_list, prompt=prompt)

        return AgentExecutor(agent=agent, tools=self.tool_list, verbose=self.verbose)
    

    def ask(self, query:str) -> str:
        response = self.agent_executor.invoke({"input":query})

        return response["output"]


if __name__ == "__main__":
    agent = TravelAgent(tool_list=agent_tools, provider="ollama", model_name="llama3.2", verbose=False)

    query1 = "Eu quero buscar um voo de São Paulo para Natal para o dia 25 de Dezembro de 2025."
    response1 = agent.ask(query1)
    print("\nResposta Final:")
    print(response1)

    query2 = "Olá, preciso de um voo de Curitiba para o Rio de Janeiro no dia 10 de Setembro de 2025 e voltando dia 20. Também quero ver hotéis por lá para essas datas."
    response2 = agent.ask(query2)
    print("\nResposta Final:")
    print(response2)


