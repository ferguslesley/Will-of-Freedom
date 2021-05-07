import tkinter as tk
import dialogue
import entry_box
import inventory

room_positions = [
    [  # column 0
        None,
        "kitchen",
        None
    ],
    [  # column 1
        "ballroom",
        "dining hall",
        "bedroom"
    ],
    [  # column 2
        "library",
        None,
        "bathroom"
    ],
    [  # column 3
        "?????",
        "cellar",
        "?????"
    ],
    [  # column 4
        None,
        "?????",
        None
    ]
]

default_item_positions = [
            [
                # column 0
                "",
                "",
                ""
            ],
            [
                # column 1
                "",
                "",
                ""
            ],
            [
                # column 2
                "",
                "",
                ""
            ],
            [
                # column 3
                "",
                "",
                ""
            ],
            [
                # column 4
                "",
                "",
                ""
            ]
        ]


class App(tk.Tk):  # Class for root app
    callback = None

    def __init__(self, function, main_map):
        tk.Tk.__init__(self)
        self._frame = None
        self.callback = function
        self.main_map = main_map
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one.
        new_frame = frame_class(self, self.callback, self.main_map)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class StartPage(tk.Frame):  # Class for input page
    callback = None

    def __init__(self, master, function, main_map):
        tk.Frame.__init__(self, master)
        # Create Title Label
        tk.Label(self, text="This is the input page").grid(row=0, column=1, sticky='nesw', padx=17)

        # Create text box
        self.textbox = tk.Text(self, height=12, width=45)
        self.textbox.grid(row=1, column=0, rowspan=3, columnspan=3, padx=17)

        # Configure text box
        self.textbox.config(wrap=tk.WORD)

        tk.Button(self, text="Open Inventory",
                  command=lambda: master.switch_frame(PageOne)).grid(
            row=6, column=0, sticky='w', padx=17)
        tk.Button(self, text="Open Map",
                  width='14',
                  command=lambda: master.switch_frame(PageTwo)).grid(
            row=6, column=2, sticky='e', padx=17)

        self.entry = tk.Entry(self)
        self.entry.grid(row=4, column=1, padx=17)
        input_button = tk.Button(
            self,
            text="Input",
            command=lambda: self.get_input()).grid(
            row=5, column=1, padx=17)
        self.command = None
        self.callback = function
        dialogue.set_function(self.append_textbox)
        dialogue.update_textbox("")   # Force window update
        entry_box.set_function(self.clear_entry)

    def get_input(self):
        self.command = self.entry.get()
        self.callback(self.command)

    def append_textbox(self, text):
        self.textbox.delete('1.0', tk.END)   # Delete current contents of textbox
        self.textbox.insert(tk.END, text)   # Insert text from dialogue text variable
        self.textbox.see("end")   # Scrolls to the bottom of the textbox

    def clear_entry(self):
        self.entry.delete(0, tk.END)


class PageOne(tk.Frame):  # Class for inventory page
    def __init__(self, master, function, main_map):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="This is the Inventory").grid(row=0, column=2)

        self.item_positions = inventory.positions

        for i in range(3):
            for j in range(5):
                frame = tk.Frame(
                    self,
                    borderwidth=1,
                    relief=tk.RAISED
                )
                frame.grid(row=i+1, column=j, padx=5, pady=5)
                label = tk.Label(master=frame, text=self.item_positions[j][i], width=7, height=3)
                label.grid(row=i+1, column=j, padx=5, pady=5)
                master.rowconfigure(i, weight=1)
                master.columnconfigure(j, weight=1)
        tk.Button(self, text="Return to input page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=4, column=1, columnspan='3')

        inventory.set_function(self.add_item)

    def add_item(self, new_item_positions):
        self.item_positions = new_item_positions

    def reset_items(self):
        self.item_positions = default_item_positions


class PageTwo(tk.Frame):  # Class for map page
    def __init__(self, master, function, main_map):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the Map").grid(row=0, column=2)
        for i in range(3):
            for j in range(5):
                frame = tk.Frame(
                    self,
                    borderwidth=1,
                    relief=tk.RAISED
                )
                frame.grid(row=i+1, column=j, padx=5, pady=5)
                if main_map:
                    label = tk.Label(master=frame, text=room_positions[j][i], width=7, height=3)
                    label.grid(row=i+1, column=j, padx=5, pady=5)
                else:
                    label = tk.Label(master=frame, text="????", width=7, height=3)
                    label.grid(row=i+1, column=j, padx=5, pady=5)
                master.rowconfigure(i, weight=1)
                master.columnconfigure(j, weight=1)
        tk.Button(self, text="Return to input page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=4, column=1, columnspan='3')
