import tkinter as tk
from tkinter import messagebox
import requests


class AddDetachedHomePopup(tk.Frame):
    """ Popup frame to add a detached home """

    def __init__(self, parent, close_callback):
        """ Constructor method """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Square Footage:").grid(row=1, column=1)
        self.square_footage = tk.Entry(self)
        self.square_footage.grid(row=1, column=2)
        tk.Label(self, text="Year Built:").grid(row=2, column=1)
        self.year_built = tk.Entry(self)
        self.year_built.grid(row=2, column=2)
        tk.Label(self, text="Number of Rooms:").grid(row=3, column=1)
        self.number_of_rooms = tk.Entry(self)
        self.number_of_rooms.grid(row=3, column=2)
        tk.Label(self, text="Number of Bathrooms:").grid(row=4, column=1)
        self.number_of_bathrooms = tk.Entry(self)
        self.number_of_bathrooms.grid(row=4, column=2)
        tk.Label(self, text="City:").grid(row=5, column=1)
        self.city = tk.Entry(self)
        self.city.grid(row=5, column=2)
        tk.Label(self, text="Selling Agent:").grid(row=6, column=1)
        self.selling_agent = tk.Entry(self)
        self.selling_agent.grid(row=6, column=2)
        tk.Label(self, text="Yearly Property Tax:").grid(row=7, column=1)
        self.yearly_property_tax = tk.Entry(self)
        self.yearly_property_tax.grid(row=7, column=2)
        tk.Label(self, text="Has Rental Suite:").grid(row=8, column=1)
        self.has_rental_suite = tk.Entry(self)
        self.has_rental_suite.grid(row=8, column=2)
        tk.Label(self, text="Number Of Floors:").grid(row=9, column=1)
        self.number_of_floors = tk.Entry(self)
        self.number_of_floors.grid(row=9, column=2)
        # tk.Label(self, text="Type:").grid(row=10, column=1)
        # self.type = tk.Entry(self)
        # self.type.grid(row=10, column=2)
        tk.Label(self, text="ID:").grid(row=10, column=1)
        self.id = tk.Entry(self)
        self.id.grid(row=10, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=11, column=2)




    def _submit_cb(self):
        """ Submit the Add Detached Home """
        data = {}
        data['square_feet'] = int(self.square_footage.get())
        data['year_built'] = int(self.year_built.get())
        data['number_of_rooms'] = int(self.number_of_rooms.get())
        data['number_of_bathrooms'] = int(self.number_of_bathrooms.get())
        data['city'] = str(self.city.get())
        data['selling_agent'] = str(self.selling_agent.get())
        data['yearly_property_tax'] = float(self.yearly_property_tax.get())
        data['has_rental_suite'] = int(self.has_rental_suite.get())
        data['number_of_floors'] = int(self.number_of_floors.get())
        data['type'] = "detached home"
        data['id'] = int(self.id.get())

        self._add_detached_home(data)

    def _add_detached_home(self, data):
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/homemanager/homes", json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Cannot add Detached Home because" + response.text)