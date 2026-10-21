from credito import aprovar_emprestimo


# --- Análise de Valor Limite: Score (Fronteira em 700) ---
def test_score_exatamente_no_limite():
    # Deve aprovar pois a regra exige score >= 700
    assert aprovar_emprestimo(700, 2000.00) is True


def test_score_logo_abaixo_do_limite():
    # Deve reprovar pois 699 < 700 e a renda é insuficiente
    assert aprovar_emprestimo(699, 5000.00) is False


# --- Análise de Valor Limite: Renda (Fronteira em 5000.00) ---
def test_renda_exatamente_no_limite():
    # Deve reprovar pois a regra exige renda > 5000.00 (estrito)
    assert aprovar_emprestimo(600, 5000.00) is False


def test_renda_logo_acima_do_limite():
    # Deve aprovar pois 5000.01 > 5000.00
    assert aprovar_emprestimo(600, 5000.01) is True


# --- Casos Gerais e Combinações Lógicas ---
def test_aprovacao_por_score_alto():
    assert aprovar_emprestimo(850, 1000.00) is True


def test_aprovacao_por_renda_alta():
    assert aprovar_emprestimo(500, 8000.00) is True


def test_aprovacao_por_ambos_critérios():
    assert aprovar_emprestimo(750, 6000.00) is True


def test_reprovacao_ambos_abaixo():
    assert aprovar_emprestimo(300, 1500.00) is False
