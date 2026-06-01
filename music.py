import subprocess

set_media_volume = int(input("volume music = ")

def set_media_volume(level):
    """level = 0 ถึง 15"""
    subprocess.run(['termux-volume', 'music', str(level)])
  
print(set_media_volume)
