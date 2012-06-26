#!/usr/bin/python
from Dialog import *
from Tkinter import *
from hello import Hello

class HelloGoodbye(Hello):
	def really_quit(self):
		Hello.quit(self)
	
	def quit(self):
		ans = Dialog(self,
			title		= 'Verify exit',
			text		= 'No, sucker! :P',
			bitmap		= 'question',
			strings		= ('Yes', 'No'), default = 1)

		if ans.num == 0:
			self.really_quit()
	
	def make_widgets(self):
		Hello.make_widgets(self)
		extra = Button(self, text = 'Bye', command = self.really_quit)
		extra.pack(side=RIGHT)

if __name__ == '__main__': HelloGoodbye().mainloop()
