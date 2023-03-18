from datetime import date
from tkinter.filedialog import asksaveasfile
import tkinter as Tk

def initGUI():
    main_window = Tk.Tk()

    open_csv_file_button = Tk.Button(
        text = "Open File",
        width = 10,
        height = 1
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

def SaveFile():
    current_day = date.today().strftime("%B %d %Y")

    save_file_dialog = Tk.filedialog.asksaveasfile(
        initialfile = current_day,
        defaultextension = ".csv",
        filetype = [
            ("CSV File (*.csv)", "(.csv)")
        ]
    )