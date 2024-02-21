import tkinter as tk
from tkinter import messagebox

class luasbangun:
    def __init__(self, root):
        self.root = root
        self.root.title("aplikasi hitung luas - adeilla")

        #variabel untuk menyimpan jenis bangun
        self.jenis_bangun = tk.StringVar()
        self.jenis_bangun.set("persegi")

        #input label dan entry
        label_input = tk.Label(root, text="input")
        label_input.grid(row=1, column=0, padx=10, pady=10)

        self.entry_input = tk.Entry(root)
        self.entry_input.grid(row=1, column=1, padx=10, pady=10)

        #tombol hitung luas
        button_hitung = tk.Button(root, text="hitung luas", command=self.hitung_luas)
        button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

    def hitung_luas(self):
        jenis_bangun = self.jenis_bangun.get()
        input_nilai = self.entry_input.get()

        try:
            nilai = float(input_nilai)

            if jenis_bangun == "persegi":
                luas = nilai ** 2
            else:
                messagebox.showerror("error", "pilih jenis bangun yang valid")
                return

            messagebox.showinfo("hasil", f"luas {jenis_bangun} adalah: {luas}")

        except ValueError:
            messagebox.showerror("error", "masukkan nilai valid")


if __name__ == "__main__":
    root = tk.Tk()
    app = luasbangun(root)
    root.mainloop()
