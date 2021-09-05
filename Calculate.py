


class SteamProfitCalculator:
    default_fee = 1.15

    def __init__(self):
        pass

    def _beforeReturn(x):
        return round(x,2)

    def _isNumber(self, *args):
        for arg in args:
            if not isinstance(arg,(int,float)) and arg != None:
                return False
        return True


    def profit(self,*,sellp=None,fee=1.15,buy=None,profitpc=None,mode="sellp"):
        """  
        mode: sellp/profitpc def: sellp
        """


        if mode=="sellp" and self._isNumber(sellp,fee,buy):
            return self._beforeReturn(sellp/fee - buy)

        return False
    

    def profitpc(self,*,profit=None,buy=None,notlose=None,sellp=None,fee=1.15,mode="profit"):
        """  
        mode: sellp/profit def: profit
        """

        if mode=="profit" and self._isNumber(profit,buy):
            return self._beforeReturn(profit/buy)
        
        return False


    def sellp(self,*,profit=None,fee=1.15,buy=None,profitpc=None,notlose=None,mode="profitpc"):
        """  
        mode: profitpc/profit def: profitpc
        """
    
        if mode == "profitpc" and self._isNumber(profitpc,notlose,fee):
            return self._beforeReturn((profitpc+1)*notlose)
        elif mode == "profit" and self._isNumber(buy,profit,fee):
            return self._beforeReturn((profit+buy)*fee)

        return False
        



