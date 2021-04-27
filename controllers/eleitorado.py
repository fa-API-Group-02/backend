from flask import jsonify
import controllers.utils.queriesEleitorado as function
import pymysql.cursors
import simplejson as json
import sys

def connectDb(request):
	json_data = request.get_json()
	municipios = json_data["MN_MUNICIPIO"]

# Conexão com mysql
	try:
		connection = pymysql.connect(
			user="admin",
			password="admin",
			host="127.0.0.1",
			port=3306,
			database="api_dados",
			cursorclass=pymysql.cursors.DictCursor
		)

	except pymysql.Error as e:
		print(f"Erro de conexão ao SGBD {e}")
		sys.exit(1)

	colunas = json_data["colunas"]
	with connection:
		with connection.cursor() as cursor:
			retornoBanco = function.buscaPorMunicipiosComColunas(cursor, municipios, colunas)

	return json.dumps(retornoBanco)

def eleitoradoQuery(request):
	return connectDb(request)
