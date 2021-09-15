import os,shutil
dict_extension = {
    "audio_extension" : (".mp3",".m4a",".wav",".flac",".pcm",".aiff",".aac",".ogg",".wma",".alac",".asf",".asx",".cda",".m4b",".wpl"),
    "video_extension" : (".mp4",".mkv",".MKV",".flv",".mpeg",".avi",".riff",".3gp",".mov",".M2TS",".vob",".aac",".xvid",".DivX",".mpg","m4v"),
    "document_extension" : (".doc",".pdf",".txt",".html",".odf",".ods",".odp",".docx",".xls",".xlsx",".ppt",".pptx",".odt",".pages",".pptm",".xps"),
    "image_extension": (".jpeg",".jpg",".png",".tga",".tif",".tiff",".wbmp",".JPG")
}

folderpath = input("enter folder path : ")

def file_finder(folder_path,file_extension):
    return [file for file in os.listdir(folderpath) for extension in file_extension if file.endswith(extension)]

for extension_type,extension_tuple in dict_extension.items():
    folder_name = extension_type.split("_")[0] + "files"
    folder_path = os.path.join(folderpath,folder_name)
    
    if os.path.exists(folder_path):
        print(f"{folder_name} folder already exists")
    
    else:
        for file in file_finder(folderpath,extension_tuple):
            for extension in extension_tuple:
                if file.endswith(extension):
                    if os.path.exists(folder_path):
                        continue
                    else:
                        os.mkdir(folder_path)

    for item in file_finder(folderpath,extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)