from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1600x2000+100+200')
root.wm_title("Data")

frame = ttk.Frame(root)
frame.pack()

tree = ttk.Treeview(frame, height=30)

style = ttk.Style()
style.configure(".", font=("Helvetica", 16))
style.configure("Treeview.Heading", font=("Helvetica", 16))

tree["columns"] = ("one", "two", "three")
tree.column("#0", width=600)
tree.column("one", width=600)
tree.column("two", width=200)
tree.column("three", width=200)

tree.heading('#0', text="Bom Line")
tree.heading("one", text="Item Description")
tree.heading("two", text="Part Name")
tree.heading("three", text="Part Number")

# 1th level
id0 = tree.insert("", 0, "dir0", text="Pivot Bearing with Wheel Hub-101BG/001",
                  values=("Pivot Bearing Assembly with Wheel Bearing",))

# 2th level
id00 = tree.insert(id0, "end", "dir00", text="Pivot Bearing Assembly with Bushs 101TJ/001",
                   values=("Pivot Bearing Assembly with Bushs",))
id01 = tree.insert(id0, "end", "dir01", text="Assembling Set Pivot Bearing with Wheel_Bearing- 101HXU/036",
                   values=("Assembling Set Pivot Bearing with Wheel_Bearing",))
# 3th level
id000 = tree.insert(id00, "end", "dir000", text="Pivot Bearing Processed Part- 101VGH/001",
                    values=('Pivot Bearing Processed Part',))
id001 = tree.insert(id00, "end", "dir001", text="Assembling Set Pivot Bearing with Bushings -101HXX/087",
                    values=('Assembling Set Pivot Bearing with Bushings',))

id010 = tree.insert(id01, "end", "dir010", text="102MKI/006_100",
                    values=('not Drive Shaft left - Wheel Bearing', 'Wheel Bearing', '234.456.865.C'))
id011 = tree.insert(id01, "end", "dir011", text="103GHJ/006_200",
                    values=('Drive Shaft left - Wheel Bearing1', 'Wheel Bearing', '234.456.865.C'))
id012 = tree.insert(id01, "end", "dir012", text="103GGJ/006_300",
                    values=('Drive Shaft left - Wheel Bearing2', 'Wheel Bearing', '234.456.865.D'))
id013 = tree.insert(id01, "end", "dir013", text="102GHY/007_100",
                    values=('fasten Wheel Bearing an Pivot Bearing', 'Internal Gear Bolt', '786.623.126.'))
# 4th level
id0000 = tree.insert(id000, "end", "dir0000", text="Pivot Bearing Raw Part- 101CCF/001",
                     values=('Pivot Bearing Raw Part',))
id0001 = tree.insert(id000, "end", "dir0001", text="102WDR/002_100",
                     values=('Pivot Bearing (Radial, left)', 'Pivot Bearing', '123.456.788.A'))
id0002 = tree.insert(id000, "end", "dir0002", text="102FCF/002_200",
                     values=('Pivot Bearing (Radial, left)', 'Pivot Bearing', '123.456.788.B'))

id0010 = tree.insert(id001, "end", "dir0010", text="102EFX/003_100",
                     values=('Guide Link Bushing - Bearing Hole', 'Bearing Hole', '234.456.376.'))
id0011 = tree.insert(id001, "end", "dir0011", text="102FTH/004_100",
                     values=('Bushing', 'Bushing', '655.456.199.'))
id0012 = tree.insert(id001, "end", "dir0012", text="102XDE/005_100",
                     values=('Support Link Bushing - Bearing Hole', 'Bearing Hole', '234.456.376.'))
# 5th level
id00000 = tree.insert(id0000, "end", "dir00000", text="102TYH/001_100",
                      values=('Pivot Bearing (Radial, left)', 'Pivot Bearing', '123.456.789.A'))

# tree.grid(row=0,column=0,sticky=NSEW)
tree.pack()

# root loop
root.mainloop()
