# 🚀 Sistema Inteligente de Gerenciamento da Colônia
## 📖 Descrição do Projeto

Este projeto é a **Fase 3** da Missão Aurora Siger, cujo objetivo é simular o funcionamento inteligente de uma colônia permanente em Marte. Após o pouso e a estabilização da base (fases anteriores), o desafio agora é **manter a colônia operando de forma autônoma e eficiente**.

O sistema integra quatro módulos principais:

1. **Organização de dados** — estruturas em lista e dicionário hierárquico
2. **Previsão energética** — regressão linear simples (vento → geração eólica)
3. **Análise de energia** — comparação entre geração e consumo
4. **Decisões automáticas** — regras lógicas com priorização de sistemas essenciais

---

## 🧠 Conceitos Aplicados

| Conceito | Aplicação no sistema |
|---|---|
| Dicionários (chave-valor) | Armazenamento dos dados da colônia |
| Estrutura hierárquica | sistema → subsistema → valor |
| `if / elif / else` | Regras de decisão e alertas |
| Operadores `and` / `or` | Condições combinadas (bateria baixa E consumo alto) |
| Regressão linear simples | Previsão de geração eólica a partir do vento |
| Funções Python | Separação clara entre dados, lógica e decisões |

---

## ⚙️ Como Executar

### 1. Requisitos
Apenas Python 3 instalado. Nenhuma biblioteca externa é necessária.

### 2. Executar
```bash
python colonia_aurora.py
```

---

## 📥 Exemplos de Entrada e Saída

### Exemplo 1 — Situação normal (dados padrão)

**Entrada (definida no código):**
```
geração solar   = 45 kW
velocidade vento = 11 m/s  →  geração eólica prevista ≈ 28.3 kW
consumo total   = 70 kW
carga bateria   = 72%
```

**Saída:**
```
Geração total      : 73.3 kW
Consumo total      : 70.0 kW
Saldo              : +3.3 kW
✔  OK: geração suficiente para o consumo atual.
→ Manter operação normal em todos os módulos.
```

---

### Exemplo 2 — Consumo maior que geração (situação de alerta)

**Entrada:**
```
geração solar   = 40 kW
geração eólica  = 10 kW  →  total = 50 kW
consumo total   = 70 kW
carga bateria   = 45%
```

**Saída:**
```
Saldo              : -20 kW
⚠  ALERTA: consumo maior que geração.
→ Suspender módulos não essenciais temporariamente.
```

---

### Exemplo 3 — Energia excedente

**Entrada:**
```
geração total   = 90 kW
consumo total   = 35 kW
```

**Saída:**
```
Saldo              : +55 kW
✔  SUGESTÃO: geração excedente significativa.
→ Armazenar energia nas baterias.
```

---

### Exemplo 4 — Previsão eólica (regressão)

**Entrada:**
```
vento = 11 m/s
```

**Saída:**
```
Equação ajustada  : geração = 3.04 × vento + (-5.07)
Previsão          : geração ≈ 28.3 kW
```

---

## 🗂️ Estrutura do Código

```
colonia_aurora.py
│
├── MÓDULO 1 — Dados da Colônia
│   ├── inicializar_colonia()    → dicionário hierárquico com todos os dados
│   └── exibir_estrutura()       → exibe dados organizados por sistema
│
├── MÓDULO 2 — Previsão Energética
│   ├── calcular_regressao_linear()  → calcula coeficientes a e b da reta
│   └── prever_geracao_eolica()      → estima geração a partir do vento
│
├── MÓDULO 3 — Análise de Energia
│   └── analisar_energia()       → compara geração vs consumo, emite diagnóstico
│
├── MÓDULO 4 — Decisões Automáticas
│   └── tomar_decisao()          → aplica regras lógicas e prioriza sistemas
│
└── MÓDULO 5 — Execução Principal
    └── executar_sistema()       → integra todos os módulos em sequência
```

---

## 🌱 Objetivo Final

Ao executar o sistema, a colônia Aurora Siger é capaz de:

- Organizar seus dados de forma estruturada e hierárquica
- Prever comportamentos futuros com base em dados históricos
- Identificar riscos energéticos e tomar decisões automáticas
- Garantir sempre o funcionamento dos sistemas essenciais à vida

---

## 🔗 Repositórios das Fases Anteriores

| Fase | Descrição | Link |
|---|---|---|
| Fase 1 | Simulação de decolagem e telemetria | [atividade_integradora](https://github.com/timsleo/atividade_integradora) |
| Fase 2 | Gerenciamento de pouso e estabilização | [mgpeb](https://github.com/timsleo/mgpeb) |
| Fase 3 | Sistema inteligente da colônia | *(este repositório)* |
