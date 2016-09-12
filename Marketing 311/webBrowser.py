import requests

import tkinter
# import ScrolledText
from tkinter import messagebox


class Browser:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()
        self.build_url_asker()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=2)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background="blue",
            fg="white",
            text="Web Browser",
            font=("Helvetica", 24),
        )
        banner.grid(
            row=0, column=0,
            sticky="ew",
            padx=10, pady=10
        )

    def build_url_asker(self):
        self.ask = tkinter.Entry(self.mainframe)
        go_button_frame = tkinter.Frame(self.mainframe)
        go_button_frame.grid(row=2, column=0, sticky="nwe", padx=10,pady=10)
        go_button_frame.columnconfigure(0, weight=1)

        self.go_button = tkinter.Button(
            go_button_frame,
            text="Go!",
            command = self.send_request
        )
        self.go_button.grid(row=0, column=0, sticky="nwe")

        self.ask.grid(row=1, column=0,
                 sticky="enw",
                 padx=10, pady=10)

    def build_response_holder(self):
        self.response = ScrolledText.ScrolledText(
            self,
            wrap=tkinter.WORD
        )


    def send_request(self):
        query_string = self.ask.get().replace(" ", "-")
        query_string = "http://www."+ query_string + ".com"

        with requests.Session() as sesh:
            response = sesh.get(query_string)
            print(response.text)







if __name__ == "__main__":
    root = tkinter.Tk()
    Browser(root)
    root.mainloop()
