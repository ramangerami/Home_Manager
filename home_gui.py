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
        self._homes_listbox = tk.Listbox(self, width=70)
        self._homes_listbox.grid(row=2, column=1, columnspan=5)

        self._home_listings = []

        tk.Label(self, text="Statistics").grid(row=1, column=70)
        self._statistics_listbox = tk.Listbox(self, width=20)
        self._statistics_listbox.grid(row=2, column=70, columnspan=50)


        specific = tk.StringVar()
        specific.set("condo")
        self.specific = specific
        self.selection_label = tk.Label(self, text=self.specific.get())
        self.selection_label.grid(row=3, column=7)

        tk.Button(self, text="Print var", command=self.print_var).grid(row=3,column=1)
        tk.Radiobutton(self, text="Condo", variable=specific, value="condo", command=self.print_var).grid(row=4,column=1)
        tk.Radiobutton(self, text="Detached Home", variable=specific, value="detached home", command=self.print_var).grid(row=4,column=2)

        # tk.Button(self, text="Add Car", command=self._add_car).grid(row=3, column=1)
        # tk.Button(self, text="Add Truck", command=self._add_truck).grid(row=3, column=2)
        # tk.Button(self, text="Sell Vehicle", command=self._sell_vehicle).grid(row=3, column=3)
        # tk.Button(self, text="Remove Vehicle", command=self._remove_vehicle).grid(row=3, column=4)
        # tk.Button(self, text="Quit", command=self._quit_callback).grid(row=4, column=2)

        self._update_homes_list()



    def print_var(self):
        """ Changes the label showing what you selected on the Radio """
        selection = self.specific.get()
        self.selection_label['text'] = selection
        print(selection)
        response = requests.get("http://127.0.0.1:5000/homemanager/homes/all/"+selection)

        if response.status_code != 200:

            messagebox.showwarning("Warning", "Could not retrieve the homes.")

            return

        self._home_listings.clear()

        self._homes_listbox.delete(0, tk.END)

        data = response.json()

        num = 1

        for home in data:

            self._home_listings.append(home)

            self._homes_listbox.insert(tk.END, home)

            num += 1


    def _update_homes_list(self):
        """ Update the List of Home Descriptions """
        self._update_homes_stats()
        self.print_var()

    # def _update_homes_list(self):
    #     """ Update the List of Home Descriptions """
    #     self.Home.delete(0, tk.END)

    #     response = requests.get("http://127.0.0.1:5000/carlot/vehicles/descriptions/car")
    #     for vehicle in response.json():
    #         self._vehicle_listbox.insert(tk.END, vehicle)

    #     if response.status_code != 200:
    #         messagebox.showwarning("Warning", "Could not retrieve the homes.")
    #         return

    #     # response = requests.get("http://127.0.0.1:5000/carlot/vehicles/descriptions/truck")

    #     for vehicle in response.json():
    #         self._vehicle_listbox.insert(tk.END, vehicle)

    #     if response.status_code != 200:
    #         messagebox.showwarning("Warning", "Could not retrieve the homes.")
    #         return

    #     # self._update_homes_stats()

    def _update_homes_stats(self):
        """ Update the Home Listing Statistics """
        self._statistics_listbox.delete(0, tk.END)

        response = requests.get("http://127.0.0.1:5000/homemanager/homes/stats")
        for stat in response.json():
            self._statistics_listbox.insert(tk.END, stat + ": " + str(response.json()[stat])) 

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

