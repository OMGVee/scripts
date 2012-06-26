from Tkinter import *

class Hello(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.make_widgets()

	def make_widgets(self):
		widget = Button(self, text='Hoi', command=self.quit)
		widget.pack(side=LEFT)

if __name__ == '__main__': Hello().mainloop()
