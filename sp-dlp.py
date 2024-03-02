import os
import subprocess
import sys
from pystyle import Colors

red = Colors.red
green = Colors.green
cyan = Colors.cyan
white = Colors.white

def spload(spurl, gffmpeg=None, gspotdl=None):
    if gffmpeg and os.path.isfile(gffmpeg):
        print(f"{green}Starting Download...")
        print(f"{cyan}Using ffmpeg:{white}", gffmpeg)
        os.environ["PATH"] += os.pathsep + os.path.dirname(gffmpeg)
    else:
        print(f"{red}Error: ffmpeg not found")
        
    if gspotdl and os.path.isfile(gspotdl):
        os.environ["PATH"] += os.pathsep + os.path.dirname(gspotdl)
    else:
        print(f"{red}Error: spotdl not found")

    try:
        subprocess.check_call([gspotdl, "--ffmpeg", gffmpeg, spurl])
    except subprocess.CalledProcessError as e:
        print(f"{red}Failed to download song from Spotify.")
        print(f"Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(f"{cyan}Usage: {sys.executable} {green}<Spotify URL>")
        sys.exit(1)
    
    spurl = sys.argv[1]
    
    if getattr(sys, 'frozen', False):
        gffmpeg = os.path.join(sys._MEIPASS, "ffmpeg.exe")
        gspotdl = os.path.join(sys._MEIPASS, "spotdl.exe")
    elif os.path.isfile("ffmpeg.exe") and os.path.isfile("spotdl.exe"):
        gffmpeg = "ffmpeg.exe"
        gspotdl = "spotdl.exe"
    else:
        print(f"{red}ffmpeg.exe or spotdl.exe not found. {cyan}(You can add it manually to the directory)")
        sys.exit(1)
    
    spload(spurl, gffmpeg, gspotdl)
