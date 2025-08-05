# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
import comboBox

# Create Object
root = Tk()

# Set geometry
root.geometry("500x400")

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()


def alarm():
	alarm_check = False
	do_snooze = False
	while alarm_check == False:
		# print(hour_now.get(),min_now.get(),sec_now.get())
		set_alarm_time = f"{hour_now.get()}:{min_now.get()}:{sec_now.get()}"
		# print(set_alarm_time)

		# Wait for one seconds
		time.sleep(1)

		if alarm_check == True:
			break

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		# print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
			alarm_check = True

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour_now = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23')
hour_now.set(hours[0])
hrs = comboBox.comboBox(root, hours, 100, 100, hour_now)

min_now = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
min_now.set(minutes[0])
mins = comboBox.comboBox(root, minutes, 200, 100, min_now)

sec_now = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
sec_now.set(seconds[0])
secs = comboBox.comboBox(root, seconds, 300, 100, sec_now)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).place(x = 200, y = 150)

# Execute Tkinter
root.mainloop()
