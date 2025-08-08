from langchain_core import tool
from typing import Optional

@tool
def buscar_voos(
    origem: str,
    destino: str,
    data_de_ida: str,
    data_de_volta: Optional[str]
) -> str:
    """
    Busca voos baseados na origem, destino data de ida e opcionalmente a data de volta
    Retorna informações simuladas de voos encontrados.
    """
    if data_de_volta:
        return f"Simulação de VOO: Encontrado voo de ida e volta de {origem} para {destino} em {data_de_ida} até {data_de_volta}."
    return f"Simulação de VOO: Encontrado voo de ida de {origem} para {destino} na data {data_de_ida}."

@tool
def buscar_hoteis(
    local: str,
    data_de_checkin: str,
    data_de_checkout: str
) -> str:
    """
    Busca por hotéis em um determinaldo local e período
    Retorna uma lista simulada de hotéis disponíveis.
    """

    return f"Encontrados 3 hotéis em {local} de {data_de_checkin} até {data_de_checkout}"


agent_tools = [buscar_voos, buscar_hoteis]