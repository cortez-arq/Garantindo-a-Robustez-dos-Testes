O mutmut show evidencia que um mutante pode trocar >= 700 por > 700, alterando a regra no limite.
O teste com score exatamente igual a 700 detecta essa mudança, pois a aprovação esperada é True.
A análise de valor limite verifica os valores imediatamente abaixo, exatamente no limite e acima dele.
Isso revela falhas que testes com valores muito distantes do limite podem não detectar.
Assim, os testes ficam mais rigorosos e conseguem eliminar mutantes que alteram as condições da regra.
