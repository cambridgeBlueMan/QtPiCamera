import subprocess

list_files = subprocess.run(["ffmpegthumbnailer",  "-i" ,  "vid.h264",  "-o",  "vidthumb.jpeg"])
#ffmpegthumbnailer -i vid.h264 -o vidthumb.jpeg
print(list_files)

