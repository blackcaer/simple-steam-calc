from tkinter import StringVar
from Calculate import SteamProfitCalculator

class ValuesTab:
    #FEE = 1.15

    def __init__(self,init_tab = None,):

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

    def __init__(self,root,roundto = 2, fee = 1.15):
        self.roundto = roundto
        self.FEE = fee
        if root == None:
            raise ValueError
        self.calculate = SteamProfitCalculator()
        self.checked_entries = ValuesTab()
        self.updated_entries = ValuesTab()
        self.handling_flag = False
        self.root = root
        

    def getEntryVal(self,name):
        return self.root.entries[name]["StringVar"].get()
    
    def setEntryVal(self,name,content = "",iffalse=False):

        if content == False and content != "":
            if iffalse != False:
                self.root.entries[name]["StringVar"].set(iffalse)
        else:
            self.root.entries[name]["StringVar"].set(content)

    def do_actions(*args):
        pass 

    def handleEntryChange(self,stringvar_after,name,index,mode):           
        if self.handling_flag == False: 
            """
            when handling input, text is inserted in the entries which is also noticed as entryChange event, so it would create infite loop of handling
            """
            self.handling_flag = True
            self.last_entry_name = name
            self.updated_entries.add(name)

            # Replacing "," with correct dot
            text_after = stringvar_after.get()
            text_after = text_after.replace(",",".")
            self.setEntryVal(name,text_after) 
            
            self.calculate_entries()
            self.handling_flag = False


    def calculate_entries(self):
    # ifs checking what can be calculated

        print(" ==== start ==== ")
        while True:
            if not self.checked_entries.contains("sellp") and not self.updated_entries.contains("sellp"):    # in sellp not calculated and can do that, do this
                val = self.calculate.sellp(profitpc = self.getEntryVal("profitpc"), buyp = self.getEntryVal("buyp"), mode = "profitpc")
                if not val or self.last_entry_name == "profit":     # if profit was inserted, calculating by the value of profitpc will be wrong, cause profitpc is calculated after sellp
                    val = self.calculate.sellp(profit = self.getEntryVal("profit"), buyp = self.getEntryVal("buyp"), mode = "profit")
                if val:
                    self._set("sellp",val) 
                else:
                    self._mark("sellp")

            elif not self.checked_entries.contains("profit") and not self.updated_entries.contains("profit"):
                val = self.calculate.profit(sellp = self.getEntryVal("sellp"), buyp = self.getEntryVal("buyp"))
                if val:
                    self._set("profit",val) 
                else:
                    self._mark("profit")

            elif not self.checked_entries.contains("profitpc") and not self.updated_entries.contains("profitpc"):
                val = self.calculate.profitpc(buyp = self.getEntryVal("buyp"), profit = self.getEntryVal("profit"))
                if val:
                    self._set("profitpc",val) 
                else:
                    self._mark("profitpc")
           
            elif not self.checked_entries.contains("minsell4profit") and not self.updated_entries.contains("minsell4profit"):
                val = self.calculate.count_notlose(buyp = self.getEntryVal("buyp"))
                if val:
                    self._set("minsell4profit",val) 
                else:
                    self._mark("minsell4profit")

            elif not self.checked_entries.contains("sell420pc") and not self.updated_entries.contains("sell420pc"):
                val = self.calculate.exactprofitpc(percent = 20, buyp = self.getEntryVal("buyp"))
                if val:
                    self._set("sell420pc",val) 
                else:
                    self._mark("sell420pc")

            elif not self.checked_entries.contains("sell450pc") and not self.updated_entries.contains("sell450pc"):
                val = self.calculate.exactprofitpc(percent = 50, buyp = self.getEntryVal("buyp"))
                if val:
                    self._set("sell450pc",val) 
                else:
                    self._mark("sell450pc")

            else:
                self.checked_entries.clear()
                self.updated_entries.clear()
                print(" ==== empty ==== ")
                break

    def _set(self,name,val):
        print(" - ",name," - ",val)

        if name == "profitpc":
            val *= 100.0
            val = str(round(val,self.roundto)) + '%'

        if isinstance(val,(float,int)):
            val = round(val,self.roundto)

        self.setEntryVal(name, val)
            
        self.checked_entries.clear()
        self.updated_entries.add(name)

        self._mark(name)

    def _mark(self,name):
        self.checked_entries.add(name)
        print("checked: ",name)