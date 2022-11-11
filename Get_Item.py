from itertools import combinations


class Busca_Item():

    def ListarNFs(itensNf_Origem):
    # Coleta as notas fiscais disponíveis no dicionário de itens da nota de origem e retorna uma lista contendo-as
       
        listaNFs = []
        
        for value in itensNf_Origem.values():
            if value['NF'] not in listaNFs:
                listaNFs.append(value['NF'])

        return listaNFs

    def Itens_por_nota(listaNFs, itensNF_Origem):
    #Retorna uma lista de listas de dicionários com os itens separados por nota fiscal
  
        listaItens = []

        for nota_fiscal in listaNFs:
            itens = []
            for value in itensNF_Origem.values():
                if value['NF'] == nota_fiscal:
                    dic_item = {value['Sku']:float(value['Valor_Unit'].replace(',','.'))}
                    itens.append(dic_item)
            listaItens.append(itens)
        
        return listaItens

    def Combinar_Itens(itensNF_Origem, num_combinacoes):
    # Retorna uma lista com todas as combinações de itens possíveis no número de itens a serem combinados

        combinacoes = []

        for item in combinations(itensNF_Origem, num_combinacoes):
            soma = 0
            for dicionario in item:
                for values in dicionario.values():
                    soma += values
                    soma = round(soma,2)
            dic_item = {soma:item}
            combinacoes.append(dic_item)

        return combinacoes
    
    def Buscar_Itens(combinacao_Itens, valor_Item):
    # Retorna o dicionário dentro da combinação que tem a Key igual ao valor do item

        dicItem = {0:'nao encontrado'}

        for dicionario in combinacao_Itens:
            for key in dicionario:
                if key == valor_Item:
                    dicItem = dicionario

    # Se o dicionário retornar uma combinação, ela deverá ser removida para evitar duplicidade
        for key in dicItem:            
            if dicItem[key] != 'nao encontrado':
                index = 0
                for dic in combinacao_Itens:
                    for keyDic in dic:
                        if key == keyDic:
                            combinacao_Itens.pop(index)
                            break
                    index += 1
                
        return dicItem

        
