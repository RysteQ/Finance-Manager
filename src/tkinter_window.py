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

    open_csv_file_button.grid(column = 0, row = 0)
    save_csv_file_button.grid(column = 1, row = 0)

    return main_window

def OpenFile():
    open_file_dialog = OpenFD(
        initialfile = "",
        defaultextension = "*.csv",
        filetypes = [
            ("CSV File (*.csv)", "*.csv")
        ]
    )

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

    filename = save_file_dialog.name
    file = open(filename, "w")
    
    file.write(contents)
    file.close()