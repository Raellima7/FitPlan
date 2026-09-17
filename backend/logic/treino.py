# -*- coding: utf-8 -*-
"""
Lógica de geração de rotina de treino semanal (5 dias).

A divisão de grupos musculares por dia é fixa (modelo clássico "ABCDE"),
mas o número de séries/repetições/descanso de cada exercício muda de
acordo com o objetivo do usuário:

- emagrecimento     -> mais repetições, menos descanso (foco metabólico)
- ganho_de_massa    -> mais séries, repetições moderadas, mais descanso
- condicionamento   -> circuitos, repetições altas, pouco descanso
- manutencao        -> parâmetros equilibrados

A estrutura de cada exercício já contempla campos para nível de
dificuldade, descrição de execução e espaço para vídeo/imagem futuramente.
"""

from backend.data.exercicios import EXERCICIOS

OBJETIVOS_VALIDOS = ["emagrecimento", "ganho_de_massa", "condicionamento", "manutencao"]

# Parâmetros de séries/reps/descanso por objetivo
PARAMETROS_POR_OBJETIVO = {
    "ganho_de_massa": {"series": 4, "repeticoes": "8-10", "descanso": "60-90s"},
    "emagrecimento": {"series": 3, "repeticoes": "15-20", "descanso": "30-45s"},
    "condicionamento": {"series": 3, "repeticoes": "12-15", "descanso": "30-40s"},
    "manutencao": {"series": 3, "repeticoes": "10-12", "descanso": "45-60s"},
}

# Divisão semanal fixa (grupos musculares por dia)
DIVISAO_SEMANAL = [
    {"dia": "Segunda-feira", "titulo": "Peito + Tríceps", "grupos": ["peito", "triceps"]},
    {"dia": "Terça-feira", "titulo": "Costas + Bíceps", "grupos": ["costas", "biceps"]},
    {"dia": "Quarta-feira", "titulo": "Pernas", "grupos": ["pernas"]},
    {"dia": "Quinta-feira", "titulo": "Ombros + Abdômen", "grupos": ["ombros", "abdomen"]},
    {"dia": "Sexta-feira", "titulo": "Treino complementar", "grupos": ["corpo_todo", "cardio", "abdomen"]},
]


def _montar_exercicios_do_dia(grupos, parametros, objetivo, limite_por_grupo=3):
    exercicios_dia = []
    for grupo in grupos:
        lista_grupo = EXERCICIOS.get(grupo, [])
        # No treino "complementar" (Sexta) pegamos só 1-2 de cada grupo extra
        limite = 2 if grupo in ("cardio", "corpo_todo", "abdomen") else limite_por_grupo
        for exercicio in lista_grupo[:limite]:
            exercicios_dia.append({
                "nome": exercicio["nome"],
                "grupo_muscular": exercicio["grupo"],
                "series": parametros["series"],
                "repeticoes": parametros["repeticoes"],
                "descanso": parametros["descanso"],
                "descricao_execucao": exercicio["descricao"],
                "nivel_dificuldade": exercicio["nivel"],
                # Campos preparados para o futuro:
                "video_url": exercicio.get("video_url"),
                "imagem_url": exercicio.get("imagem_url"),
            })
    return exercicios_dia


def gerar_treino(objetivo: str):
    """
    Gera a rotina de treino semanal (5 dias) de acordo com o objetivo.

    Retorna um dicionário com o objetivo e a lista dos 5 dias,
    cada um com título, grupos musculares e exercícios detalhados.
    """
    if objetivo not in PARAMETROS_POR_OBJETIVO:
        objetivo = "manutencao"

    parametros = PARAMETROS_POR_OBJETIVO[objetivo]

    semana = []
    for dia_info in DIVISAO_SEMANAL:
        exercicios_dia = _montar_exercicios_do_dia(dia_info["grupos"], parametros, objetivo)
        semana.append({
            "dia": dia_info["dia"],
            "titulo": dia_info["titulo"],
            "exercicios": exercicios_dia,
        })

    return {
        "objetivo": objetivo,
        "parametros_gerais": parametros,
        "semana": semana,
    }
