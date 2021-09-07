from tkinter import StringVar
from Calculate import SteamProfitCalculator

"""
self.entry_sellprice 
self.entry_buyprice 
self.entry_profit 
self.entry_profitpercent 
self.entry_minsell4profit 
self.entry_sell420pc 
self.entry_sell450pc
"""

class Handler:
    calculate : SteamProfitCalculator = None
    last_entry_name : str = None
    _r = None    # root, MainWindow

    def __init__(self,root):
        if root == None:
            raise ValueError
        self.calculate = SteamProfitCalculator()
        self._r = root
        

    def handleEntryChange(self,text_after,name,index,mode):
        #print("handle",text_after.get(),name,index,mode)
        
        self.last_entry_name = name
        self.getStrVar(name)==""

        # 1 - profit
        if self.getStrVar("sellp") != "" and self.getStrVar("buyp") != "":
            self.do_actions(self.calculate.profit (sellp = self.getStrVar("sellp"),buy = self.getStrVar("buyp")),mode = "sellp")

        # 3 - profitpc  
        if self.getStrVar("profit") != "" and self.getStrVar("buyp") != "":
            self.do_actions(self.calculate.profitpc(profit = self.getStrVar("profit"), buy = self.getStrVar("buyp"), mode = "profit"))

        # 5 - 
        if self.getStrVar("profitpc") != "" and self.getStrVar("buyp") != "":
            self.do_actions(self.calculate.sellp(profitpc = self.getStrVar("profitpc"), mode = "profitpc"))
        
        # 6 -
        if self.getStrVar("profit") != "" and self.getStrVar("buyp") != "":
            self.do_actions(self.calculate.sellp(profit = self.getStrVar("profit"), buy = self.getStrVar("buyp"), mode = "profit"))



    def getStrVar(self,name):
        return self._r.entries[name]["StringVar"].get()
    
    def do_actions():
        pass

    

        