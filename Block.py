import datetime

class Blockchain:
    hash = ""
    data = ""
    previousHash = ""
    timeStamp = ""

    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = datetime.datetime.now()