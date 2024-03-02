import os
import subprocess
import sys
from pystyle import Colors

red = Colors.red
green = Colors.green
cyan = Colors.cyan
white = Colors.white

def ytload(yturl, gyt_dlp=None):
    if gyt_dlp and os.path.isfile(gyt_dlp):
        print(f"{green}Starting Download...")
        print(f"{cyan}Using yt-dlp:{white}", gyt_dlp)
        os.environ["PATH"] += os.pathsep + os.path.dirname(gyt_dlp)
    else:
        print(f"{red}Error: yt-dlp not found")

    try:
        subprocess.check_call([gyt_dlp, "--extract-audio", "--audio-format", "mp3", yturl])
    except subprocess.CalledProcessError as e:
        print(f"{red}Failed to download audio from YouTube.")
        print(f"Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(f"{cyan}Usage: {sys.executable} {green}<YouTube URL>")
        sys.exit(1)
    
    yturl = sys.argv[1]
    
    if getattr(sys, 'frozen', False):
        gyt_dlp = os.path.join(sys._MEIPASS, "yt-dlp.exe")
    elif os.path.isfile("yt-dlp.exe"):
        gyt_dlp = "yt-dlp.exe"
    else:
        print(f"{red}yt-dlp.exe not found. {cyan}(You can add it manually to the directory)")
        sys.exit(1)
    
    ytload(yturl, gyt_dlp)
