# 🌿 FitPlan — MVP

Monte sua rotina de alimentação e treino de acordo com seus objetivos.

Projeto de portfólio: plataforma web para geração de sugestões de dieta e
rotinas de treino, com base em dados simples informados pelo usuário
(peso e objetivo). Construído com **Python + Flask** no backend e
**HTML/CSS/JS** no frontend, com banco de dados **SQLite**.

> ⚠️ As sugestões geradas são **educacionais** e não substituem a avaliação
> de um(a) nutricionista, médico(a) ou profissional de educação física.

---

## 📁 Estrutura do projeto

```
fitplan/
├── app.py                      # Aplicação Flask (rotas principais)
├── requirements.txt            # Dependências do projeto
├── backend/
│   ├── data/
│   │   ├── alimentos.py        # Base de alimentos pré-cadastrada
│   │   └── exercicios.py       # Base de exercícios pré-cadastrada
│   ├── logic/
│   │   ├── dieta.py            # Lógica de geração da dieta
│   │   └── treino.py           # Lógica de geração do treino
│   └── database/
│       ├── db.py                # Conexão e funções do SQLite
│       └── fitplan.db           # Banco de dados (criado automaticamente)
├── templates/                   # Páginas HTML (Jinja2)
│   ├── base.html
│   ├── home.html
│   ├── dieta.html
│   ├── treino.html
│   ├── resultado_dieta.html
│   └── resultado_treino.html
└── static/
    ├── css/style.css            # Estilo visual (moderno, saúde/academia)
    └── js/script.js             # Menu mobile
```

---

## 🚀 Como executar

1. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python app.py
   ```

4. **Acesse no navegador:**
   ```
   http://127.0.0.1:5000
   ```

O banco de dados SQLite (`backend/database/fitplan.db`) é criado
automaticamente na primeira execução — não é preciso configurar nada.

---

## 🧭 Páginas disponíveis (MVP)

| Página              | Rota                | Descrição                                      |
|---------------------|----------------------|-------------------------------------------------|
| Home                | `/`                  | Apresentação do projeto e botões principais     |
| Dieta               | `/dieta`             | Formulário: peso, objetivo e dias da semana     |
| Resultado da dieta  | `/resultado-dieta`   | Cardápio semanal sugerido                       |
| Treino              | `/treino`            | Formulário: objetivo do treino                  |
| Resultado do treino | `/resultado-treino`  | Rotina de treino de 5 dias                      |

---

## 🥗 Como funciona a geração de dieta

Arquivo: `backend/logic/dieta.py`

1. Calcula-se uma meta calórica simplificada: `peso (kg) × fator do objetivo`
   - Emagrecimento: 24 kcal/kg
   - Manutenção: 30 kcal/kg
   - Ganho de massa: 35 kcal/kg
2. Um cardápio-modelo (pensado para 2000 kcal/dia) é escalado
   proporcionalmente até a meta calórica do usuário.
3. O cardápio é repetido pelo número de dias solicitado (1 a 7).

Essa lógica é propositalmente simples para o MVP. A estrutura já está
preparada para, no futuro, considerar altura, idade, sexo e calcular
macronutrientes (proteínas, carboidratos e gorduras) com mais precisão.

## 🏋️ Como funciona a geração de treino

Arquivo: `backend/logic/treino.py`

- A divisão semanal é fixa (modelo clássico):
  Segunda: Peito + Tríceps · Terça: Costas + Bíceps · Quarta: Pernas ·
  Quinta: Ombros + Abdômen · Sexta: Treino complementar.
- Series, repetições e descanso variam de acordo com o objetivo escolhido
  (ganho de massa, emagrecimento, condicionamento ou manutenção).
- Cada exercício já contém campos para nível de dificuldade, descrição de
  execução e espaço reservado para vídeo/imagem (a serem usados no futuro).

---

## 🧪 Como testar

- Acesse `/dieta`, preencha peso (ex.: `75`), selecione um objetivo e a
  quantidade de dias, e clique em **"Gerar minha dieta"** — a página de
  resultado deve mostrar o cardápio para cada dia solicitado.
- Acesse `/treino`, selecione um objetivo e clique em **"Gerar meu
  treino"** — a página de resultado deve mostrar os 5 dias com exercícios,
  séries, repetições e descanso.
- Teste em uma janela estreita do navegador (ou no celular) para conferir
  a responsividade do layout e o menu mobile (ícone ☰).

---

## 🗺️ Roadmap (funcionalidades futuras)

Login e cadastro · Histórico de dietas e treinos · Cálculo de calorias e
macronutrientes · Mais objetivos, alimentos e exercícios · Imagens e vídeos
dos exercícios · Dashboard do usuário · Integração com APIs · Acompanhamento
de evolução (peso/medidas) · Gráficos de progresso · Personalização com IA ·
Evolução para modelo SaaS.
