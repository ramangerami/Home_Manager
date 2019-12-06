import tkinter as tk
import requests
from add_car_popup import AddCarPopup
from add_truck_popup import AddTruckPopup
from sell_popup import SellPopup
from remove_vehicle_popup import RemoveVehiclePopup
from tkinter import messagebox


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Home Listings").grid(row=1, column=2)
        self._vehicle_listbox = tk.Listbox(self, width=70)
        self._vehicle_listbox.grid(row=2, column=1, columnspan=5)
        self._vehicles = []

        tk.Button(self, text="Add Condo", command=self._add_car).grid(row=3, column=1)
        tk.Button(self, text="Add Detached Home", command=self._add_truck).grid(row=3, column=2)
        tk.Button(self, text="Sell Home", command=self._sell_vehicle).grid(row=3, column=3)
        tk.Button(self, text="Remove Home", command=self._remove_vehicle).grid(row=3, column=4)

        tk.Button(self, text="Quit", command=self._quit_callback).grid(row=4, column=2)

        self._update_vehicles_list()

    def _add_car(self):
        """ Add Home Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddCarPopup(self._popup_win, self._close_car_cb)

    def _close_car_cb(self):
        """ Close Add Home Popup """
        self._popup_win.destroy()
        self._update_vehicles_list()

    def _add_truck(self):
        """ Add Home Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddTruckPopup(self._popup_win, self._close_truck_cb)

    def _close_truck_cb(self):
        """ Close Add Home Popup """
        self._popup_win.destroy()
        self._update_vehicles_list()

    def _sell_vehicle(self):
        """ Sell Home Popup """
        self._popup_win = tk.Toplevel()
        self._popup = SellPopup(self._popup_win, self._close_sell_cb)



    def _close_sell_cb(self):
        """ Close Sell Home Popup """
        self._popup_win.destroy()
        self._update_vehicles_list()



    def _remove_vehicle(self):
        self._popup_win = tk.Toplevel()
        self._popup = RemoveVehiclePopup(self._popup_win, self._close_remove_cb)

    def _close_remove_cb(self):
        """ Close Sell Home Popup """
        self._popup_win.destroy()
        self._update_vehicles_list()



    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_vehicles_list(self):
        """ Update the List of Home Descriptions """
        response1 = requests.get("http://127.0.0.1:5000/carlot/vehicles/descriptions/car")

        if response1.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the vehicles.")
            return

        response2 = requests.get("http://127.0.0.1:5000/carlot/vehicles/descriptions/truck")

        if response2.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the vehicles.")
            return

        self._vehicles.clear()
        self._vehicle_listbox.delete(0, tk.END)

        data = response1.json()
        num = 1
        for vehicle in data:
            self._vehicles.append(vehicle)
            self._vehicle_listbox.insert(tk.END, vehicle)
            num += 1

        data2 = response2.json()
        num = 1
        for vehicle in data2:
            self._vehicles.append(vehicle)
            self._vehicle_listbox.insert(tk.END, vehicle)
            num += 1




if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

