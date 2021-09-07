class SteamProfitCalculator:
    FEE = 1.15
    ROUNDTO = 3

    
    def __init__(self):
        pass

    def _beforeReturn(self,x):
        return round(x,self.ROUNDTO)

    def _isNumber(self, *args):
        for arg in args:
            if not isinstance(arg,(int,float)) and arg != None:
                return False
        return True


    def profit(self,*,sellp=None,fee=FEE,buy=None,profitpc=None,mode="sellp"):
        """  
        mode: sellp/profitpc def: sellp
        """

        if mode=="sellp" and self._isNumber(sellp,fee,buy):
            return self._beforeReturn(sellp/fee - buy)

        return False
    

    def profitpc(self,*,profit=None,buy=None,sellp=None,fee=FEE,mode="profit"):
        """  
        mode: sellp/profit def: profit
        """

        if mode=="profit" and self._isNumber(profit,buy):
            return self._beforeReturn(profit/buy)
        
        return False


    def sellp(self,*,profit=None,fee=FEE,buy=None,profitpc=None,mode="profitpc"):
        """  
        mode: profitpc/profit def: profitpc
        """

        notlose = self.count_notlose(buy,fee)

        if mode == "profitpc" and self._isNumber(profitpc,notlose,fee):
            return self._beforeReturn((profitpc+1)*notlose)
        elif mode == "profit" and self._isNumber(buy,profit,fee):
            return self._beforeReturn((profit+buy)*fee)

        return False

    def count_notlose(buy,fee=FEE):
        if (fee and buy) or (buy==0 and fee):
            return buy*fee