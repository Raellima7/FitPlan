# -*- coding: utf-8 -*-
"""
Lógica de geração de sugestão de dieta.

IMPORTANTE (limitação assumida de propósito, para o MVP):
- Este é um cálculo SIMPLIFICADO e EDUCACIONAL, não substitui avaliação
  de um nutricionista ou profissional de saúde.
- A estimativa calórica usa apenas peso + objetivo (não usa altura, idade
  ou sexo, pois ainda não são coletados). A arquitetura está preparada
  para receber esses dados no futuro e refinar o cálculo (ex.: fórmulas
  de Harris-Benedict / Mifflin-St Jeor).

Como funciona hoje:
1. Estima-se um gasto calórico aproximado (kcal/dia) multiplicando o peso
   por um fator que depende do objetivo.
2. Um "cardápio-modelo" (template) é definido para 2000 kcal/dia, com
   alimentos e quantidades-base para cada refeição.
3. As quantidades desse modelo são escaladas proporcionalmente à meta
   calórica calculada para o usuário (regra de três simples).
4. O cardápio é repetido para a quantidade de dias solicitada, podendo
   futuramente variar as opções dia a dia (por ora, mesma estrutura).
"""

from backend.data.alimentos import ALIMENTOS

# Base calórica de referência do template abaixo (kcal/dia)
KCAL_BASE_TEMPLATE = 2000

# Fatores simplificados de kcal por kg de peso corporal, por objetivo
FATOR_KCAL_POR_KG = {
    "emagrecimento": 24,
    "manutencao": 30,
    "ganho_de_massa": 35,
}

OBJETIVOS_VALIDOS = list(FATOR_KCAL_POR_KG.keys())

# Template-base (para 2000 kcal/dia). Quantidades em g/ml/unidade.
# Cada item: (id_do_alimento, quantidade_base)
CARDAPIO_TEMPLATE = {
    "cafe_da_manha": [
        ("pao_integral", 50),
        ("ovo", 2),
        ("fruta_variada", 100),
    ],
    "lanche_da_manha": [
        ("iogurte_natural", 120),
        ("castanha", 15),
    ],
    "almoco": [
        ("frango_grelhado", 150),
        ("arroz_integral", 100),
        ("feijao", 80),
        ("legumes_variados", 100),
        ("salada_verde", 50),
        ("azeite", 10),
    ],
    "lanche_da_tarde": [
        ("pao_integral", 30),
        ("pasta_amendoim", 15),
        ("banana", 1),
    ],
    "jantar": [
        ("tilapia", 130),
        ("batata_doce", 120),
        ("legumes_variados", 100),
        ("salada_verde", 50),
    ],
    "ceia": [
        ("cottage", 100),
    ],
}

NOMES_REFEICOES = {
    "cafe_da_manha": "Café da manhã",
    "lanche_da_manha": "Lanche da manhã",
    "almoco": "Almoço",
    "lanche_da_tarde": "Lanche da tarde",
    "jantar": "Jantar",
    "ceia": "Antes de dormir (opcional)",
}


def calcular_meta_calorica(peso_kg: float, objetivo: str) -> float:
    """Estima uma meta calórica diária simplificada."""
    fator = FATOR_KCAL_POR_KG.get(objetivo, FATOR_KCAL_POR_KG["manutencao"])
    return round(peso_kg * fator)


def _formatar_quantidade(alimento_id: str, quantidade_escalada: float):
    """Formata a quantidade final para exibição, respeitando a unidade do alimento."""
    alimento = ALIMENTOS[alimento_id]
    unidade = alimento["unidade"]

    if unidade == "un":
        # Nunca deixa cair pra 0 unidades; arredonda para o inteiro mais próximo (mín. 1)
        qtd = max(1, round(quantidade_escalada))
        texto = f"{qtd} un"
    elif unidade == "ml":
        qtd = max(5, round(quantidade_escalada / 5) * 5)  # arredonda em passos de 5ml
        texto = f"{qtd} ml"
    else:  # "g"
        qtd = max(5, round(quantidade_escalada / 5) * 5)  # arredonda em passos de 5g
        texto = f"{qtd} g"

    return qtd, texto


def montar_cardapio_do_dia(fator_escala: float):
    """Monta um dia de cardápio já escalado pela meta calórica do usuário."""
    dia = []
    for refeicao_id, itens in CARDAPIO_TEMPLATE.items():
        itens_formatados = []
        for alimento_id, quantidade_base in itens:
            alimento = ALIMENTOS[alimento_id]
            quantidade_escalada = quantidade_base * fator_escala
            qtd_num, qtd_texto = _formatar_quantidade(alimento_id, quantidade_escalada)
            itens_formatados.append({
                "nome": alimento["nome"],
                "quantidade": qtd_texto,
                "quantidade_valor": qtd_num,
            })
        dia.append({
            "id": refeicao_id,
            "nome": NOMES_REFEICOES[refeicao_id],
            "itens": itens_formatados,
        })
    return dia


def gerar_dieta(peso_kg: float, objetivo: str, dias_semana: int):
    """
    Gera a sugestão completa de dieta para a semana.

    Retorna um dicionário com a meta calórica estimada e a lista de dias,
    cada um contendo as refeições e os alimentos com quantidade.
    """
    meta_kcal = calcular_meta_calorica(peso_kg, objetivo)
    fator_escala = meta_kcal / KCAL_BASE_TEMPLATE

    dias_semana = max(1, min(7, int(dias_semana)))

    plano_semanal = []
    for numero_dia in range(1, dias_semana + 1):
        plano_semanal.append({
            "dia_numero": numero_dia,
            "refeicoes": montar_cardapio_do_dia(fator_escala),
        })

    return {
        "meta_kcal_estimada": meta_kcal,
        "objetivo": objetivo,
        "dias_semana": dias_semana,
        "plano_semanal": plano_semanal,
    }
