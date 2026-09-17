# -*- coding: utf-8 -*-
"""
Base de alimentos pré-cadastrada.

Cada alimento tem informações nutricionais aproximadas por 100g/100ml
(kcal, proteína, carboidrato, gordura), para permitir evoluções futuras
(cálculo de macros, calorias totais etc.) sem precisar remodelar a estrutura.

unidade:
    "g"   -> quantidade pensada em gramas
    "un"  -> quantidade pensada em unidades (ex.: ovo, banana)
"""

ALIMENTOS = {
    # --- Cafés da manhã / lanches ---
    "pao_integral": {"nome": "Pão integral", "kcal_100": 250, "proteina_100": 9, "carbo_100": 45, "gordura_100": 3, "unidade": "g"},
    "ovo": {"nome": "Ovo", "kcal_100": 155, "proteina_100": 13, "carbo_100": 1, "gordura_100": 11, "unidade": "un", "peso_unidade": 50},
    "banana": {"nome": "Banana", "kcal_100": 89, "proteina_100": 1, "carbo_100": 23, "gordura_100": 0.3, "unidade": "un", "peso_unidade": 100},
    "aveia": {"nome": "Aveia em flocos", "kcal_100": 389, "proteina_100": 17, "carbo_100": 66, "gordura_100": 7, "unidade": "g"},
    "leite_desnatado": {"nome": "Leite desnatado", "kcal_100": 35, "proteina_100": 3.4, "carbo_100": 5, "gordura_100": 0.2, "unidade": "ml"},
    "iogurte_natural": {"nome": "Iogurte natural", "kcal_100": 61, "proteina_100": 3.5, "carbo_100": 4.7, "gordura_100": 3.3, "unidade": "g"},
    "queijo_branco": {"nome": "Queijo branco/minas", "kcal_100": 264, "proteina_100": 18, "carbo_100": 3, "gordura_100": 20, "unidade": "g"},
    "whey_protein": {"nome": "Whey protein (dose)", "kcal_100": 400, "proteina_100": 80, "carbo_100": 8, "gordura_100": 6, "unidade": "g"},
    "castanha": {"nome": "Castanha-do-pará", "kcal_100": 656, "proteina_100": 14, "carbo_100": 12, "gordura_100": 66, "unidade": "g"},
    "pasta_amendoim": {"nome": "Pasta de amendoim", "kcal_100": 588, "proteina_100": 25, "carbo_100": 20, "gordura_100": 50, "unidade": "g"},
    "fruta_variada": {"nome": "Fruta da estação (maçã, mamão, laranja...)", "kcal_100": 55, "proteina_100": 0.5, "carbo_100": 14, "gordura_100": 0.2, "unidade": "g"},

    # --- Almoço / jantar: proteínas ---
    "frango_grelhado": {"nome": "Peito de frango grelhado", "kcal_100": 165, "proteina_100": 31, "carbo_100": 0, "gordura_100": 3.6, "unidade": "g"},
    "carne_bovina_magra": {"nome": "Carne bovina magra (patinho)", "kcal_100": 187, "proteina_100": 28, "carbo_100": 0, "gordura_100": 8, "unidade": "g"},
    "tilapia": {"nome": "Filé de tilápia", "kcal_100": 128, "proteina_100": 26, "carbo_100": 0, "gordura_100": 2.7, "unidade": "g"},
    "ovo_cozido": {"nome": "Ovo cozido", "kcal_100": 155, "proteina_100": 13, "carbo_100": 1, "gordura_100": 11, "unidade": "un", "peso_unidade": 50},

    # --- Almoço / jantar: carboidratos ---
    "arroz_branco": {"nome": "Arroz branco cozido", "kcal_100": 130, "proteina_100": 2.7, "carbo_100": 28, "gordura_100": 0.3, "unidade": "g"},
    "arroz_integral": {"nome": "Arroz integral cozido", "kcal_100": 123, "proteina_100": 2.6, "carbo_100": 26, "gordura_100": 1, "unidade": "g"},
    "batata_doce": {"nome": "Batata-doce cozida", "kcal_100": 86, "proteina_100": 1.6, "carbo_100": 20, "gordura_100": 0.1, "unidade": "g"},
    "mandioca": {"nome": "Mandioca cozida", "kcal_100": 125, "proteina_100": 1, "carbo_100": 30, "gordura_100": 0.3, "unidade": "g"},
    "macarrao_integral": {"nome": "Macarrão integral cozido", "kcal_100": 124, "proteina_100": 5, "carbo_100": 25, "gordura_100": 1, "unidade": "g"},

    # --- Almoço / jantar: leguminosas e vegetais ---
    "feijao": {"nome": "Feijão cozido", "kcal_100": 76, "proteina_100": 5, "carbo_100": 14, "gordura_100": 0.5, "unidade": "g"},
    "lentilha": {"nome": "Lentilha cozida", "kcal_100": 116, "proteina_100": 9, "carbo_100": 20, "gordura_100": 0.4, "unidade": "g"},
    "legumes_variados": {"nome": "Legumes variados (cenoura, brócolis, abobrinha...)", "kcal_100": 35, "proteina_100": 2, "carbo_100": 7, "gordura_100": 0.3, "unidade": "g"},
    "salada_verde": {"nome": "Salada verde (alface, rúcula, agrião...)", "kcal_100": 15, "proteina_100": 1.3, "carbo_100": 2.9, "gordura_100": 0.2, "unidade": "g"},
    "azeite": {"nome": "Azeite de oliva", "kcal_100": 884, "proteina_100": 0, "carbo_100": 0, "gordura_100": 100, "unidade": "ml"},

    # --- Ceia / lanches leves ---
    "gelatina_diet": {"nome": "Gelatina diet", "kcal_100": 10, "proteina_100": 1.5, "carbo_100": 1, "gordura_100": 0, "unidade": "g"},
    "cottage": {"nome": "Queijo cottage", "kcal_100": 98, "proteina_100": 11, "carbo_100": 3.4, "gordura_100": 4.3, "unidade": "g"},
}
