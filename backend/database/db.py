# -*- coding: utf-8 -*-
"""
Módulo de acesso ao banco de dados SQLite.

No MVP, o banco guarda um registro simples de cada solicitação de dieta
e de treino (sem login/usuário, já que ainda não existe autenticação).
Isso já deixa a base pronta para, no futuro, virar "histórico do usuário"
quando o login for implementado (bastaria adicionar uma coluna usuario_id).
"""

import sqlite3
import os
from datetime import datetime

CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "fitplan.db")


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    """Cria as tabelas do banco de dados, caso ainda não existam."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitacoes_dieta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            peso REAL NOT NULL,
            altura REAL,
            objetivo TEXT NOT NULL,
            dias_semana INTEGER NOT NULL,
            meta_kcal_estimada REAL,
            imc REAL,
            criado_em TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitacoes_treino (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            objetivo TEXT NOT NULL,
            criado_em TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_solicitacao_dieta(peso, objetivo, dias_semana, meta_kcal_estimada, altura=None, imc=None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """INSERT INTO solicitacoes_dieta (peso, altura, objetivo, dias_semana, meta_kcal_estimada, imc, criado_em)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (peso, altura, objetivo, dias_semana, meta_kcal_estimada, imc, datetime.now().isoformat()),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id


def salvar_solicitacao_treino(objetivo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """INSERT INTO solicitacoes_treino (objetivo, criado_em)
           VALUES (?, ?)""",
        (objetivo, datetime.now().isoformat()),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id
