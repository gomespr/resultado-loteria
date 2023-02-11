import requests

def resultado(loteria):
    # Tentar implementar a Loteca 'Loteca':'https://servicebus2.caixa.gov.br/portaldeloterias/api/loteca',
    links = {'Mega':'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena', 
             'Quina':'https://servicebus2.caixa.gov.br/portaldeloterias/api/quina', 
             'Dupla Sena':'https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena', 
             'Loto Fácil':'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil', 
             'Loto Mania':'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania', 
             'Dia de Sorte':'https://servicebus2.caixa.gov.br/portaldeloterias/api/diadesorte', 
             'Time Mania':'https://servicebus2.caixa.gov.br/portaldeloterias/api/timemania', 
             'Federal':'https://servicebus2.caixa.gov.br/portaldeloterias/api/federal',  
             'Super Sete':'https://servicebus2.caixa.gov.br/portaldeloterias/api/supersete'}
    
    
    mega = requests.get(links[loteria], verify=False)
    dic = mega.json()
    
    
    return dic['listaDezenas']