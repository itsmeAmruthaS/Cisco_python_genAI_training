
import time

class vendor:

    def __init__(self,vName,vGST):
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} wenrollment is done')

    def billing(self,pname,pQty=0,pCost=0.0):
        self.pName = pname
        self.pQty = pQty
        self.pCost = pCost
        self.tot = self.pQty * self.pCost
        self.tax = self.tot * 0.18 
        self.gs = self.tot + self.tax
        print(f'Total cost for product {self.pName} is {self.tot}')
        print(f'Billing for product {self.pName} with quantity {self.pQty} and cost {self.pCost} is done')