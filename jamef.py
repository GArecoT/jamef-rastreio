import requests, sys

def main():
    if(len(sys.argv) < 3):
        print("Siga o padrão:\njamef.py {nota_fiscal} {cnpj_cpf}")
        return

    print("Gerando Token...")
    res = requests.post('https://www.jamef.com.br/login-api', headers = {
            "Host":"www.jamef.com.br",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Origin":"https://www.jamef.com.br",
            "Connection":"keep-alive",
            "Referer":"https://www.jamef.com.br/",
            "Cookie":"Path=/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            "host":"www.jamef.com.br",
    })
    token = res.json()['token']
    headers = {
        "Host":"5p9h1eo176.execute-api.us-east-1.amazonaws.com",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip, deflate, br, zstd",
        "Content-Type":"application/json",
        "Authorization": f"Bearer {token}",
        "Origin":"https://www.jamef.com.br",
        "Connection":"keep-alive",
        "Referer":"https://www.jamef.com.br/",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"cross-site",
        "host":"5p9h1eo176.execute-api.us-east-1.amazonaws.com"
    }
    data = {
        "nota_fiscal": sys.argv[1], 
        "cnpj_cpf": sys.argv[2]	
    }
    print("\n\nRastreando...")
    res = requests.post('https://5p9h1eo176.execute-api.us-east-1.amazonaws.com/prod/rastreamento-carga', json  = data, headers= headers)
    retorno = res.json()
    print(f"\n\n## DADOS ##\nOrigem: {retorno['Conhecimentos'][0]['municipioOrigem']},{retorno['Conhecimentos'][0]['ufOrigem']} -> Destino: {retorno['Conhecimentos'][0]['municipioDestino']},{retorno['Conhecimentos'][0]['ufDestino']}\nPrevisão: {retorno['Conhecimentos'][0]['dataPrevisaoEntrega']}\n\n")
    print("## Histórico ##")
    for historico in reversed(retorno['Historico']):
        print(f"Status: {historico['dataAtualizacao']} - {historico['statusRastreamento']}\nOrigem: {historico['municipioOrigem']},{historico['ufOrigem']} -> {historico['municipioDestino']},{historico['ufDestino']}\n\n")
    

main()

