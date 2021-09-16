from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
from PIL import Image, ImageTk

win = tk.Tk()

win.title("Document separator")
win.geometry('550x300+420+200')
win.wm_iconbitmap('')
win.wm_resizable(width=False, height=False)

# set main window background to black
win.config(background='black')

# Header
label1 = ttk.Label(win, text="DOCUMENT SEPARATOR", font=(
    'verdana', 15, 'bold'), background='black', foreground='green')
label1.pack()

# creating label
usernamelbl = ttk.Label(win, text='Username -', font=("helvetica",
                        10, 'bold'), background='black', foreground='orange')

pathlbl = ttk.Label(win, text='Input path -', font=("helvetica",
                    10, 'bold'), background='black', foreground='orange')

thxlbl = ttk.Label(win,text='',font=("helvetica",
                        10, 'bold'),width=65,background='black',foreground='orange')

# positioning label
usernamelbl.place(x=30, y=60)
pathlbl.place(x=30, y=120)
thxlbl.place(x=53,y=210)
# variable - entry box
namevar = tk.StringVar()
pathvar = tk.StringVar()

# create entry boxes
usernameentry = tk.Entry(win, textvariable=namevar, width=22,
                         background='grey', font=('Aerial', 11, 'bold'))
pathentry = tk.Entry(win, textvariable=pathvar, width=30,
                     background='grey', font=('Aerial', 11, 'bold'))

# positioning the entry boxex
usernameentry.place(x=126, y=60, height=22)
pathentry.place(x=125, y=120, height=25)

# browsebtn functionality
download_dir = ''

def open_path():
    global download_dir
    download_dir = filedialog.askdirectory(initialdir=os.getcwd(
    ), title='Select Path')
    pathvar.set(download_dir)
    # pathentry.config(foreground='darkgreen')

username = namevar.get()

def process():
    dict_extensions = {'audio_extensions': (".mp3", ".m4a", ".wav", ".flac", ".pcm", ".aiff", ".aac", ".ogg", ".wma", ".alac", ".asf", ".asx", ".cda", ".m4b", ".wpl"),
                       'video_extensions': (".mp4", ".mkv", ".MKV", ".flv", ".mpeg", ".avi", ".riff", ".3gp", ".mov", ".M2TS", ".vob", ".aac", ".xvid", ".DivX", ".mpg", "m4v"),
                       'documents_extensions': (".doc", ".pdf", ".txt", ".html", ".odf", ".ods", ".odp", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".pages", ".pptm", ".xps"),
                       'image_extensions': (".jpeg", ".jpg", ".png", ".tga", ".tif", ".tiff", ".wbmp", ".JPG")
                       }
    def file_finder(folder_path,file_extension):
        global inputpath
        inputpath = pathvar.get()
        files = []
        for file in os.listdir(inputpath):
            for extension in  file_extension:
                if file.endswith(extension):
                    files.append(file) 
        return files
    for extension_type , extension_tuple in dict_extensions.items():
        folder_name = extension_type.split('_')[0] + 'files' # to extract foldername from extension 
        inputpath =  pathvar.get()
        folder_path = os.path.join(inputpath,folder_name)
        if os.path.exists(folder_path):
            msg1 =messagebox.showinfo('already exist',f'{folder_name} is already exist')
        else:
            for file in file_finder(inputpath,extension_tuple):
                for extension in extension_tuple:
                    if file.endswith(extension):
                        if os.path.exists(folder_path):
                            continue
                        else:
                            os.mkdir(folder_path) 
                            # if msg1:
                            #     messagebox.showinfo('Completed',f'{folder_name} is already exist \n {folder_name} folder created')
                            
                            messagebox.showinfo('completed',f'{folder_name} folder created')    
                                                       
        for item in file_finder(inputpath,extension_tuple):
            item_path = os.path.join(inputpath,item)
            item_new_path = os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)   
    if username=="":
        thxlbl.config(text='Thank you !! for using the application. \n Hope you like it ')                                   
    else:
        thxlbl.config(text=f'Thank you {username} for using the application. \n Hope you like it ')   



# button
browsebtn = tk.Button(win, text="Browse", width=9, command=open_path,
                      relief=RIDGE, bg='#9c2d2c', fg='white', font=('verdana', 9, 'bold'))

processbtn = tk.Button(win, text=" Start Process ", width=12, command=process,
                       relief=RIDGE, bg='#9c2d2c', fg='white', font=('verdana', 9, 'bold'))

# positioning button
browsebtn.place(x=372, y=120)
processbtn.place(x=210, y=180)

win.mainloop()
