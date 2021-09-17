class SteamProfitCalculator:

    _DEFAULTFEE = 1.15

    def __init__(self,fee = 1.15, ):#roundto=3):
        self.changeFee(fee)
        #if isinstance(roundto,int):
        #    self.ROUNDTO = roundto


    def changeFee(self,newvalue):
        if isinstance(newvalue,(float,int)) and newvalue != 0:
            self.FEE = float(newvalue)
        else:
            self.FEE = self._DEFAULTFEE


    def _beforeReturn(self,x):
        #return round(x,self.ROUNDTO)
        return x


    def _isValid(self, *args):
        for arg in args:
             
            try:
                arg = float(arg)
            except ValueError:
                return False
            except Exception:
                print("WARNING: UNKNOWN ERROR")
                return False
            
        return True


    def count_notlose(self,buyp,fee=None):
        if fee == None:
            fee = self.FEE

        if self._isValid(buyp,fee):
            buyp,fee = float(buyp),float(fee)
            return self._beforeReturn(buyp*fee)
        return False


    def profit(self,*, sellp = None, fee = None,buyp = None, profitpc = None, mode = "sellp"):
        """  
        mode: sellp def: sellp
        sellp - sellp,buyp
        """
        if fee == None:
            fee = self.FEE

        if mode=="sellp" and self._isValid(sellp,fee,buyp):
            sellp,fee,buyp = float(sellp),float(fee),float(buyp)
            return self._beforeReturn(sellp/fee - buyp)

        return False
    

    def profitpc(self,*,profit = None,buyp = None,sellp = None,fee = None,mode = "profit"):
        """  
        mode: profit def: profit
        profit - profit,buyp
        """
        if fee == None:
            fee = self.FEE

        if mode=="profit" and self._isValid(profit,buyp):
            profit, buyp = float(profit),float(buyp)
            if buyp != 0:
                return self._beforeReturn(profit/buyp)
        
        return False

    def exactprofitpc(self,*, percent = None, buyp = None, fee = None, mode = "percent"):
        """  
        mode: percent def: percent
        percent - percent,buyp 

        (percent = 50 is 50%)
        """
        if fee == None:
            fee = self.FEE

        if self._isValid(percent,buyp,fee):
            percent,buyp,fee = float(percent),float(buyp),float(fee)
            return self._beforeReturn((1.0+percent/100.0) * buyp * fee)
        return False


    def sellp(self,*,profit=None,fee=None,buyp=None,profitpc=None,mode="profitpc"):
        """  
        mode: profitpc/profit def: profitpc
        profit - buyp,profit
        profitpc - profitpc,buyp
        """
        if fee == None:
            fee = self.FEE

        if mode == "profitpc" and self._isValid(profitpc,buyp,fee):
            profitpc,buyp,fee = float(profitpc),float(buyp),float(fee)
            notlose = self.count_notlose(buyp,fee)
            return self._beforeReturn((profitpc+1)*notlose)

        elif mode == "profit" and self._isValid(buyp,profit,fee):
            buyp,profit,fee = float(buyp),float(profit),float(fee)
            return self._beforeReturn((profit+buyp)*fee)

        return False

    def buyp(self,*, profit = None, profitpc = None, sellp = None, fee = None, mode = "sellp"):
        """  
        mode: profit/sellp def: sellp
        profit - profit,profitpc
        sellp - sellp,profit
        """
        if fee == None:
            fee = self.FEE

        if mode == "sellp" and self._isValid(sellp,profit,fee):
            sellp,fee,profit = float(sellp),float(fee),float(profit),
            return self._beforeReturn(sellp/fee - profit)
        elif mode == "profit" and self._isValid(profit,profitpc):
            profit,profitpc = float(profit),float(profitpc)
            if profitpc != 0:
                return self._beforeReturn(profit/profitpc)
        return False
        