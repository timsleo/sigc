# ============================================================
#   MISSÃO AURORA SIGER — FASE 3
#   Sistema Inteligente de Gerenciamento da Colônia em Marte
# ============================================================
# Disciplinas integradas:
#   - Estruturas de dados (listas, dicionários, hierarquias)
#   - Lógica computacional (if / elif / else)
#   - Modelagem matemática (regressão linear simples)
#   - Análise energética
# ============================================================


# ============================================================
# MÓDULO 1 — DADOS DA COLÔNIA
# Organização em dicionário (chave-valor) e hierarquia
# ============================================================

def inicializar_colonia():
    """
    Retorna a estrutura de dados da colônia Aurora Siger.
    Organizada em dicionário hierárquico: sistema → subsistema → valor.
    """
    colonia = {
        "nome": "Aurora Siger",
        "sistema_energetico": {
            "solar": {
                "geracao_kw": 45.0,
                "paineis_ativos": True
            },
            "eolico": {
                "velocidade_vento_ms": 11.0,
                "geracao_kw": 0.0      # será calculada pela regressão
            },
            "bateria": {
                "carga_percentual": 72.0,
                "capacidade_kwh": 200.0
            }
        },
        "sistema_ambiental": {
            "temperatura_interna_c": 22.0,
            "temperatura_externa_c": -55.0,
            "pressao_atm": 0.006
        },
        "sistema_operacional": {
            "consumo_total_kw": 70.0,
            "suporte_vida": True,
            "modulos": {
                "habitacao": {"consumo_kw": 20.0, "essencial": True},
                "pesquisa":  {"consumo_kw": 15.0, "essencial": False},
                "comunicacao": {"consumo_kw": 10.0, "essencial": True},
                "mobilidade": {"consumo_kw": 15.0, "essencial": False},
                "producao_alimento": {"consumo_kw": 10.0, "essencial": True}
            }
        }
    }
    return colonia


def exibir_estrutura(colonia):
    """
    Exibe os dados da colônia de forma organizada e hierárquica.
    """
    print("=" * 60)
    print(f"  COLÔNIA: {colonia['nome']}")
    print("=" * 60)

    # Sistema energético
    se = colonia["sistema_energetico"]
    print("\n[SISTEMA ENERGÉTICO]")
    print(f"  Solar   → Geração: {se['solar']['geracao_kw']} kW | Painéis ativos: {se['solar']['paineis_ativos']}")
    print(f"  Eólico  → Vento: {se['eolico']['velocidade_vento_ms']} m/s | Geração: {se['eolico']['geracao_kw']:.1f} kW")
    print(f"  Bateria → Carga: {se['bateria']['carga_percentual']}% | Capacidade: {se['bateria']['capacidade_kwh']} kWh")

    # Sistema ambiental
    sa = colonia["sistema_ambiental"]
    print("\n[SISTEMA AMBIENTAL]")
    print(f"  Temperatura interna : {sa['temperatura_interna_c']} °C")
    print(f"  Temperatura externa : {sa['temperatura_externa_c']} °C")
    print(f"  Pressão atmosférica : {sa['pressao_atm']} atm")

    # Sistema operacional
    so = colonia["sistema_operacional"]
    print("\n[SISTEMA OPERACIONAL]")
    print(f"  Consumo total: {so['consumo_total_kw']} kW | Suporte à vida: {so['suporte_vida']}")
    print("  Módulos:")
    for nome, dados in so["modulos"].items():
        essencial = "ESSENCIAL" if dados["essencial"] else "não essencial"
        print(f"    • {nome:<20} {dados['consumo_kw']:>5} kW  [{essencial}]")


# ============================================================
# MÓDULO 2 — PREVISÃO ENERGÉTICA (Regressão Linear Simples)
# Estima geração eólica com base na velocidade do vento
# ============================================================

def calcular_regressao_linear(x_lista, y_lista):
    """
    Calcula os coeficientes de uma reta y = a*x + b
    usando mínimos quadrados (regressão linear simples).

    Fórmulas:
        a = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
        b = (Σy - a*Σx) / n
    """
    n = len(x_lista)
    soma_x  = sum(x_lista)
    soma_y  = sum(y_lista)
    soma_xy = sum(x_lista[i] * y_lista[i] for i in range(n))
    soma_x2 = sum(x * x for x in x_lista)

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n
    return a, b


def prever_geracao_eolica(velocidade_ms):
    """
    Usa regressão linear sobre dados históricos da colônia
    para estimar a geração eólica (kW) a partir do vento (m/s).

    Dados históricos: vento x geração
    """
    historico_vento  = [4, 6, 8, 10, 12, 14, 16]
    historico_geracao = [8, 12, 20, 25, 30, 38, 44]

    a, b = calcular_regressao_linear(historico_vento, historico_geracao)
    previsao = a * velocidade_ms + b

    print("\n" + "=" * 60)
    print("  PREVISÃO DE GERAÇÃO EÓLICA (Regressão Linear)")
    print("=" * 60)
    print(f"  Dados históricos  : vento={historico_vento}, geração={historico_geracao}")
    print(f"  Equação ajustada  : geração = {a:.2f} × vento + ({b:.2f})")
    print(f"  Entrada           : vento = {velocidade_ms} m/s")
    print(f"  Previsão          : geração ≈ {previsao:.1f} kW")
    print("=" * 60)

    return round(previsao, 1)


# ============================================================
# MÓDULO 3 — ANÁLISE DE ENERGIA
# Compara geração total × consumo e emite diagnóstico
# ============================================================

def analisar_energia(geracao_solar, geracao_eolica, consumo, carga_bateria):
    """
    Compara geração total com consumo e estado da bateria.
    Gera alertas ou sugestões com base nas condições identificadas.
    """
    geracao_total = geracao_solar + geracao_eolica
    diferenca = geracao_total - consumo

    print("\n" + "=" * 60)
    print("  ANÁLISE DE USO DE ENERGIA")
    print("=" * 60)
    print(f"  Geração solar      : {geracao_solar} kW")
    print(f"  Geração eólica     : {geracao_eolica} kW")
    print(f"  Geração total      : {geracao_total} kW")
    print(f"  Consumo total      : {consumo} kW")
    print(f"  Saldo (geração-consumo): {diferenca:+.1f} kW")
    print(f"  Carga da bateria   : {carga_bateria}%")
    print("-" * 60)

    # Regras de análise energética
    if consumo > geracao_total and carga_bateria < 30:
        print("  ⚠  ALERTA CRÍTICO: consumo maior que geração E bateria baixa!")
        print("     → Reduzir consumo imediatamente e ativar modo emergência.")
    elif consumo > geracao_total:
        print("  ⚠  ALERTA: consumo maior que geração.")
        print("     → Recomendado reduzir módulos não essenciais.")
    elif geracao_total > consumo * 1.5:
        print("  ✔  SUGESTÃO: geração excedente significativa.")
        print("     → Armazenar energia nas baterias.")
    elif geracao_total >= consumo:
        print("  ✔  OK: geração suficiente para o consumo atual.")
    print("=" * 60)

    return diferenca


# ============================================================
# MÓDULO 4 — DECISÕES AUTOMÁTICAS (Lógica do Sistema)
# Aplica regras condicionais e prioriza sistemas essenciais
# ============================================================

def tomar_decisao(colonia, diferenca_energia):
    """
    Aplica regras de decisão baseadas no estado atual da colônia.
    Combina múltiplas condições (lógica AND/OR) para gerar ações claras.
    Prioriza sempre o suporte à vida.
    """
    carga      = colonia["sistema_energetico"]["bateria"]["carga_percentual"]
    consumo    = colonia["sistema_operacional"]["consumo_total_kw"]
    modulos    = colonia["sistema_operacional"]["modulos"]
    temp_int   = colonia["sistema_ambiental"]["temperatura_interna_c"]

    print("\n" + "=" * 60)
    print("  SISTEMA DE DECISÃO AUTOMÁTICA")
    print("=" * 60)

    acoes = []

    # Regra 1: Bateria crítica → modo emergência
    if carga < 20:
        acoes.append("ALERTA: bateria crítica (< 20%) → ativar MODO EMERGÊNCIA.")
        acoes.append("→ Desligar todos os módulos não essenciais.")

    # Regra 2: Bateria baixa E consumo alto → reduzir consumo
    elif carga < 50 and consumo > 60:
        acoes.append("ALERTA: bateria baixa E consumo alto → reduzir consumo.")
        acoes.append("→ Desligar módulos não essenciais (pesquisa, mobilidade).")

    # Regra 3: Energia no deficit → economizar
    elif diferenca_energia < 0:
        acoes.append("ALERTA: consumo maior que geração → reduzir consumo.")
        acoes.append("→ Suspender módulos não essenciais temporariamente.")

    # Regra 4: Energia abundante → armazenar
    elif diferenca_energia > 20:
        acoes.append("SUGESTÃO: excesso de energia → carregar baterias.")
        acoes.append("→ Manter todos os sistemas em operação normal.")

    # Regra 5: Situação normal
    else:
        acoes.append("OK: sistema em equilíbrio energético.")
        acoes.append("→ Manter operação normal em todos os módulos.")

    # Regra 6: Temperatura interna fora do ideal (sempre verificar)
    if temp_int < 18 or temp_int > 28:
        acoes.append(f"ALERTA: temperatura interna fora do ideal ({temp_int} °C).")
        acoes.append("→ Ajustar sistema de climatização.")

    # Prioridade máxima: suporte à vida sempre ligado
    print("  [PRIORIDADE MÁXIMA] Suporte à vida: SEMPRE LIGADO")
    print("-" * 60)
    print("  Módulos essenciais garantidos:")
    for nome, dados in modulos.items():
        if dados["essencial"]:
            print(f"    ✔ {nome}")
    print("-" * 60)
    print("  Decisões geradas:")
    for acao in acoes:
        print(f"    → {acao}")
    print("=" * 60)

    return acoes


# ============================================================
# MÓDULO 5 — EXECUÇÃO PRINCIPAL
# Integra todos os módulos em sequência lógica
# ============================================================

def executar_sistema():
    print("\n" + "=" * 60)
    print("  MISSÃO AURORA SIGER — SISTEMA INTELIGENTE DA COLÔNIA")
    print("=" * 60)

    # 1. Carregar dados da colônia
    colonia = inicializar_colonia()

    # 2. Exibir estrutura organizada
    exibir_estrutura(colonia)

    # 3. Prever geração eólica via regressão linear
    vento_atual = colonia["sistema_energetico"]["eolico"]["velocidade_vento_ms"]
    geracao_eolica = prever_geracao_eolica(vento_atual)
    colonia["sistema_energetico"]["eolico"]["geracao_kw"] = geracao_eolica

    # 4. Analisar uso de energia
    geracao_solar = colonia["sistema_energetico"]["solar"]["geracao_kw"]
    consumo       = colonia["sistema_operacional"]["consumo_total_kw"]
    carga_bat     = colonia["sistema_energetico"]["bateria"]["carga_percentual"]
    diferenca     = analisar_energia(geracao_solar, geracao_eolica, consumo, carga_bat)

    # 5. Tomar decisões automáticas
    tomar_decisao(colonia, diferenca)

    print("\n  [FIM DO CICLO DE ANÁLISE — AURORA SIGER]\n")


# ============================================================
# PONTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    executar_sistema()
