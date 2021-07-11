import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there 				= tk.Button(self)
        self.hi_there["text"] 		= "Hello World\n(click me)"
        self.hi_there["command"] 	= self.say_hi
        self.hi_there.pack(side="top")

        self.example 			= tk.Button(self,fg="green")
        self.example["text"] 	= "Click the example"
        self.example["command"]	= self.new_example
        self.example.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def new_example(self):
    	print("new example command")

if __name__ == "__main__":
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()