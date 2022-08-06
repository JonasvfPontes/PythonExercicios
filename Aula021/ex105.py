def notas(* n, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adiocinar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    nota = dict()
    nota["total"] = len(n)
    nota["maior"] = max(n)
    nota["menor"] = min(n)
    nota["média"] = sum(n)/nota["total"]
    if sit:
        if nota["média"] < 5:
            nota["situação"] = 'RUIM'
        elif nota["média"] < 7:
            nota["situação"] = 'RAZOÁVEL'
        elif nota["média"] > 7:
            nota["situação"] = 'BOA'
    return nota


resp = notas(5.5, 4.5, 10, 6.5, 10, 1, 3, 12)
print(resp)

