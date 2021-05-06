import simplejson as json
import sys
import decimal

def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "

	if not municipios:
		query = "SELECT " + sumColumns +\
			"FROM `abstencao_2020` \
			WHERE NR_TURNO = '1'"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "
		query = "SELECT `NM_MUNICIPIO` AS municipio, " +\
			sumColumns +\
			"FROM `abstencao_2020` " +\
			"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
			"AND NR_TURNO = '1' \
			GROUP BY `NM_MUNICIPIO`"

	return query


def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1' " +\
						"GROUP BY DS_FAIXA_ETARIA \
						ORDER BY DS_FAIXA_ETARIA ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO, DS_FAIXA_ETARIA \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaEstadoCivilPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1'" +\
						"GROUP BY DS_ESTADO_CIVIL \
						ORDER BY DS_ESTADO_CIVIL ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO,DS_ESTADO_CIVIL \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaGrauEscolaridadePorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1'" +\
						"GROUP BY DS_GRAU_ESCOLARIDADE \
						ORDER BY DS_GRAU_ESCOLARIDADE ASC"
						
	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO, DS_GRAU_ESCOLARIDADE \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)


def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response
