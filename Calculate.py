class SteamProfitCalculator:
    FEE = 1.15
    ROUNDTO = 3

    def __init__(self):
        pass

    def _beforeReturn(self,x):
        return round(x,self.ROUNDTO)


    def _isValid(self, *args):
        for arg in args:
             
            try:
                arg = float(arg)
            except ValueError:
                return False
            except Exception:
                print("WARNING: UNKNOWN ERROR")
                return False
            
            if isinstance(arg,float) or arg == None:
                return True
        return False


    def count_notlose(self,buyp,fee=FEE):
        if buyp!=None and fee != None and self._isValid(buyp,fee):
            return buyp*fee
        return False


    def profit(self,*,sellp=None,fee=FEE,buyp=None,profitpc=None,mode="sellp"):
        """  
        mode: sellp/profitpc def: sellp
        """
        
        if mode=="sellp" and self._isValid(sellp,fee,buyp):
            
            return self._beforeReturn(sellp/fee - buyp)

        return False
    

    def profitpc(self,*,profit=None,buyp=None,sellp=None,fee=FEE,mode="profit"):
        """  
        mode: sellp/profit def: profit
        """

        if mode=="profit" and self._isValid(profit,buyp):
            return self._beforeReturn(profit/buyp)
        
        return False

    def exactprofitpc(self,*, percent = None, buyp = None, mode = "percent"):
        """  
        mode: percent def: percent
        """
        if self._isValid(percent,buyp):
            return self._beforeReturn((1+percent) * buyp)
        return False


    def sellp(self,*,profit=None,fee=FEE,buyp=None,profitpc=None,mode="profitpc"):
        """  
        mode: profitpc/profit def: profitpc
        """

        notlose = self.count_notlose(buyp,fee)

        if mode == "profitpc" and self._isValid(profitpc,notlose,fee):
            return self._beforeReturn((profitpc+1)*notlose)
        elif mode == "profit" and self._isValid(buyp,profit,fee):
            return self._beforeReturn((profit+buyp)*fee)

        return False

    def buyp(self,*, profit = None, profitpc = None, sellp = None, fee = FEE, mode = "sellp"):
        """  
        mode: profit/sellp def: sellp
        """
        if mode == "sellp" and self._isValid(sellp,fee,profit):
            return self._beforeReturn(sellp/fee - profit)
        elif mode == "profit" and self._isValid(profit,profitpc):
            return self._beforeReturn(profit/profitpc)
        return False
        