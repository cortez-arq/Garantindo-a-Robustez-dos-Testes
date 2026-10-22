import pytest

from credito import aprovar_emprestimo


@pytest.mark.parametrize(
    ("score_serasa", "renda_mensal", "resultado_esperado"),
    [
        (850, 2000.00, True),       # Aprovação por score acima do limite
        (700, 1500.00, True),       # Limite exato do score: >= 700
        (699, 1500.00, False),      # Um ponto abaixo do limite do score
        (500, 8000.00, True),       # Aprovação por renda acima do limite
        (500, 5000.01, True),       # Renda um centavo acima do limite
        (500, 5000.00, False),      # Limite exato da renda: exige > 5000.00
        (500, 4999.99, False),      # Renda um centavo abaixo do limite
        (699, 5000.00, False),      # Ambos os critérios insuficientes nos limites
        (700, 5000.00, True),       # Score atende mesmo que renda esteja no limite
        (300, 1500.00, False),      # Reprovação por score e renda baixos
    ],
)
def test_aprovar_emprestimo_nos_limites(
    score_serasa, renda_mensal, resultado_esperado
):
    assert aprovar_emprestimo(score_serasa, renda_mensal) is resultado_esperado
