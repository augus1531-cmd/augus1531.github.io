import subprocess

def set_media_volume(level):
    subprocess.run(['termux-volume', 'music', str(level)])

level = int(input("ใส่ระดับเสียง (0-15): "))
set_media_volume(level)
