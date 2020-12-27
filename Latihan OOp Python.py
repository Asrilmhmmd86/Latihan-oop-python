import tkinter

main_window = tkinter.Tk()

tombol1 = tkinter.Button(main_window, text = "button1")
tombol2 = tkinter.Button(main_window, text = "button2")

#method_positioning
tombol1.pack()
tombol2.pack()

#method_menampilkan GUI
main_window.mainloop()