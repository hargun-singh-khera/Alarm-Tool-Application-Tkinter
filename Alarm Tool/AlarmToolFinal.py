# Import Required Library
from tkinter import *
from threading import *
from tkinter import messagebox
from playsound import playsound
import time
import os

# Class for AlarmTool
class AlarmTool():
    # The init method or constructor to initialize the GUI application with clock and widgets functions
    def __init__(self, root):
        self.root = root
        # Set the title of the GUI Project
        self.root.title("Alarm Tool")

        # Set Geomtery size of GUI
        self.root.geometry("400x500")

        # Set the background color of GUI
        self.root.config(bg="#c5d5cb")

        # Blocking the user from making the GUI in full screen
        self.root.resizable(0,0)

        # Calling the clock function to display the clock
        self.clock()
        # Calling the widgets function to display the required widgets in the GUI
        self.createWidgets()

    # Funciton to display system clock in the application
    def clock(self):

        # Initializing root object
        self.root = root
        # Used to set 12-hour format same as system
        self.system_hour = time.strftime("%I")
        # Used to set system min
        self.system_min = time.strftime("%M")
        # Used to set system second
        self.system_sec = time.strftime("%S")
        # Used to set system day
        self.day = time.strftime("%A")
        # Used to set whether time is in AM or PM
        self.am_pm = time.strftime("%p")
        # Used to set time zone of the device like(IST)
        self.time_zone = time.strftime("%Z") 
        
        # Clock_label used to display time in application
        self.clock_label = Label(root, text=self.system_hour + ":" + self.system_min + ":" + self.system_sec + " " + self.am_pm, font="Helvetica 48",fg="green",bg="black")
        self.clock_label.place(x=14,y=10)

        # Used to update the clock after every 1000 milliseconds
        self.clock_label.after(1000,self.update)    

        # It displays the time zone of the system
        self.time_zone_day = Label(root, text=self.time_zone + "\n"+ self.day, font="Helvetica 14",fg="green",bg="#c5d5cb")
        self.time_zone_day.place(x=110,y=100)

    # Function used to update the clock time
    def update(self):
        self.clock() 

    # Function used to create the widgets for the Alarm Tool GUI Application
    def createWidgets(self):
        
        # Label used to display "Set time for Alarm: " in the GUI Application
        self.setYourAlarm = Label(root, text="Set Time for Alarm: ",fg="white",bg="#D2691E",relief="solid", font="Helevetica 15 bold").place(x=10,y=180)

        # Label used to display "What is this Alarm for?: " in the GUI Application
        self.messageforAlarm = Label(root, text="What is this Alarm for?",fg="white",bg="#FF8C00",relief="solid", font="Helevetica 15 bold").place(x=10,y=230)

        # Declaration of Tkinter variables
        self.hour = IntVar()
        self.minute = IntVar()
        self.ampmuser = StringVar()
        self.messageforAlarmvalue = StringVar()
    
        # Spinbox for choosing the hour user you want to set
        self.shour = Spinbox(width=3,from_=1, to=12, state="readonly", font="Helvetica 15", textvariable=self.hour, wrap=True)
        self.shour.place(x=215,y=180)

        # Spinbox for choosing the minute user you want to set
        self.smin = Spinbox(width=3,from_=00, to=59, state="readonly", font="Helvetica 15", textvariable=self.minute, wrap=True,format="%02.0f")
        self.smin.place(x=275,y=180)

        # List for the options of "AM" and "PM"
        self.sampmlist = ['AM','PM']

        # Spinbox containing the list of AM and PM options user want to set
        self.sampmuser = Spinbox(width=3,values=self.sampmlist, state="readonly", font="Helvetica 15",  textvariable=self.ampmuser, wrap=True)
        self.sampmuser.place(x=335,y=180)

        # Entry widget to allow the user to enter the message for the Alarm
        self.alarmMessage = Entry(root, textvariable=self.messageforAlarmvalue,bg="#E5E4E2",width=13,font="Helvetica 15")
        self.alarmMessage.place(x=240,y=232,height=25)
        
        # Button used to set the alarm by user
        self.button = Button(root, text="Set Your Alarm",command=self.Threading,font="Helevetica 12 bold", activebackground="Orange").place(x=140,y=280)    

    # Displaying pop up messgae to the user that the time for alarm is set : {time_given_by_user}
    def message(self):
        # Used for modifying the text with text in Label countAlarm
        self.countAlarm.config(text=" The alarm is counting . . . ")

        # If minute value has only one digit like 0 to 9 then concatenate string 0 before with these numbers
        if self.minute.get() < 10:
            messagebox.showinfo("Alarm Tool",f"The alarm is set to: {self.hour.get()}:{str(0)+str(self.minute.get())} {self.ampmuser.get()}")

        else:      
            messagebox.showinfo("Alarm Tool",f"The alarm is set to: {self.hour.get()}:{self.minute.get()} {self.ampmuser.get()}")   


    # Use Threading
    def Threading(self):
        t1 = Thread(target=self.submit)
        t1.start()    

    # Submit function called when pressed Set Alarm button
    def submit(self):
        
        # Label used to display "The alarm is counting" and for displaying "Playing Alarm Sound" in the GUI Application
        self.countAlarm = Label(root, text="", font="Helevetica 13 bold",fg="white",bg="#FF0000")
        self.countAlarm.place(x=10,y=325)

        # Check if the time given by user is in PM and is it is less than 12
        if self.ampmuser.get() == 'PM' and self.hour.get() < 12:
            # Increment hour time set by user by 12
            # If minute value has only one digit like 0 to 9 then concatenate string 0 before with these numbers
            if self.minute.get() < 10:  
                set_alarm_time = f"{self.hour.get()+12}:{str(0)+str(self.minute.get())}:00"    
            else:      
                set_alarm_time = f"{self.hour.get()+12}:{self.minute.get()}:00"

        else:
            # If minute value has only one digit like 0 to 9 then concatenate string 0 before with these numbers
            if self.hour.get() < 10 and self.minute.get() < 10:  
                set_alarm_time = f"{str(0)+str(self.hour.get())}:{(str(0)+str(self.minute.get()))}:00"
            elif self.hour.get() < 10:
                set_alarm_time = f"{str(0)+str(self.hour.get())}:{self.minute.get()}:00"
            elif self.minute.get() < 10:
                set_alarm_time = f"{self.hour.get()}:{str(0)+str(self.minute.get())}:00"
            else:      
                set_alarm_time = f"{self.hour.get()}:{self.minute.get()}:00"


        # Calling the message function to display pop up message to the user
        self.message()

        # Calling the alarm which checks whether the time set by user is equal to the current time        
        self.alarm(set_alarm_time)                  

    # Set Alarm function
    def alarm(self,set_alarm_time):
        # Infinite Loop
        while True:
            # Get current time
            current_time = time.strftime("%H:%M:%S")
            print(current_time,set_alarm_time)
            # Wait for one seconds
            time.sleep(1)
            
            # Assigning the value entered by user in the message entry box
            alarmmessage = self.alarmMessage.get() 

            # Check whether set alarm is equal to current time or not       
            if current_time==set_alarm_time:
                print("Playing Alarm Sound ...")    
                
                # Displaying Alarm sound playing label in GUI
                self.countAlarm.config(text=" Alarm Sound Playing >>>> ",bg="#0000A5")

                # Displaying the message entered by user iff user has given some message while setting the alarm
                if(alarmmessage != ""):
                    messagebox.showinfo("Alarm Tool(Message)", f"The message is: {alarmmessage}")
                
                # Playing sound
                playsound('C:/Users/user/Desktop/Python GUI Project/MV27TES-alarm.mp3') 
                break
        
        # Used for modifying the text with empty text in Label countAlarm after Alarm Sound Rung successfully
        self.countAlarm.config(text="",bg="#c5d5cb")              
    

# Create Tkinter Object
root = Tk()

# Passing root to AlarmTool class
alrmt = AlarmTool(root)

# Execute Tkinter
root.mainloop()        
