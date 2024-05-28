import pandas as pd

def producao (year: int):
    return pd.read_html(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_02', encoding='utf8', thousands='.', decimal=',')[3]
    
def processamento(year: int, subopt: int):
    return pd.read_html(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_03&subopcao=subopt_{subopt:02}', encoding='utf8', thousands='.', decimal=',')[3]

def comercializacao(year: int):
    return pd.read_html(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_04', encoding='utf8', thousands='.', decimal=',')[3]

def importacao(year: int, subopt: int):
    return pd.read_html(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_05&subopcao={subopt:02}', encoding='utf8', thousands='.', decimal=',')[3]

def exportacao(year: int, subopt: int):
    return pd.read_html(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_06&subopcao={subopt:02}', encoding='utf8', thousands='.', decimal=',')[3]