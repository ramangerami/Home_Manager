import tkinter as tk
from tkinter import messagebox
import requests


class UpdateDetachedHomePopup(tk.Frame):
    """ Popup frame to Update a Home """

    def __init__(self, id, parent, close_callback):
        """ Constructor method """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Square Footage:").grid(row=1, column=1)
        self._square_footage = tk.Entry(self)
        self._square_footage.grid(row=1, column=2)
        tk.Label(self, text="Year Built:").grid(row=2, column=1)
        self._year_built = tk.Entry(self)
        self._year_built.grid(row=2, column=2)
        tk.Label(self, text="Number of Rooms:").grid(row=3, column=1)
        self._number_of_rooms = tk.Entry(self)
        self._number_of_rooms.grid(row=3, column=2)
        tk.Label(self, text="Number of Bathrooms:").grid(row=4, column=1)
        self._number_of_bathrooms = tk.Entry(self)
        self._number_of_bathrooms.grid(row=4, column=2)
        tk.Label(self, text="City:").grid(row=5, column=1)
        self._city = tk.Entry(self)
        self._city.grid(row=5, column=2)
        tk.Label(self, text="Selling Agent:").grid(row=6, column=1)
        self._selling_agent = tk.Entry(self)
        self._selling_agent.grid(row=6, column=2)
        tk.Label(self, text="Yearly Property Tax:").grid(row=7, column=1)
        self._yearly_property_tax = tk.Entry(self)
        self._yearly_property_tax.grid(row=7, column=2)
        tk.Label(self, text="Has Rental Suite:").grid(row=8, column=1)
        self._has_rental_suite = tk.Entry(self)
        self._has_rental_suite.grid(row=8, column=2)
        tk.Label(self, text="Number Of Floors:").grid(row=9, column=1)
        self._number_of_floors = tk.Entry(self)
        self._number_of_floors.grid(row=9, column=2)
        # tk.Label(self, text="Type:").grid(row=10, column=1)
        # self._type = tk.Entry(self)
        # self._type.grid(row=10, column=2)
        self._home_id = id
        # tk.Label(self, text="ID:").grid(row=10, column=1)
        # self._home_id = tk.Entry(self)
        # self._home_id.grid(row=10, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=11, column=2)




    def _submit_cb(self):
        """ Submit the Update Detached Home """
        data = {}
        data['square_feet'] = int(self._square_footage.get())
        data['year_built'] = int(self._year_built.get())
        data['number_of_rooms'] = int(self._number_of_rooms.get())
        data['number_of_bathrooms'] = int(self._number_of_bathrooms.get())
        data['city'] = str(self._city.get())
        data['selling_agent'] = str(self._selling_agent.get())
        data['yearly_property_tax'] = float(self._yearly_property_tax.get())
        data['has_rental_suite'] = int(self._has_rental_suite.get())
        data['number_of_floors'] = int(self._number_of_floors.get())
        data['type'] = 'detached home'
        data['id'] = int(self._home_id)

        self._update_detached_home(data)

    def _update_detached_home(self, data):
        headers = {"content-type": "application/json"}
        response = requests.put("http://127.0.0.1:5000/homemanager/homes/"+str(self._home_id), json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Cannot update Home because" + response.text)