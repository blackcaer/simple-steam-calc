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

class ValuesTab:
    FEE = 1.15

    def __init__(self,init_tab = None):
        if type(init_tab) == list:
            self.tab = init_tab
        elif init_tab == None:
            self.tab = []
        else:
            raise ValueError("Init_tab must be a list")

    def get(self):
        return self.tab[:]

    def clear(self):
        self.tab.clear()

    def add(self,element):
        self.tab.append(element)
    
    def contains(self,element):
        if element in self.tab:
            return True
        return False


class Handler:

    def __init__(self,root):
        if root == None:
            raise ValueError
        self.calculate = SteamProfitCalculator()
        self.checked_entries = ValuesTab()
        self.updated_entries = ValuesTab()
        self.handling_flag = False
        self._r = root
        

    def getStrVar(self,name):
        return self._r.entries[name]["StringVar"].get()
    
    def setStrVar(self,name,content = "",iffalse=False):
        """ 
         """
        if content == False:
            self._r.entries[name]["StringVar"].set(iffalse)
        self._r.entries[name]["StringVar"].set(content)

    def do_actions(*args):
        pass 

    def handleEntryChange(self,text_after,name,index,mode):           
        if self.handling_flag == False: 
            """
            when handling input, text is inserted in the entries which is also noticed as entryChange event, so it would create infite loop of handling
            """
            self.handling_flag = True
            self.last_entry_name = name
            self.updated_entries.add(name)
            self.calculate_entries()
            self.handling_flag = False
            


    def calculate_entries(self):
    # ifs checking what can be calculated

        print(" ==== start ==== ")
        while True:
            if not self.checked_entries.contains("sellp") and not self.updated_entries.contains("sellp"):    # in sellp not calculated and can do that, do this
                val = self.calculate.sellp(profitpc = self.getStrVar("profitpc"), buyp = self.getStrVar("buyp"), mode = "profitpc")
                if not val or self.last_entry_name == "profit":     # if profit was inserted, calculating by the value of profitpc will be wrong, cause profitpc is calculated after sellp
                    val = self.calculate.sellp(profit = self.getStrVar("profit"), buyp = self.getStrVar("buyp"), mode = "profit")
                if val:
                    self._set("sellp",val) 
                else:
                    self._set("sellp",0)

            elif not self.checked_entries.contains("profit") and not self.updated_entries.contains("profit"):
                val = self.calculate.profit(sellp = self.getStrVar("sellp"), buyp = self.getStrVar("buyp"))
                if val:
                    self._set("profit",val) 
                else:
                    self._set("profit",0)

            elif not self.checked_entries.contains("profitpc") and not self.updated_entries.contains("profitpc"):
                val = self.calculate.profitpc(buyp = self.getStrVar("buyp"), profit = self.getStrVar("profit"))
                if val:
                    self._set("profitpc",val) 
                else:
                    self._set("profitpc",0)
           
            elif not self.checked_entries.contains("minsell4profit") and not self.updated_entries.contains("minsell4profit"):
                val = self.calculate.count_notlose(buyp = self.getStrVar("buyp"))
                if val:
                    self._set("minsell4profit",val) 
                else:
                    self._set("minsell4profit",0)

            elif not self.checked_entries.contains("sell420pc") and not self.updated_entries.contains("sell420pc"):
                val = self.calculate.exactprofitpc(percent = 20, buyp = self.getStrVar("buyp"))
                if val:
                    self._set("sell420pc",val) 
                else:
                    self._set("sell420pc",0)

            elif not self.checked_entries.contains("sell450pc") and not self.updated_entries.contains("sell450pc"):
                val = self.calculate.exactprofitpc(percent = 50, buyp = self.getStrVar("buyp"))
                if val:
                    self._set("sell450pc",val) 
                else:
                    self._set("sell450pc",0)

            else:
                self.checked_entries.clear()
                self.updated_entries.clear()
                print(" ==== empty ==== ")
                break

    def _set(self,name,val):
        if val != 0:                # TODO DELETE IT! TEST
            print(" - ",name," - ",val)
            self.setStrVar(name, val)
            self.checked_entries.clear()
            self.updated_entries.add(name)
        self.checked_entries.add(name)
        print("checked: ",name)
        

# garbage : 

            #elif not self.checked_entries.contains("buyp") and not self.updated_entries.contains("buyp"):
            #    val = self.calculate.buyp(profitpc = self.getStrVar("profitpc"), profit = self.getStrVar("profit"), mode="profit")
            #    if not val:
            #        val = self.calculate.profitpc(sellp = self.getStrVar("sellp"), profit = self.getStrVar("profit"), mode="sellp")
            #    if val:
            #        self._set("buyp",val) 
            #    else:
            #        self._set("buyp",0)