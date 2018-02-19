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
        print(self.hash)

    def calculateHash(self):
        inp = "{}{} {}".format(self.previousHash, self.timeStamp, self.data)
        calculatedHash = hashlib.sha256(str.encode(inp, "UTF-8")).hexdigest()
        return calculatedHash
