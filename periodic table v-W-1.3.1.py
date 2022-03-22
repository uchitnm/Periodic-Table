from tkinter import *
from tkinter import messagebox
import json

with open('main.json',encoding="utf8") as f:
    main = json.load(f)
    # print(type(main))
    f.close()
    
def prop(a):
    # win=Tk()
    data=''
    # win.config(background='darksalmon')
    d=("name",'number','atomic_mass','category','electron_configuration','phase','discovered_by','period')
    # win.title(str(a).capitalize())
    for h,p in enumerate(d):
            # Label(win,text=('    %d ) %a : %a')%(h+1,str(p).capitalize(),str(main[a][p]).capitalize())).pack(side= TOP, anchor="w")
            data += (('    %d ) %a : %a\n')%(h+1,str(p).capitalize(),str(main[a][p]).capitalize()))

    messagebox.showinfo(title=str(a).capitalize(),message=data)
          
    # win.mainloop()
    # print(a)


def about():
    messagebox.showinfo(" Credits", "Click on Elements symbol to know it\'s properties."+'\n\n'+'Coded and Develooped by Uchit.N.M')


window = Tk()
window.title('Modern Periodic Table 1.3.1')
main_keys = main.keys()


bar = Menu(window)
about_menu = Menu(bar, tearoff=0)
about_menu.add_command(label="Credits", command=about)
about_menu.add_separator()
about_menu.add_command(label="Exit", command=exit)
bar.add_cascade(label="About", menu=about_menu)
window.config(menu=bar)

for a in range(18):
    Label(window, height=3, width=6, text=(a+1)).grid(column=a+1, row=0)

for b in range(0, 7):
    Label(window, height=3, width=6, text=(b+1)).grid(column=0, row=b+1)

for c in main_keys:

    if (main[c]['xpos']) in (1, 2) and (main[c]['ypos']) in range(2, 8):

        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),
               background='pink',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif main[c]['symbol'] == 'H':
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),
               background='red',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif (main[c]['xpos']) in range(3, 13) and (main[c]['ypos']) in range(2, 8):
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),
               background='grey',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif (main[c]['xpos']) in range(13, 18) and (main[c]['ypos']) in range(2, 8):
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),
               background='yellow',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif (main[c]['xpos']) == 18 and (main[c]['ypos']) in range(1, 8):
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),
               background='gold',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif (main[c]['ypos']) == 9:
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),              
               background='blue',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    elif (main[c]['ypos']) == 10:
        Button(window, height=3, width=7, text=(str(main[c]['number'])+':'+main[c]['symbol']),              
               background='lightgreen',command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    else:
        Button(window, height=3, width=7, text=(str(
            main[c]['number'])+':'+main[c]['symbol']),command= lambda c=c :prop(c)).grid(column=(main[c]['xpos']), row=(main[c]['ypos']))

    Button(window, height=3, width=7, text=('Lanthanides'),foreground='blue').grid(column=3, row=6)
    Button(window, height=3, width=7, text=('Actinides'),foreground='green').grid(column=3, row=7)

window.mainloop()
