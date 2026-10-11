

def display():
    for var in ['f1', 'f2', 'f3']:
        print(var)

class Cname:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2

    def display(self):
        return self.a1, self.a2

def connect(dsn):
    class Connection:
        def __init__(self, dsn, dbname, password):
            self.dsn = dsn
            self.dbname = dbname
            self.password = password

        def method(self):
            return 'query processed'

    obj = Connection(dsn, 'mydb', 'mypassword')
    return obj



   