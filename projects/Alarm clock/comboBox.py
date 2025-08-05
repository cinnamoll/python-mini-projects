import tkinter as tk
from PIL import Image, ImageTk

class comboBox():
    def __init__(self, root, options, x, y, var = None) -> None:
        self.dropdown_id = None
        self.root = root
        self.options = options

        self.wrapper = tk.Frame(self.root)
        self.wrapper.pack()
        self.wrapper.place(x=x, y=y)

        self.entry = tk.Entry(self.wrapper, width = 10)
        self.entry.bind("<KeyRelease>", self.on_entry_key)
        self.entry.bind("<FocusIn>", self.show_dropdown)
        self.entry.bind("<Return>", self.on_entry_return)
        self.entry.bind("<FocusOut>", self.on_entry_return)
        self.entry.pack(side=tk.LEFT)

        self.icon = ImageTk.PhotoImage(Image.open("projects\\Alarm clock\\down-arrow.png").resize((16, 16)))
        tk.Button(self.wrapper, image=self.icon, command = self.show_dropdown).pack(side = tk.LEFT)

        self.listBox = tk.Listbox(self.root, height = 5, width = 30)
        self.listBox.bind("<<ListboxSelect>>", self.on_select)

        for option in self.options:
            self.listBox.insert(tk.END, option)
        
        self.var = var if var is not None else tk.StringVar()


    def on_entry_key(self, event):
        typed = event.widget.get().strip().lower()
        if not typed:
            self.listBox.delete(0, tk.END)
            for option in self.options:
                self.listBox.insert(tk.END, option)
        else:
            self.listBox.delete(0, tk.END)
            filtered = [option for option in self.options if option.lower().startswith(typed)]
            for option in filtered:
                self.listBox.insert(tk.END, option)
        self.show_dropdown()

    def on_select(self, event):
        selected_index = self.listBox.curselection()
        if selected_index:
            selected_val = self.listBox.get(selected_index)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_val)
            self.var.set(selected_val)

    def show_dropdown(self, event = None):
        self.listBox.place(in_ = self.entry, x = 0, rely = 1, relwidth = 1.0, anchor = "nw")
        self.listBox.lift()

        if self.dropdown_id:
            self.listBox.after_cancel(self.dropdown_id)
        self.dropdown_id = self.listBox.after(4000, self.hide_dropdown)

    def hide_dropdown(self):
        self.listBox.place_forget()

    def on_entry_return(self, event):
        value = self.entry.get()
        if value in self.options:
            self.var.set(value)