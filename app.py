from tkinter import *
class Application:
	def __init__(self,master=None):
		self.widget1 = Frame(master)
		self.widget1.pack()
		self.msg = Label(self.widget1,text='maerli')
		self.msg.pack()
root = Tk()
root.title('maerli')
root.geometry('400x400')
Application(root)
print(dir(root))
root.mainloop()