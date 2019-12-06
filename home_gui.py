import tkinter as tk
from tkinter import messagebox

import requests
from add_condo_popup import AddCondoPopup
from add_detached_home_popup import AddDetachedHomePopup
from update_condo_popup import UpdateCondoPopup
from updated_detached_home import UpdateDetachedHomePopup
# from add_truck_popup import AddTruckPopup
# from sell_popup import SellPopup
# from remove_popup import RemovePopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Home Listings").grid(row=1, column=2)
        self._homes_listbox = tk.Listbox(self, width=150)
        self._homes_listbox.grid(row=2, column=1, columnspan=5)

        self._home_listings = []

        tk.Label(self, text="Statistics").grid(row=1, column=70)
        self._statistics_listbox = tk.Listbox(self, width=20)
        self._statistics_listbox.grid(row=2, column=70, columnspan=50)


        specific = tk.StringVar()
        specific.set("condo")
        self.specific = specific
        self.selection_label = tk.Label(self, text=self.specific.get())
        self.selection_label.grid(row=3, column=2)

        tk.Button(self, text="Reload", command=self._update_listings).grid(row=3,column=1)
        tk.Radiobutton(self, text="Condo", variable=specific, value="condo", command=self._update_listings).grid(row=4,column=1)
        tk.Radiobutton(self, text="Detached Home", variable=specific, value="detached home", command=self._update_listings).grid(row=4,column=2)

        self.add_home_btn = tk.Button(self, text="Add "+self.specific.get().upper(), command=self._add_home)
        self.add_home_btn.grid(row=3, column=3)
        self.detail_home_btn = tk.Button(self, text="Details "+self.specific.get().upper(), command=self._details_home)
        self.detail_home_btn.grid(row=4, column=3)
        self.delete_home_btn = tk.Button(self, text="Delete Home", command=self._delete_home)
        self.delete_home_btn.grid(row=4, column=4)
        self.update_home_btn = tk.Button(self, text="Update Home", command=self._update_home)
        self.update_home_btn.grid(row=3, column=1)

        # tk.Button(self, text="Add Truck", command=self._add_truck).grid(row=3, column=2)
        # tk.Button(self, text="Sell Vehicle", command=self._sell_vehicle).grid(row=3, column=3)
        # tk.Button(self, text="Remove Vehicle", command=self._remove_vehicle).grid(row=3, column=4)
        # tk.Button(self, text="Quit", command=self._quit_callback).grid(row=4, column=2)

        self._update_homes_list()



    def _update_listings(self):
        """ Changes the listing based on the Radio selection """
        selection = self.specific.get()
        self.selection_label['text'] = selection
        self.add_home_btn['text'] = "Add "+selection.upper()
        self.delete_home_btn['text'] = "Delete "+selection.upper()
        self.update_home_btn['text'] = "Update "+selection.upper()
        # print(selection)
        response = requests.get("http://127.0.0.1:5000/homemanager/homes/descriptions/"+selection)

        if response.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the homes.")
            return
        self._home_listings.clear()
        self._homes_listbox.delete(0, tk.END)
        data = response.json()
        for home in data:
            self._home_listings.append(home)
            self._homes_listbox.insert(tk.END, home)

        response = requests.get("http://127.0.0.1:5000/homemanager/homes/all/"+selection)

        if response.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the homes.")
            return

        self._home_listings.clear()
        data = response.json()
        num = 1
        for home in data:
            self._home_listings.append(home)
            num += 1


    def _update_homes_list(self):
        """ Update the List of Home Descriptions """
        self._update_homes_stats()
        self._update_listings()

    def _add_home(self):
        """ Add Home Popup """
        selection = self.specific.get()
        self._popup_win = tk.Toplevel()

        if selection == "condo":
            self._popup = AddCondoPopup(self._popup_win, self._close_home_cb)
        elif selection == "detached home":
            self._popup = AddDetachedHomePopup(self._popup_win, self._close_home_cb)
            # print("DETACHED HOME ADD")
        else:
            print("Home type not found")

    def _update_home(self):
        """ Add Home Popup """
        selection = self.specific.get()
        self._popup_win = tk.Toplevel()
        cursor = self._homes_listbox.curselection()

        if cursor is None or len(cursor) == 0:
            messagebox.showwarning("Warning", "No home selected to update.")
            return

        home = self._home_listings[cursor[0]]


        if selection == "condo":
            self._popup = UpdateCondoPopup(home["id"], self._popup_win, self._close_home_cb)
        elif selection == "detached home":
            self._popup = UpdateDetachedHomePopup(home["id"], self._popup_win, self._close_home_cb)
            # print("DETACHED HOME UPDATE")
        else:
            print("Home type not found")

    def _close_home_cb(self):
        """ Close Edit Home Popup """
        self._popup_win.destroy()
        self._update_homes_list()


    def _delete_home(self):
        """ Deletes the selected home """
        selection = self._homes_listbox.curselection()

        if selection is None or len(selection) == 0:
            messagebox.showwarning("Warning", "No home selected to delete.")
            return

        home = self._home_listings[selection[0]]

        result = messagebox.askyesno("Confirm", "Are you sure you want to delete the home?")

        if result:
            response = requests.delete("http://127.0.0.1:5000/homemanager/homes/" + str(home["id"]))
            # print(home)
            self._update_homes_list()

    def _details_home(self):
        """ Displays details for the selected home """
        selection = self._homes_listbox.curselection()

        if selection is None or len(selection) == 0:
            messagebox.showwarning("Warning", "No home selected to show details for.")
            return

        home = self._home_listings[selection[0]]

        # result = messagebox.askyesno("Confirm", "Are you sure you want to delete the home?")

        # if result:
        response = requests.get("http://127.0.0.1:5000/homemanager/homes/" + str(home["id"]))
        # print(response.text)
        messagebox.showinfo("Details for id: "+str(home["id"]), response.text)
            # print(home)
        self._update_homes_list()

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

