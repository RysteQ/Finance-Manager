from matplotlib_window import DisplayGraph

from datetime import date

from tkinter.filedialog import asksaveasfile as SaveFD
from tkinter.filedialog import askopenfile as OpenFD
import tkinter as Tk

def initGUI():
    main_window = Tk.Tk()

    open_csv_file_button = Tk.Button(
        text = "Open File",
        width = 10,
        height = 1,
        command = OpenFile
    )

    save_csv_file_button = Tk.Button(
        text = "Save File",
        width = 10,
        height = 1,
        command = SaveFile
    )

    display_csv_graph_button = Tk.Button(
        text = "Display Graph",
        width = 22,
        height = 1,
        command = DisplayGraph
    )

    open_csv_file_button.grid(column = 0, row = 0)
    save_csv_file_button.grid(column = 1, row = 0)
    display_csv_graph_button.grid(column = 0, row = 1, columnspan = 2)

    return main_window

def OpenFile():
    open_file_dialog = OpenFD(
        initialfile = "",
        defaultextension = "*.csv",
        filetypes = [
            ("CSV File (*.csv)", "*.csv")
        ]
    )

    # I might use this later so the user can edit the valus in the program rather than an external application
    filename = open_file_dialog.name
    file = open(filename, "r")
    file.close()

def SaveFile():
    current_day = date.today().strftime("%B %d %Y")
    contents = ""

    save_file_dialog = SaveFD(
        initialfile = current_day,
        defaultextension = ".csv",
        filetypes = [
            ("CSV File (*.csv)", ".csv")
        ]
    )

    # I might use this later so the user can edit the valus in the program rather than an external application
    filename = save_file_dialog.name
    file = open(filename, "w")
    
    file.write(contents)
    file.close()