#-*- codec: cp1251 -*-
from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox as mb 
from backend import DatabaseManager  
from PIL import ImageTk, Image
import re 
import datetime
BD = DatabaseManager() 
current_acc = []
months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
class WindowApp(Tk): 

    def __init__(self): 
        Tk.__init__(self) 
        self.geometry('1200x800') 
        self.title('Test Window.') 
        self.basic = Frame(self)
        bg = ImageTk.PhotoImage(Image.open("clouds.jpg"))
        labelbg = Label(self.basic, image = bg, text = 'his')
        labelbg.photo = bg
        labelbg.grid(row = 0, column = 0, rowspan = 4, columnspan =4, sticky = 'news') 
        for i in range(4): # basic window is 4x4 grid 
            self.basic.grid_columnconfigure(i, minsize = 200, weight = 1) 
            self.basic.grid_rowconfigure(i, minsize = 200, weight = 1)  
        self.basic.pack(fill = 'both', expand = 1)
        Button(self.basic, bd = 5, text = 'Log in', command = self.switch_to_log,bg ='#BDE4F4', font = ('Papyrus', 15), fg = "#10316B", border = 2).grid(padx = 10, pady = 50, row = 1, column = 1, sticky = 'news') 
        Button(self.basic, bd = 5, text = 'Register', command = self.switch_to_reg, bg ='#BDE4F4', font = ('Papyrus', 15), fg = "#10316B", border = 2).grid(padx = 10, pady = 50, row = 1, column = 2, sticky = 'news') 
 
    def switch_to_reg(self): 
        self.basic.forget() 
        Log.forget() 
        Menu.forget()
        Log.logentry.delete(0, END)
        Log.passentry.delete(0, END)
        Reg.pack(fill = 'both', expand = 1) 

    def switch_to_main(self): 
        Menu.forget()
        Reg.forget() 
        Log.forget() 
        Reg.realnameentry.delete(0, END)
        Reg.realsurnameentry.delete(0, END)
        Reg.logentry.delete(0, END)
        Reg.passentry.delete(0, END)
        Reg.realage.delete(0, END)
        Log.logentry.delete(0, END)
        Log.passentry.delete(0, END)
        self.basic.pack(fill = 'both', expand = 1)   
    

    def switch_to_log(self): 
        Menu.forget()
        self.basic.forget() 
        Reg.forget() 
        Reg.realnameentry.delete(0, END)
        Reg.realsurnameentry.delete(0, END)
        Reg.logentry.delete(0, END)
        Reg.passentry.delete(0, END)
        Reg.realage.delete(0, END)
        Log.pack(fill = 'both', expand = 1) 
 
    def switch_to_menu(self):
        Tic.forget()
        self.basic.forget()  
        Log.forget() 
        Reg.forget()
        Reg.realnameentry.delete(0, END)
        Reg.realsurnameentry.delete(0, END)
        Reg.logentry.delete(0, END)
        Reg.passentry.delete(0, END)
        Reg.realage.delete(0, END)
        Log.logentry.delete(0, END)
        Log.passentry.delete(0, END)
        Menu.pack(fill = 'both', expand = 1) 
        update_table()

    def switch_to_tickets(self):
        self.basic.forget()  
        Log.forget() 
        Reg.forget()
        Menu.forget()
        Tic.pack(fill = 'both', expand = 1)
 
class RegScreen(Frame): 
 
    def __init__(self, root): 
        Frame.__init__(self, root)#, bg = '#FFF7E9' 
        bg = ImageTk.PhotoImage(Image.open("cloud1.jpg"))
        labelbg = Label(self, image = bg, text = 'his')
        labelbg.photo = bg
        labelbg.grid(row = 0, column = 0, rowspan = 8, columnspan =8, sticky = 'news')
        for i in range(8): 
            self.grid_columnconfigure(i, minsize = 150) 
            self.grid_rowconfigure(i, minsize = 100)
        list = ['Real First Name', 'Real Surname', 'Personal Login', 'Password', 'Age'] 
        for i in range(len(list)): #'#FFF7E9'
            Label(self, text = list[i] + ': ', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2).grid(row = 0 + i, column = 1)# sticky = 'news' 

        self.realnameentry = Entry(self,bg ='#BDE4F4', font=("Papyrus  20"),fg = "#10316B", border = 3, width=20) 
        self.realnameentry.grid(row = 0, column = 2) 
        self.realsurnameentry = Entry(self, bg ='#BDE4F4',font=("Papyrus 20"),fg = "#10316B", border = 2,  width=20) 
        self.realsurnameentry.grid(row = 1, column = 2) 
        self.logentry = Entry(self,bg ='#BDE4F4', font=("Papyrus 20"),fg = "#10316B", border = 2,  width=20) 
        self.logentry.grid(row = 2, column = 2) 
        self.passentry = Entry(self,bg ='#BDE4F4',font=("Papyrus 20"), fg = "#10316B", border = 2,  width=20) 
        self.passentry.grid(row = 3, column = 2)  
        self.realage = Entry(self,bg ='#BDE4F4',font=("Papyrus 20"),fg = "#10316B",border = 2,  width=20 )
        self.realage.grid(row = 4, column = 2)
        #'#5F9DF7'
        back = Button(self, text = 'Log in.', command = Main.switch_to_log, bg = '#BDE4F4',fg = "#10316B",font = ('Papyrus', 15), width=17, height=2).grid(row = 5, column = 1) 
        ok1 = Button(self, text = 'OK', command = button_for_reg, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=20, height=2) 
        ok1.grid(row = 5, column = 2) 
 
class LogScreen(Frame): 
 
    def __init__(self, root): 
        Frame.__init__(self, root, bg = '#FFF7E9') 
        bg = ImageTk.PhotoImage(Image.open("plane.jpg"))
        labelbg = Label(self, image = bg, text = 'his')
        labelbg.photo = bg
        labelbg.grid(row = 0, column = 0, rowspan = 8, columnspan =8, sticky = 'news')
        for i in range(8): #login screen is 
            self.grid_columnconfigure(i, minsize = 150, weight = 1) 
            self.grid_rowconfigure(i, minsize = 100, weight = 1) 
        self.grid_rowconfigure(2, minsize = 100); self.grid_rowconfigure(1, minsize = 100, weight = 1) 
        Label(self, text = 'Personal Login:', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2).grid(row = 1, column = 6) 
        Label(self, text = 'Password:', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2).grid(row = 3, column = 6) 
        self.logentry = Entry(self,bg ='#BDE4F4', font=("Papyrus  20"),fg = "#10316B", border = 3, width=20) 
        self.logentry.grid(row = 2, column = 6) 
        self.passentry = Entry(self, border = 3, show = '*',bg ='#BDE4F4', font=("Papyrus  20"),fg = "#10316B", width=20)
        self.passentry.grid(row = 4, column = 6) 
        back = Button(self, text = 'Register', command = Main.switch_to_reg, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=20, height=2)
        back.grid(row = 6, column = 6) 
        ok = Button(self, text = 'OK', command = button_func1, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=20, height=2) 
        ok.grid(row = 5, column = 6) 
 
def button_func1():
    if len(Log.logentry.get()) == 0:
        mb.showerror("Error!", "Enter your login")
    else:
        records = BD.select_from_passengers_by_login(Log.logentry.get())
        if len(records) == 0: 
            Log.logentry.delete(0, END) 
            Log.passentry.delete(0, END) 
            mb.showerror("Error!", "Such login doesn`t exist.") 
        elif records[0][1] != Log.passentry.get(): 
            Log.logentry.delete(0, END) 
            mb.showerror("Error!", "Password isn`t correct. Try again.") 
        else: 
            current_acc.append(records[-1])
            status = "VIP" if current_acc[-1][4] > 10 else "None"
            # bg = ImageTk.PhotoImage(Image.open("profil.jpg"))
            # labelbg = Label(Menu.frame_profile, image = bg)
            # labelbg.photo = bg
            # labelbg.grid(row = 0, column = 0, rowspan = 4, columnspan = 4, sticky = 'news')
            info = Label(Menu.frame_profile, bg = '#BDE4F4',fg = "#10316B",text = f"Name: {current_acc[-1][2]}\n\n\nSurname: {current_acc[-1][3]}\n\n\nAge: {current_acc[-1][-1]}\n\n\nStatus: {status}",  font = ('Papyrus', 15))
            info.grid(row = 1, column = 0, sticky = 'news') 
            

            Main.switch_to_menu() 

def button_for_reg():
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,15}$'
    pattern2 = r'^\d{1,3}$'
    x = re.findall(pattern, Reg.passentry.get())
    y = re.findall(pattern2, Reg.realage.get() )
    if len(Reg.logentry.get())==0 or len(Reg.logentry.get())>20:
        mb.showerror("Error!", "Login should be less than 20 and more than 0 characters")
    elif len(y)!=1 or int(y[0])<=0 or int(y[0])>150:
        mb.showerror("Error!", "Age should be digit from 1-150")
    elif len(x)!=1:
        mb.showerror("Error!", "Minimum 8 and maximum 15 characters, at least one uppercase letter, one lowercase letter, one number and one special character: @$!%*?&")
    else:
        array_varible = []
        array_varible.append((Reg.logentry.get(), Reg.passentry.get(), Reg.realnameentry.get(), Reg.realsurnameentry.get(), 0, False, int(Reg.realage.get()) ))
        BD.insert_into_passengers(array_varible)
        Main.switch_to_log()

def update_table(event = None):
    for row in Menu.table.get_children():
        Menu.table.delete(row)
    if len(str(Menu.selected_city_from.get())) > 1: city_from = Menu.selected_city_from.get() 
    else: city_from = None
    if len(str(Menu.selected_city_to.get())) > 1: city_to = Menu.selected_city_to.get() 
    else: city_to = None
    if len(str(Menu.month_chosen.get())) > 1: month_index = months.index(str(Menu.month_chosen.get()))
    else: month_index = None
    #print(BD.select_from_flights(city_from, city_to, month_index))
    try:
        for row in BD.select_from_flights(city_from, city_to, month_index): Menu.table.insert('', END, values = row)
    except Exception as e: print(e)

def tickets_history():
    for i in Tic.table.get_children():
        Tic.table.delete(i)
    try:
        for row in BD.select_from_tickets_by_login(current_acc[-1][0]): Tic.table.insert('', END, values = row)
    except Exception as e: print(e)
    Main.switch_to_tickets()

def cancel_tic():
    try:
        details = Tic.table.item(Tic.table.selection())
        flight_id = int(details.get('values')[1])
        login = details.get('values')[0]
        data = BD.select_from_flights_by_flightid(flight_id)
        place = details.get('values')[2]
        dates = data[0][4]
        now = datetime.datetime.now()
        difference = dates - now
        seconds = difference.days * 3600 * 24 + difference.seconds
        if seconds<43200 :#12hour
            mb.showerror("Error!", "Cancel is not available, time difference less than 12hour")
        else:
            BD.delete_from_tickets_by_login(login, flight_id, place)
            print('canceled')
            BD.modify_tickets_in_flights(flight_id, add = True)
            selected_item = Tic.table.selection()[0]
            Tic.table.delete(selected_item)
            Main.switch_to_menu()
    except Exception as e:
        print(e)
        mb.showerror("Error!", "Choose one ticket")

def print_tic():
    try:
        details = Tic.table.item(Tic.table.selection())
        login = details.get('values')[0]
        flight_id = int(details.get('values')[1])
        cost = int(details.get('values')[3])
        place = int(details.get('values')[2])
        data = BD.select_from_flights_by_flightid(flight_id)
        names = BD.select_from_passengers_by_login(login)
        with open('ticket.txt', 'w') as k:
            k.write("Ticket"+'\n')
            k.write("Login: "+str(login) +'\n')
            k.write("Name: "+str(names[0][2]) +'\n')
            k.write("SurName: "+str(names[0][3]) +'\n')
            k.write("Age: "+str(names[0][-1]) +'\n')
            k.write("Flight ID: "+str(data[0][0]) +'\n')
            k.write("Airplane: "+str(data[0][1]) +'\n')
            k.write("Place: "+str(place) +'\n')
            k.write("From City: "+str(data[0][2]) +'\n')
            k.write("To City: "+str(data[0][3]) +'\n')
            k.write("Date Time: "+str(data[0][4]) +'\n')
            k.write("Departure Time: "+str(data[0][5]) +'\n')
            k.write("Arrival Time: "+str(data[0][6]) +'\n')
            k.write("Cost: " + str(cost) +'\n')
    except:
        mb.showerror("Error!", "Choose one ticket")

def ticket_pick(event):
    Menu.seat_chosen = True
    Menu.buy_button['state'] = 'normal'
    label_id = event.widget
    label_id = re.sub(r'^.*label(\d*)$', r'\1', str(label_id))
    if len(label_id) == 0: label_id = 0
    else: label_id = int(label_id) - 1
    disable_seatmap()
    Menu.seats[label_id]['borderwidth'] = 2
    Menu.seats[label_id]['relief'] = 'solid'
    Menu.seat_chosen_id = label_id

def ticket_buy():
    res = mb.askquestion("Attention!", "Are you sure? The payment will be done automatically.")
    if str(res) == "yes":
        try:
            status = "VIP" if current_acc[-1][4] > 10 else "None"
            coef = 0.9 if current_acc[-1][4] > 10 else 1
            classplace = Menu.status_chosen.get()
            if len(classplace) < 1: raise Exception
            if classplace == "Econom Class": addition = 0
            elif classplace == "Business Class": addition = 1000
            else: addition = 2000
            for row in BD.select_from_tickets_by_flight_id(Menu.flight_id):
                if row[2] == Menu.seat_chosen_id: 
                    raise ValueError
            BD.insert_into_tickets([(current_acc[-1][0], Menu.flight_id, Menu.seat_chosen_id, int((4000 + addition) * coef), classplace)])
            BD.modify_tickets_in_flights(Menu.flight_id, add = False)
            update_table()
            table_clear()
        except ValueError: mb.showerror("Error", "You have chosen busy seat!")
        except Exception: mb.showerror("Error", "Make sure you have chosen the parameters correctly!")

def disable_seatmap():
    for label in Menu.seats:
        label['relief'] = 'flat'

def table_selected(event = None):
    details = Menu.table.item(Menu.table.selection())
    print("table_selected func: ", details)
    Menu.flight_id = details.get('values')[0]
    data = BD.select_from_tickets_by_flight_id(Menu.flight_id)
    for i in range(60):
        Menu.seats[i]['bg'] = 'green'
    for row in data:
        if row[2] != 'A1': Menu.seats[int(row[2])]['bg'] = 'red'

def table_clear():
    for i in Tic.table.get_children():
        Tic.table.delete(i)
    for i in range(60):
        Menu.seats[i]['bg'] = 'green'

class MenuScreen(Frame): # menuscreen is 4x4 1200х800
     def __init__(self, root): 
        Frame.__init__(self, root, bg = '#BDE4F4')  #bg = '#BDE4F4'
        for i in range(4): ## 
            if i < 3: self.grid_columnconfigure(i, minsize = 320, weight = 1) 
            else: self.grid_columnconfigure(i, minsize = 240, weight = 1) 
            self.grid_rowconfigure(i, minsize = 200, weight = 1)
        ######################################################################### ticket frame
        self.frame_buy = Frame(self, bg = '#BDE4F4')# bg = '#BDE4F4'
        self.frame_buy.grid(row = 0, column = 0, columnspan = 3, rowspan = 2, sticky = 'news')  # 2x3 640x600
        for i in range(10): # 8x12 first two rows narrower
           self.frame_buy.grid_columnconfigure(i, minsize = 96, weight = 1)
           if i < 2: self.frame_buy.grid_rowconfigure(i, minsize = 60, weight = 1)
           elif 2 <= i < 6: self.frame_buy.grid_rowconfigure(i, minsize = 120, weight = 1)


        Label(self.frame_buy, text = 'From:', font = ('Papyrus', 25), bg = '#BDE4F4',fg = "#10316B").grid(row = 0, column =  1, columnspan = 2)
        self.selected_city_from = StringVar()
        #selected_city_from.set('Choose the city')
        city_from = ttk.Combobox(self.frame_buy, textvariable = self.selected_city_from)
        city_from.bind('<<ComboboxSelected>>', update_table)
        city_from['state'] = 'readonly'
        city_from['values'] = ['Almaty', 'Astana', 'Atyrau', 'Semey', 'Taraz', 'Aktobe', 'Any']
        city_from.grid(row = 1, column = 1, columnspan = 2, padx = 5)

        Label(self.frame_buy, text = 'To:', font = ('Papyrus', 25), bg = '#BDE4F4',fg = "#10316B").grid(row = 0, column =  3, columnspan = 2)
        self.selected_city_to = StringVar()
        #selected_city_to.set('Choose the city')
        city_to = ttk.Combobox(self.frame_buy, textvariable = self.selected_city_to)
        city_to.bind('<<ComboboxSelected>>', update_table)
        city_to['state'] = 'readonly'
        city_to['values'] = ['Almaty', 'Astana', 'Atyrau', 'Semey', 'Taraz', 'Aktobe', 'Any']
        city_to.grid(row = 1, column = 3, columnspan = 2, padx = 5)

        Label(self.frame_buy, text = 'Month:', font = ('Papyrus', 25), bg = '#BDE4F4',fg = "#10316B").grid(row = 0, column =  5, columnspan = 2)
        self.month_chosen = StringVar()
        #month_chosen.set('Choose the month')
        month = ttk.Combobox(self.frame_buy, textvariable = self.month_chosen)
        month.bind('<<ComboboxSelected>>', update_table)
        month['state'] = 'readonly'
        month['values'] = months + [""]
        month.grid(row = 1, column = 5, columnspan = 2, padx = 5)

        Label(self.frame_buy, text = 'Status:', font = ('Papyrus', 25), bg = '#BDE4F4',fg = "#10316B").grid(row = 0, column =  7, columnspan = 2)
        self.status_chosen = StringVar()
        #status_chosen.set('Choose the status')
        status = ttk.Combobox(self.frame_buy, textvariable = self.status_chosen)
        status.bind('<<ComboboxSelected>>', update_table)
        status['state'] = 'readonly'
        status['values'] = ['Econom Class', 'Business Class', 'First Class']
        status.grid(row = 1, column = 7, columnspan = 2, padx = 5)

        back = Button(self.frame_buy, text = 'Log out', command = Main.switch_to_main, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=8, height=1)
        back.grid(row = 0, column = 9)

        ticket = Button(self.frame_buy, text = 'tickets', command =tickets_history, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=8, height=1)
        ticket.grid(row = 1, column = 9)



        heads = ['Flight ID', 'Plane ID', 'From', 'Destination', 'Date', 'Arrival time', 'Departure time', 'Tickets available']
        self.table = ttk.Treeview(self.frame_buy, show = 'headings', columns = heads)
        self.table['columns'] = heads
        for header in heads: 
            self.table.heading(header, text = header, anchor = 'center')
            self.table.column(header, width = 70)
        self.table.bind('<Double-1>', table_selected)
        self.table.grid(row = 2, column = 1, columnspan = 8, rowspan = 2, sticky = 'news')
        ########################################################################## profile frame
        self.frame_profile = Frame(self, bg = '#BDE4F4')
        self.frame_profile.grid(row = 0, column = 3, columnspan = 1, rowspan = 4, sticky = 'news')
        for i in range(3):
            self.frame_profile.grid_rowconfigure(i, minsize = 10, weight = 1)
         
        
        ######################################################################### Seats Frame
        self.frame_seat = Frame(self, bg = '#BDE4F4') # #BDE4F4
        self.frame_seat.grid(row = 2, column = 0, columnspan = 3, rowspan = 2, sticky = 'news') #frame_seat sizes 560x600
        for i in range(5):
            self.frame_seat.grid_columnconfigure(i, minsize = 120); self.frame_seat.grid_rowconfigure(i, minsize = 112)
        self.frame_seatmap = Frame(self.frame_seat, bg = 'white', highlightbackground = 'black', highlightthickness = 1)
        self.frame_seatmap.grid(row = 0, column = 1, rowspan = 2, columnspan = 15, sticky = 'news')
        for i in range(15):
            self.frame_seatmap.grid_columnconfigure(i, minsize = 10, weight = 1)
            self.frame_seatmap.grid_rowconfigure(i, minsize = 10, weight = 1)
        self.seats = []
        self.seat_chosen = False
        self.seat_chosen_id = None
        self.flight_id = None
        for i in range(60):
            self.seats.append(Label(self.frame_seatmap, bg = 'green', text = f'{i}'))
            self.seats[-1].bind('<Double-1>', ticket_pick)
            self.seats[-1].grid(row = int(i / 15) + int(int(i / 15)/2), column = int(i % 15), sticky = 'enws', padx = 5, pady = 5)
        self.buy_button = Button(self.frame_seat, bg = '#BDE4F4', command = ticket_buy, state = 'disabled', text = 'Buy')
        self.buy_button.grid(row = 0, column = 0, sticky = 'news', padx = 7, pady = 7)

class Tickets(Frame):
    def __init__(self, root): 
        Frame.__init__(self, root, bg = '#FFF7E9') 
        bg = ImageTk.PhotoImage(Image.open("menu11.jpg"))
        labelbg = Label(self, image = bg, text = 'his')
        labelbg.photo = bg
        labelbg.grid(row = 0, column = 0, rowspan = 8, columnspan =8, sticky = 'news')
        for i in range(8): #login screen is 
            self.grid_columnconfigure(i, minsize = 150, weight = 1) 
            self.grid_rowconfigure(i, minsize = 100, weight = 1) 
        self.grid_rowconfigure(2, minsize = 100); self.grid_rowconfigure(1, minsize = 100, weight = 1) 
        back = Button(self, text = 'back', command = Main.switch_to_menu, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=8, height=1)
        back.grid(row = 0, column = 7)
        print = Button(self, text = 'print', command = print_tic, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=8, height=1)
        print.grid(row = 1, column = 7)
        cancel = Button(self, text = 'cancel', command = cancel_tic, bg = '#BDE4F4',fg = "#10316B", font = ('Papyrus', 15), width=8, height=1)
        cancel.grid(row = 2, column = 7)
        heads = ['passenger_login', 'flight_id', 'place', 'cost', 'place_status']
        self.table = ttk.Treeview(self, show = 'headings')
        self.table['columns'] = heads
        for header in heads: 
            self.table.heading(header, text = header, anchor = 'center')
            self.table.column(header, width = 70)
        self.table.grid(row = 1, column = 1, columnspan = 5, sticky = 'news')

Main = WindowApp() 
 
Reg = RegScreen(Main) 
Log = LogScreen(Main) 
Menu = MenuScreen(Main)
Tic = Tickets(Main)

Main.mainloop()
