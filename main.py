import tkinter as tk
from ttkbootstrap import Style as StyleBs
import tkinter.ttk as ttk

class MainWindow(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        # Configuring rows & columns weight (for parent and for this main window)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)

        # Placing main frame
        self.grid(row=0,column=0, sticky = "nsew")

        self.entry_sellprice = ttk.Entry(self)
        self.entry_buyprice = ttk.Entry(self)
        self.entry_profit = ttk.Entry(self)
        self.entry_profitpercent = ttk.Entry(self)
        self.entry_minsell4profit = ttk.Entry(self)
        self.entry_sell420pc = ttk.Entry(self)
        self.entry_sell450pc = ttk.Entry(self)

        self.label_sellprice = ttk.Label(self)
        self.label_buyprice = ttk.Label(self)
        self.label_profit = ttk.Label(self)
        self.label_profitpc = ttk.Label(self)
        self.label_minsell4profit = ttk.Label(self)
        self.label_sell420pc = ttk.Label(self)
        self.label_sell450pc = ttk.Label(self)

        self.labels = {
            "sellp" : { 
                "widget" : self.label_sellprice,
                #"StringVar" :
                },

            "buyp" : { 
                "widget" : self.label_buyprice,
                
                },

            "profit" : { 
                "widget" : self.label_profit,
                
                },

            "profitpc" : { 
                "widget" : self.label_profitpc,
                
                },

            "minsell4profit" : { 
                "widget" : self.label_minsell4profit,
                
                },

            "sell420pc" : { 
                "widget" : self.label_sell420pc,
                
                },

            "sell450pc" : { 
                "widget" : self.label_sell450pc,
                
                },
        }
        
        self.entries = {
            "sellp" : { 
                "widget" : self.entry_sellprice,
                
                },

            "buyp" : { 
                "widget" : self.entry_buyprice,
                
                },

            "profit" : { 
                "widget" : self.entry_profit,
                
                },

            "profitpc" : { 
                "widget" : self.entry_profitpercent,
                
                },

            "minsell4profit" : { 
                "widget" : self.entry_minsell4profit,
                
                },

            "sell420pc" : { 
                "widget" : self.entry_sell420pc,
                
                },

            "sell450pc" : { 
                "widget" : self.entry_sell450pc,
                
                },
        }

        self.gridMatrix = [
            [self.label_sellprice,      self.label_buyprice],
            [self.entry_sellprice,      self.entry_buyprice],
            [self.label_profit,         self.entry_profit],
            [self.label_profitpc,  self.entry_profitpercent],
            [self.label_minsell4profit, self.entry_minsell4profit],
            [self.label_sell420pc,      self.entry_sell420pc],
            [self.label_sell450pc,      self.entry_sell450pc],
        ]
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        # Grid all elements from matrix:
        row=0
        for wholerow in self.gridMatrix:
            column=0
            self.grid_rowconfigure(row,weight=1)
            for cell in wholerow:
                cell.grid(row=row,column=column,sticky="nsew",padx=3,pady=3)
                column += 1
            row += 1

        for i in range(2,7):                        # only for those rows
            self.gridMatrix[i][0]["anchor"]="e" 
        
        for entry in self.entries.values():
            print(entry,type(entry))
            entry["StringVar"] = tk.StringVar()
            entry["widget"]["textvariable"] = entry["StringVar"]
            entry["StringVar"].trace_add("write",lambda name, index, mode, text_after = entry["StringVar"]: self.handleWriteEvent(text_after,name,index,mode))


        self.changeLabel("Sell Price: ","Buy Price: ","Profit:","Profit %: ","Not-lose price: ","Sell price for 20% profit: ","Sell price for 50% profit: ")

        

    def handleWriteEvent(self,text_after,name,index,mode):
        print("handle",text_after.get(),name,index,mode)

        



        

    def changeLabel(self, sp = None, bp = None, profit = None, profpc = None, minsprofit = None, s20pc = None, s50pc = None):
        if sp != None:
            self.label_sellprice["text"] = sp
        if bp  != None:
            self.label_buyprice["text"] = bp
        if profit  != None:
            self.label_profit["text"] = profit
        if profpc  != None:
            self.label_profitpc["text"] = profpc
        if minsprofit  != None:
            self.label_minsell4profit["text"] = minsprofit 
        if s20pc  != None:
            self.label_sell420pc["text"] = s20pc
        if s50pc  != None:
            self.label_sell450pc["text"] = s50pc



try:
    if __name__ ==  "__main__" : 
        mainwindows_args = {}
        root = tk.Tk()
        root.resizable(1, 1)
        """ root.geometry("260x270") """
        # root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./img/calc_icon.png')) #setting icon
        root.title("Steam profit calculator")
        MainWindow(root, **mainwindows_args)
        root.mainloop() 

except Exception as e:
    print(e)
""" 
def callback(x):
   content= x.get()
   Label(win, text=content).pack()

#Create an variable to store the user-input
var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))
#Create an Entry widget
e = Entry(win, textvariable=var) """