import Calculate


class Handler:
    def __init__(self):
        pass

    def handleEntryChange(self,text_after,name,index,mode):
        print("handle",text_after.get(),name,index,mode)