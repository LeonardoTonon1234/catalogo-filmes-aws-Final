import json
import pymysql

def lambda_handler(event, context):
    connection = pymysql.connect(
        host='catalogofilmes-db.c762082m6il2.us-east-1.rds.amazonaws.com',
        user='admin',
        password='SUA_SENHA_AQUI',
        database='catalogofilmes'
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT id, titulo, diretor, genero, ano_lancamento, avaliacao FROM filmes")
        filmes = cursor.fetchall()

    connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps(filmes)
    }

