n1 = float(input('Primeira nota '))
n2 = float(input('Segudna nota '))
m = (n1 + n2)/2
if m < 5:
    print('Vc é muito burro, está \033[0;41mREPROVADO!\033[m')
elif m >= 5 and m < 6.9:
    print('Vc ainda tem uma chance, \033[2;30;45mRECUPERAÇÃO\033[m')
else:
    print('Vc teve muita sorte, \033[0;42m APROVADO!!!!!!\033[m')