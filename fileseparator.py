import time
import os ,shutil
dict_extensions = {'audio_extensions' : (".mp3",".m4a",".wav",".flac",".pcm",".aiff",".aac",".ogg",".wma",".alac",".asf",".asx",".cda",".m4b",".wpl"),
'video_extensions' : (".mp4",".mkv",".MKV",".flv",".mpeg",".avi",".riff",".3gp",".mov",".M2TS",".vob",".aac",".xvid",".DivX",".mpg","m4v"),
'documents_extensions' : (".doc",".pdf",".txt",".html",".odf",".ods",".odp",".docx",".xls",".xlsx",".ppt",".pptx",".odt",".pages",".pptm",".xps"),
'image_extensions' : (".jpeg",".jpg",".png",".tga",".tif",".tiff",".wbmp",".JPG")
}

print('-------*************************************------')
print('****** WELCOME TO FILE SEPARATOR APPLICATION *****')
print('-------*************************************------')
user_name = input('Your name please :')
input_folderpath =  input('Enter folder path - ')

def file_finder(folder_path,file_extension):
    files = []
    for file in os.listdir(input_folderpath):
        for extension in  file_extension:
            if file.endswith(extension):
                files.append(file)
    return files            
# return [file for file in os.listdir(folderpath) for extension in file_extension if file.endswith(extension)]

for extension_type , extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'files' # to extract foldername from extension 
    folder_path = os.path.join(input_folderpath,folder_name)
    if os.path.exists(folder_path):
        print('--------------------------------------------')
        print(f'{folder_name} folder is alreay exist')
    else:
        for file in file_finder(input_folderpath,extension_tuple):
            for extension in extension_tuple:
                if file.endswith(extension):
                    if os.path.exists(folder_path):
                         continue
                    else:
                        os.mkdir(folder_path)
                        print('--------------------------------------------')
                        print(f'{folder_name} folder created')    

    for item in file_finder(input_folderpath,extension_tuple):
        item_path = os.path.join(input_folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)

print('--------------------------------------------')
print(f'Thank you {user_name} ! for using this application') 
print('This application is made by : Lakshya verma')
time.sleep(12)