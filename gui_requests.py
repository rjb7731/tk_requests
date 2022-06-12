import tkinter as tk
import requests


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # URL Entry
        self.entry_box = tk.Entry(width=66)
        self.entry_box.place(x=475, y=50)
        self.contents = tk.StringVar()
        #post headers entry
        self.entry_box_2 = tk.Text(root,height=2,width=50)
        self.entry_box_2.place(x=475, y=100)
        self.contents_2 = tk.StringVar()
        #data entry
        self.entry_box_3 = tk.Text(root,height=2,width=50)
        self.entry_box_3.place(x=475, y=150)
        self.contents_3 = tk.StringVar()
        
        # self.entry_box["textvariable"] = self.contents
        self.entry_box.bind('<Key-Return>',self.get_request)

        ##URL-LABEL
        self.L1 = tk.Label(root, text="URL")
        self.L1.place(x=425, y=50)

        #request headers-LABEL
        self.L2 = tk.Label(root, text="Request Headers")
        self.L2.place(x=375, y=105)

        ##requests data-LABEL
        self.L3 = tk.Label(root, text="Request Data")
        self.L3.place(x=375, y=155)

        ##headers-LABEL
        self.L4 = tk.Label(root, text="Response Headers")
        self.L4.place(x=950, y=265)

        ##statuscode-LABEL
        self.L5 = tk.Label(root, text="Status Code")
        self.L5.place(x=540, y=265)

       	##response-LABEL
        self.L6 = tk.Label(root, text="Text Response")
        self.L6.place(x=275, y=265)

        ##GET BUTTON
        self.GetButton = tk.Button(text="GET", pady=10,width=10, command=self.get_request)
        self.GetButton.place(x=550, y=195)

        ##POST button
        self.PostButton = tk.Button(text="POST", pady=10,width=10, command=self.get_request)
        self.PostButton.place(x=650, y=195)

        ##Status code
        self.status_box = tk.Text(root,height=1,width=5)
        self.status_box.place(x=610, y=265)

        ##text box 1
        self.text_box = tk.Text(root,height=20,width=75)
        self.text_box.place(x=15, y=295)
        #scroll text
        self.text_box2 = tk.Text(root,height=20,width=75)
        self.text_box2.place(x=650, y=295)
        #scroll text

    def get_request(self):
    	print(self.entry_box.get())
    	r= requests.get(f"https://www.{self.entry_box.get()}")
    	self.status_box.insert(tk.END, r.status_code)
    	self.text_box.insert(tk.END,r.text)
    	self.text_box2.insert(tk.END,r.headers)



if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1000x600")
	root.state("zoomed")
	myapp = App(root)
	myapp.mainloop()