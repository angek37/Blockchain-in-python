import datetime
import hashlib

class Block:
    hash = ""
    data = ""
    previousHash = ""
    timeStamp = ""

    #Constructor
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = datetime.datetime.now()
        self.hash = self.calculateHash()

    def calculateHash(self):
        inp = "{}{} {}".format(self.previousHash, self.timeStamp, self.data)
        calculatedHash = hashlib.sha256(str.encode(inp, "UTF-8")).hexdigest()
        return calculatedHash


#Test
# genesisBlock = Block("First Block", 0)
# print("Hash for 1º Block:", genesisBlock.hash)
# secondBlock = Block("Second Block", genesisBlock.hash)
# print("Hash for 2º Block:", secondBlock.hash)
# thirdBlock = Block("Third Block", secondBlock.hash)
# print("Hash for 3º Block:", thirdBlock.hash)