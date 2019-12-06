import tkinter as tk
import requests
# from add_car_popup import AddCarPopup
# from add_truck_popup import AddTruckPopup
# from sell_popup import SellPopup
# from remove_popup import RemovePopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Home Listings").grid(row=1, column=2)
        self._homes_listbox = tk.Listbox(self, width=50)
        self._homes_listbox.grid(row=2, column=1, columnspan=5)

        tk.Label(self, text="Statistics").grid(row=1, column=7)
        self._statistics_listbox = tk.Listbox(self, width=50)
        self._statistics_listbox.grid(row=2, column=7, columnspan=50)


        specific = tk.StringVar()
        specific.set("condo")
        self.specific = specific
        tk.Button(self, text="Print var", command=self.print_var).grid(row=3,column=1)
        tk.Radiobutton(self, text="Condo", variable=specific, value="condo").grid(row=4,column=1)
        tk.Radiobutton(self, text="Detached Home", variable=specific, value="detached home").grid(row=4,column=2)

        # tk.Button(self, text="Add Car", command=self._add_car).grid(row=3, column=1)
        # tk.Button(self, text="Add Truck", command=self._add_truck).grid(row=3, column=2)
        # tk.Button(self, text="Sell Vehicle", command=self._sell_vehicle).grid(row=3, column=3)
        # tk.Button(self, text="Remove Vehicle", command=self._remove_vehicle).grid(row=3, column=4)
        # tk.Button(self, text="Quit", command=self._quit_callback).grid(row=4, column=2)

        # self._update_vehicles_list()



    def print_var(self):
        print(self.specific.get())

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

