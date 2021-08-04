#implement table
class SQLTable:
    def __init__(self, name):
        self.name = name
        self.prvkey_list = []
        self.forkey_list = []

#implement property
class PrvProperty:
    def __init__(self, name, type):
        self.name = name
        self.type = type

#implement Foreign Key
class ForProperty:
    def __init__(self, name, trg_tb, trg_id, rfr_tb, rfr_id):
        self.name = name
        self.trg_tb = trg_tb
        self.trg_id = trg_id
        self.rfr_tb = rfr_tb
        self.rfr_id = rfr_id

