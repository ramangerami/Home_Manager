import tkinter as tk
from tkinter import messagebox
import requests


class RemoveHomePopup(tk.Frame):
    """ Popup Frame to Remove a Home """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="ID:").grid(row=1, column=1)
        self._home_id = tk.Entry(self)
        self._home_id.grid(row=1, column=2)

        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=3, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=3, column=2)

    def _submit_cb(self):
        """ Submit Remove Home """
        data = {}
        data['home_id'] = self._home_id.get()

        result = messagebox.askyesno("Confirm", "Are you sure you want to delete the Home?")

        if result:
            response = requests.delete("http://127.0.0.1:5000/homemanager/homes/" + str(data["home_id"]))

            if response.status_code == 200:
                self._close_cb()
            else:
                messagebox.showwarning("Error", "Delete Home Request Failed")