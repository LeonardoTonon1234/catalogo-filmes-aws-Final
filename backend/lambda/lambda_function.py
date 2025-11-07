import json
import urllib.request

def lambda_handler(event, context):
    try:
        # URL da sua API Gateway
        API_URL = "https://7itkaw7gz0.execute-api.us-east-1.amazonaws.com/prod/filmes"
        
        # Faz requisição GET para obter os filmes
        with urllib.request.urlopen(API_URL) as response:
            data = response.read().decode()
            filmes = json.loads(data)

        # Calcula métricas simples
        total = len(filmes)
        media_avaliacao = sum(f["avaliacao"] for f in filmes) / total if total > 0 else 0
        anos = [f["anoLancamento"] for f in filmes]
        mais_recente = max(anos) if anos else "N/A"
        mais_antigo = min(anos) if anos else "N/A"

        # Monta o relatório
        relatorio = {
            "total_filmes": total,
            "media_avaliacao": round(media_avaliacao, 2),
            "ano_mais_recente": mais_recente,
            "ano_mais_antigo": mais_antigo
        }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "mensagem": "Relatório gerado com sucesso!",
                "relatorio": relatorio
            }),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
