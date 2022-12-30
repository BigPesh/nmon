from datetime import datetime

import psutil
import tkinter as tk
import os
import subprocess
import platform
from openpyxl import Workbook

# Create a new workbook to store the data
workbook = Workbook()
sheet = workbook.active
sheet.append(["Total megabytes sent", "Total megabytes received", "Current download speed", "Current upload speed"])

# Set up the GUI
window = tk.Tk()
window.title("Nmon - https://grant-peach-blog.web.app - @BIG_PESH")
window.geometry("480x230")
window.resizable(False, False)
window.configure(bg="#1cff9f")
title_lbl = tk.Label(window, text="Nmon v1.0.0 - @BIG_PESH ", font=("Arial", 20), fg="#6638f0", background="#1cff9f")
title_lbl.pack()


# Function to stop the update label function
def stop():
    window.destroy()


# Function to delete the workbook
def delete_workbook():
    os.remove("Network Usage.xlsx")
    label4.config(text="Workbook deleted", fg="red")


# function to ping google to check if the internet is working
def ping():
    # Ping google
    # Run the ping command
    response = os.system("ping -c 1 google.com")
    today = datetime.now()
    # Check the response
    if response == 0:
        label1.config(fg="black", background="#1cff9f")
        label2.config(fg="black", background="#1cff9f")
        label3.config(fg="black", background="#1cff9f")
        label4.config(text="Internet connection: OK", fg="blue", background="#1cff9f")
        window.configure(bg="#1cff9f")
    else:
        label1.config(fg="white", background="red")
        label2.config(fg="white", background="red")
        label3.config(fg="white", background="red")
        label4.config(text="Internet connection: ERROR", fg="white", background="red")
        window.configure(bg="red")
        sheet.append([f"{today.strftime('%d/%m/%y %H:%M')} - Internet connection: ERROR"])


# Function to open the workbook
def open_workbook(workbook_path):
    # Get the current operating system
    os_name = platform.system()

    # Call the appropriate command for opening the workbook
    if os_name == "Windows":
        subprocess.run(["start", workbook_path], check=True)
    elif os_name == "Darwin":  # macOS
        subprocess.run(["open", workbook_path], check=True)
    elif os_name == "Linux":
        subprocess.run(["xdg-open", workbook_path], check=True)
    else:
        print(f"Unable to open workbook on {os_name}.")


def start():
    # Start updating the label
    update_label()


# Create a label to display the current network usage
label1 = tk.Label(window, background="#1cff9f")
label1.pack()
label2 = tk.Label(window, background="#1cff9f")
label2.pack()
label3 = tk.Label(window, background="#1cff9f")
label3.pack()
label4 = tk.Label(window, background="#1cff9f")
label4.pack()
but = tk.Button(window, text="Start", background="#1cff9f", command=start)
but.pack()
but1 = tk.Button(window, text="Load Data Sheet", command=lambda: open_workbook("Network Usage.xlsx"))
but1.pack()
but2 = tk.Button(window, text="Delete Data Sheet", command=delete_workbook)
but2.pack()
but3 = tk.Button(window, text="Quit", command=stop)
but3.pack()


# Create a function to update the label with the current network usage
def update_label():
    # Get the current network statistics
    title_lbl.destroy()
    ping()
    net_stats = psutil.net_io_counters()
    bytes_sent = net_stats.bytes_sent
    bytes_recv = net_stats.bytes_recv
    # Calculate the download and upload speeds
    global prev_bytes_recv, prev_bytes_sent
    try:
        download_speed = (bytes_recv - prev_bytes_recv) / 1024 / 1024
        upload_speed = (bytes_sent - prev_bytes_sent) / 1024 / 1024
    except NameError:
        download_speed = 0
        upload_speed = 0
    prev_bytes_recv = bytes_recv
    prev_bytes_sent = bytes_sent
    # Convert the bytes to megabytes
    megabytes_sent = bytes_sent / 1024 / 1024
    megabytes_recv = bytes_recv / 1024 / 1024
    # Update the labels with the megabytes sent and received and the download and upload speeds
    label1.config(text=f"Total megabytes sent: {megabytes_sent:.2f}\nTotal megabytes received: {megabytes_recv:.2f}")
    label2.config(text=f"Current download speed: {download_speed:.2f} MB/s")
    label3.config(text=f"Current upload speed: {upload_speed:.2f} MB/s")
    # Write the data to the sheet
    sheet.append([megabytes_sent, megabytes_recv, f"{download_speed:.2f} MB/s", f"{upload_speed:.2f} MB/s"])
    # Save the workbook
    workbook.save("Network Usage.xlsx")
    window.after(1000, update_label)


# Run the GUI loop
window.mainloop()
