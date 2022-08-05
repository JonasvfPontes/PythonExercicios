#Cores no terminal
# sempre que eu quiser adicionar cores no terminal eu coloco \033[style;text;Back m]
'''     text - - - - background

30  ↔    black           preto     →   40
31  ↔    red             vermelho  →   41
32  ↔    green           verde     →   42
33  ↔    yellow          amarelo   →   43
34  ↔    blue            azul      →   44
35  ↔    Magenta         Magenta   →   45
36  ↔    cyan            ciano     →   46
37  ↔    grey            cinza     →   47
97  ↔    white           branco    →  107'''

print('\033[0;30;41mJonas\33[m')
'''Para as fontes das letras, ou seja, para o "Stylo" segue a tabela abaixo
0 - SEM FORMATAÇÃO
1 - NEGRITO
4 - SUBLINHADO
7 - INVERTE AS CORES'''