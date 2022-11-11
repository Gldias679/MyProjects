from flask import Flask, Response
from flask_restful import Api, Resource, reqparse
import json
from Framework.Get_Item import Busca_Item
from sympy import re

app = Flask(__name__)
api = Api(app)

argumentos = reqparse.RequestParser()
argumentos.add_argument("itensOrigem")
argumentos.add_argument("itensNf")

class GetItens(Resource):

    def get(self):
        args = argumentos.parse_args()

        itensOrigem = json.loads(args['itensOrigem'])
        itensNf = json.loads(args['itensNf'])

        listaNFs = Busca_Item.ListarNFs(itensOrigem)
        listaItensNota = Busca_Item.Itens_por_nota(listaNFs, itensOrigem)


        itensCorretos = []

        for lista in listaItensNota:
            combinacoes = []
            rangeFinal = len(lista) + 1
            for numCombinacoes in range(1, rangeFinal):
                itens = Busca_Item.Combinar_Itens(lista,numCombinacoes)
                for combinacao in itens:
                    combinacoes.append(combinacao)
            for item in itensNf.values():        
                dicionarioItem = Busca_Item.Buscar_Itens(combinacoes, float(item['valor_unit'].replace(',','.')))
                itensCorretos.append(dicionarioItem)
        
        jsonRetorno = {}
        for itemCorreto in itensCorretos:
            contadorItem = 0
            for key in itemCorreto:
                if key != 0:
                    for itemRxTr in itensNf.values():
                        if key == float(itemRxTr['valor_unit'].replace(",",".")):
                            for tupla in itemCorreto.values():
                                for dic in tupla:
                                    for chave in dic:
                                        jsonRetorno['item ' + str(contadorItem)] = {'sku':chave, 'valor_unit':dic[chave], 'quantidade': itemRxTr['quantidade']}
                                        contadorItem += 1
                        else:
                            raise Exception("Não foi possível encontrar um ou mais itens.")
        
        return jsonRetorno

api.add_resource(GetItens, "/item/")

if __name__ == "__main__":
    app.run(debug=True)