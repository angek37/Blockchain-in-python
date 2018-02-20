import json
from Block import Block

blockchain = []
print(type(blockchain))

#Guarda la cadena en una lista

blockchain.append(Block("Genesis block", 0))
blockchain.append(Block("Second Block", blockchain[-1].hash))
blockchain.append(Block("Third Block", blockchain[-1].hash))


