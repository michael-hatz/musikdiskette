#***** source ~/.bashrc && /usr/bin/python3 /home/pi/Desktop/Music/music.py

import subprocess
import vlc
import os
import time
import pyudev
from threading import Thread
import re
import os
import time
global running
global stop_flag
global changetimer
running = True
stop_flag = False
p = vlc.MediaPlayer()
changetimer = 0

def parse_m3u8(file_path):
    segments = []
    metadata = {}
    
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            if line.startswith('#EXTINF'):
                duration = re.search(r'#EXTINF:(\d+(\.\d+)?)', line)
                if duration:
                    metadata['duration'] = float(duration.group(1))
            elif line.startswith('#EXT-X-STREAM-INF'):
               
                info = re.findall(r'(\w+)=["\']([^"\']+)["\']', line)
                for key, value in info:
                    metadata[key] = value
       
        elif line:  
            segments.append({'url': line, 'metadata': metadata})

            metadata = {}

    return segments

def monitor_usb():
    global running
    global stop_flag
    global changetimer

    context = pyudev.Context()
    

    monitor = pyudev.Monitor.from_netlink(context)

    for device in iter(monitor.poll, None):
        if device.action == 'change': #and device.get('ID_USB_DRIVER'):
            changetimer = changetimer + 1

        print(changetimer)

        if changetimer >= 2 and changetimer % 3 != 0 and changetimer %2 == 0:
            print(f"Floppy disk inserted: {device.device_node}")
            stop_flag = False

            befehl = f"sudo mount {device.device_node} /media/pi/disk"
            print(befehl)

            os.system(befehl)
            time.sleep(6)
            print("mounting")
            
            partition = device.get('ID_FS_LABEL')
            print(partition)

            mount_point = '/media/pi/disk'

            print(mount_point)
            if mount_point:
                print("Checking for '1.txt' in USB drive...")
                time.sleep(5)
                file_path = os.path.join(mount_point, 'playlist.m3u8')
                print("file_path: ", file_path)
                
                if os.path.isfile(file_path):
                    print("'1.txt' found. Starting to print content...")

                    running = True

                    
                    Thread(target=print_file_content, args=(file_path,)).start()
                else:
                    print("'1.txt' not found.")
        elif changetimer % 3 == 0:
            print("Auswurf Diskette")
            os.system('sudo umount /media/pi/disk')
            time.sleep(4)
          
            running = False
            stop_flag = True

            p.stop()


def get_mount_point(device):
    # This function gets the mount point of the USB device
    for part in device.children:
        if part.get('ID_FS_LABEL') and part.get('ID_FS_LABEL') != '':
            mount_point = os.path.join('/media', part.get('ID_FS_LABEL'))
            if os.path.ismount(mount_point):
                return mount_point
    return None

def print_file_content(file_path):
    global running
    global stop_flag
    while running:

        print("running", running)
        
        playlist_path = file_path
        print(playlist_path)
        mp3_path = r'/home/pi/Music'
        segments = parse_m3u8(playlist_path)
        prefix = "file://"
        
        media_player = vlc.MediaListPlayer() 

        player = vlc.Instance() 
          
        media_list = player.media_list_new() 
        for segment in segments:

            music_file = os.path.join(mp3_path, segment['url'])
            music_file = segment['url']
            music_file = music_file[len(prefix):]
            music_file = music_file.replace("%20", " ")
            music_file = music_file.replace("%E2%80%99" , "’")
            music_file = music_file.replace("%E2%80%A6" , "…")
            print(music_file)
            media = player.media_new(music_file)
            media_list.add_media(media) 
        
        print(media_list)
        media_player.set_media_list(media_list) 
        
         
        media_player.play() 
        
        while not stop_flag:
            time.sleep(1)
            
        
        media_player.stop()
 
if __name__ == "__main__":
    try:
        monitor_usb()
    except KeyboardInterrupt:
        print("Monitoring stopped.")