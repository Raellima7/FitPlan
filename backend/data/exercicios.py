# -*- coding: utf-8 -*-
"""
Base de exercícios pré-cadastrada, organizada por grupo muscular.

Cada exercício já nasce com uma estrutura pensada para o futuro
(descrição da execução, nível de dificuldade, campo para imagem/vídeo),
mesmo que no MVP a gente não exiba tudo isso na tela ainda.
"""

EXERCICIOS = {
    "peito": [
        {"nome": "Supino reto (barra ou halteres)", "grupo": "Peito", "descricao": "Deitado no banco, empurre a carga para cima até estender os braços, controlando a descida.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Supino inclinado", "grupo": "Peito", "descricao": "Banco inclinado a 30-45°, foco na porção superior do peitoral.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Crucifixo (halteres ou máquina)", "grupo": "Peito", "descricao": "Movimento de abertura e fechamento dos braços, com leve flexão no cotovelo.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Flexão de braço", "grupo": "Peito", "descricao": "Apoiado nas mãos e pés, desça o corpo controlando o tronco alinhado.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
    ],
    "triceps": [
        {"nome": "Tríceps corda (polia)", "grupo": "Tríceps", "descricao": "Puxe a corda para baixo estendendo o cotovelo, mantendo o braço fixo.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Tríceps testa (barra ou halteres)", "grupo": "Tríceps", "descricao": "Deitado, flexione e estenda os cotovelos levando a carga próxima à testa.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Mergulho no banco (dips)", "grupo": "Tríceps", "descricao": "Apoie as mãos no banco atrás do corpo e flexione os cotovelos descendo o quadril.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
    "costas": [
        {"nome": "Puxada frontal (polia)", "grupo": "Costas", "descricao": "Puxe a barra em direção ao peito, contraindo as escápulas.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Remada baixa (polia)", "grupo": "Costas", "descricao": "Puxe o cabo em direção ao abdômen mantendo a coluna ereta.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Remada curvada (barra)", "grupo": "Costas", "descricao": "Tronco inclinado à frente, puxe a barra em direção ao abdômen.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Pulldown unilateral", "grupo": "Costas", "descricao": "Puxada de um braço por vez, focando na ativação isolada do dorsal.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
    "biceps": [
        {"nome": "Rosca direta (barra)", "grupo": "Bíceps", "descricao": "Flexione os cotovelos elevando a barra, sem balançar o tronco.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Rosca alternada (halteres)", "grupo": "Bíceps", "descricao": "Flexione um braço de cada vez, girando o punho ao final do movimento.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Rosca martelo", "grupo": "Bíceps", "descricao": "Rosca com pegada neutra, focando em bíceps e antebraço.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
    ],
    "pernas": [
        {"nome": "Agachamento livre ou guiado", "grupo": "Pernas", "descricao": "Desça flexionando quadril e joelhos, mantendo o tronco estável.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Leg press", "grupo": "Pernas", "descricao": "Empurre a plataforma estendendo os joelhos, sem travar totalmente.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Cadeira extensora", "grupo": "Pernas", "descricao": "Estenda os joelhos contra a resistência, controlando a volta.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Mesa flexora", "grupo": "Pernas", "descricao": "Flexione os joelhos trazendo o calcanhar em direção ao glúteo.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Stiff (halteres ou barra)", "grupo": "Pernas/Posterior", "descricao": "Desça o tronco mantendo as pernas semi-estendidas, sentindo o alongamento posterior.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Panturrilha em pé", "grupo": "Panturrilha", "descricao": "Eleve os calcanhares o máximo possível e desça controlando.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
    ],
    "ombros": [
        {"nome": "Desenvolvimento com halteres", "grupo": "Ombros", "descricao": "Empurre os halteres para cima até estender os braços acima da cabeça.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Elevação lateral", "grupo": "Ombros", "descricao": "Eleve os braços lateralmente até a altura dos ombros.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Elevação frontal", "grupo": "Ombros", "descricao": "Eleve os braços à frente do corpo até a altura dos ombros.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Remada alta", "grupo": "Ombros", "descricao": "Puxe a barra verticalmente até a altura do peito, cotovelos para cima.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
    "abdomen": [
        {"nome": "Abdominal supra", "grupo": "Abdômen", "descricao": "Flexione o tronco em direção aos joelhos, sem puxar o pescoço.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Prancha isométrica", "grupo": "Abdômen", "descricao": "Mantenha o corpo alinhado apoiado nos antebraços e pontas dos pés.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "Elevação de pernas", "grupo": "Abdômen", "descricao": "Deitado, eleve as pernas estendidas até 90° e desça controlando.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
    "cardio": [
        {"nome": "Esteira ou bicicleta (moderado)", "grupo": "Cardio", "descricao": "Ritmo moderado e constante, mantendo a respiração controlada.", "nivel": "Iniciante", "video_url": None, "imagem_url": None},
        {"nome": "HIIT (intervalado)", "grupo": "Cardio", "descricao": "Alternância entre picos de intensidade alta e recuperação ativa.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
    "corpo_todo": [
        {"nome": "Circuito funcional", "grupo": "Corpo todo", "descricao": "Sequência de exercícios com pouco descanso entre eles, unindo força e cardio.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
        {"nome": "Burpee", "grupo": "Corpo todo", "descricao": "Agachar, jogar as pernas para trás em prancha, voltar e saltar.", "nivel": "Intermediário", "video_url": None, "imagem_url": None},
    ],
}
