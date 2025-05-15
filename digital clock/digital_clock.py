# Import the tkinter module for GUI and strftime to get formatted time/date
import tkinter as tk
from time import strftime

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")  # Set the window title

# Define a function that updates the clock every second
def time():
    # Get the current time and date in formatted string
    string = strftime(" %H:%M:%S %p \n %d/%m/%y")
    # Update the text of the label with the current time/date
    label.config(text=string)
    # Call this function again after 1000 milliseconds (1 second)
    label.after(1000, time)

# Try to use a digital-style font; if not available, use Arial
try:
    clock_font = ("DS-Digital", 100, "bold")  # Try using DS-Digital font
except:
    clock_font = ("Arial", 100, "bold")       # Fallback to Arial if DS-Digital is not found

# Create a label widget to display the time/date
label = tk.Label(
    root,
    font=clock_font,          # Set the clock font
    background="black",       # Set background color
    foreground="blue"         # Set text color
)
label.pack(anchor="center")   # Center the label in the window

# Start the clock function
time()

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
