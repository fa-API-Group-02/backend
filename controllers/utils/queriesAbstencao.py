import simplejson as json
import sys
import decimal

def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS municipio, " +\
		sumColumns +\
		"FROM `abstencao_2020` " +\
		"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
		"GROUP BY `NM_MUNICIPIO`"

	return query

def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
					`CD_FAIXA_ETARIA` AS 'cd_faixa_etaria', `DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
					SUM(QT_APTOS) AS 'qt_aptos', \
					SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
					SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
					FROM `abstencao_2020` " +\
					"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
					"AND `NR_TURNO` = '1'" +\
					"GROUP BY NM_MUNICIPIO, CD_FAIXA_ETARIA, DS_FAIXA_ETARIA \
					ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaEstadoCivilPorMunicipio(cursor, municipios:[]):
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
					`CD_ESTADO_CIVIL` AS 'cd_estado_civil', `DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
					SUM(QT_APTOS) AS 'qt_aptos', \
					SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
					SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
					FROM `abstencao_2020` " +\
					"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
					"AND `NR_TURNO` = '1'" +\
					"GROUP BY NM_MUNICIPIO, CD_ESTADO_CIVIL, DS_ESTADO_CIVIL \
					ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaGrauEscolaridadePorMunicipio(cursor, municipios:[]):
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
					`CD_GRAU_ESCOLARIDADE` AS 'cd_grau_escolaridade', `DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
					SUM(QT_APTOS) AS 'qt_aptos', \
					SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
					SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
					FROM `abstencao_2020` " +\
					"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
					"AND `NR_TURNO` = '1'" +\
					"GROUP BY NM_MUNICIPIO, CD_GRAU_ESCOLARIDADE, DS_GRAU_ESCOLARIDADE \
					ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)


def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response
