# -*- coding: utf-8 -*-
"""
FitPlan - Aplicação principal (MVP)

Monte sua rotina de alimentação e treino de acordo com seus objetivos.

Como executar:
    1. pip install -r requirements.txt
    2. python app.py
    3. Acesse http://127.0.0.1:5000 no navegador

Rotas:
    /                -> Home
    /dieta           -> Formulário para gerar dieta
    /resultado-dieta -> Resultado da dieta (POST do formulário)
    /treino          -> Formulário para gerar treino
    /resultado-treino-> Resultado do treino (POST do formulário)
"""

from flask import Flask, render_template, request, redirect, url_for, flash

from backend.database.db import inicializar_banco, salvar_solicitacao_dieta, salvar_solicitacao_treino
from backend.logic.dieta import gerar_dieta, OBJETIVOS_VALIDOS as OBJETIVOS_DIETA
from backend.logic.treino import gerar_treino, OBJETIVOS_VALIDOS as OBJETIVOS_TREINO

app = Flask(__name__)
app.secret_key = "chave-de-desenvolvimento-fitplan"  # apenas para uso local/MVP

# Garante que o banco e as tabelas existam ao subir a aplicação
inicializar_banco()


# ---------------------------------------------------------------------------
# Rotas de navegação principal
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------------------------------------------------------------------
# Fluxo de Dieta
# ---------------------------------------------------------------------------

@app.route("/dieta", methods=["GET"])
def dieta_formulario():
    return render_template("dieta.html", objetivos=OBJETIVOS_DIETA)


@app.route("/resultado-dieta", methods=["POST"])
def resultado_dieta():
    try:
        peso = float(request.form.get("peso", "").replace(",", "."))
        altura_str = request.form.get("altura", "").replace(",", ".").strip()
        altura = float(altura_str) if altura_str else None
        objetivo = request.form.get("objetivo")
        dias_semana = int(request.form.get("dias_semana", 5))
    except (ValueError, TypeError):
        flash("Por favor, preencha os dados corretamente.")
        return redirect(url_for("dieta_formulario"))

    if peso <= 0 or peso > 400:
        flash("Informe um peso válido.")
        return redirect(url_for("dieta_formulario"))

    if altura is not None and (altura <= 0 or altura > 260):
        flash("Informe uma altura válida, em centímetros (ex.: 170).")
        return redirect(url_for("dieta_formulario"))

    if objetivo not in OBJETIVOS_DIETA:
        flash("Selecione um objetivo válido.")
        return redirect(url_for("dieta_formulario"))

    if dias_semana < 1 or dias_semana > 7:
        dias_semana = 7

    resultado = gerar_dieta(peso, objetivo, dias_semana, altura_cm=altura)

    # Salva o registro da solicitação no banco (base para histórico futuro)
    salvar_solicitacao_dieta(
        peso, objetivo, dias_semana, resultado["meta_kcal_estimada"],
        altura=altura, imc=resultado["imc"],
    )

    return render_template("resultado_dieta.html", resultado=resultado, peso=peso)


# ---------------------------------------------------------------------------
# Fluxo de Treino
# ---------------------------------------------------------------------------

@app.route("/treino", methods=["GET"])
def treino_formulario():
    return render_template("treino.html", objetivos=OBJETIVOS_TREINO)


@app.route("/resultado-treino", methods=["POST"])
def resultado_treino():
    objetivo = request.form.get("objetivo")

    if objetivo not in OBJETIVOS_TREINO:
        flash("Selecione um objetivo válido.")
        return redirect(url_for("treino_formulario"))

    resultado = gerar_treino(objetivo)

    # Salva o registro da solicitação no banco (base para histórico futuro)
    salvar_solicitacao_treino(objetivo)

    return render_template("resultado_treino.html", resultado=resultado)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
