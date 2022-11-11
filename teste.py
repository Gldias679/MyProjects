from urllib import response
import requests
import json


base = 'http://20.96.227.207/'
#base = 'http://127.0.0.1:5000/'
dic = {"itensOrigem":'{"Item 1":{"Sku": "RX1252670DP0000000","Valor_Unit": "367,9","NF":"978462001"},"Item 2":{"Sku": "RX0252840DP1310001","Valor_Unit": "372,39","NF":"978462001"}}', "itensNf": '{"Item 1":{"valor_unit":"740,29","quantidade":"2"}}'}

response = requests.get(base + "item/", dic)

print(response)
