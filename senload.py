import os
import subprocess
import sys
from pystyle import Colors

red = Colors.red
green = Colors.green
cyan = Colors.cyan
white = Colors.white

def senloader(url, smeth, senexe):
    if os.path.isfile(smeth):
        print(f"{green}Starting Download...")
        print(f"{cyan}Using {senexe}:{white}", smeth)
        os.environ["PATH"] += os.pathsep + os.path.dirname(smeth)
    else:
        print(f"{red}Error: {senexe} not found")
        sys.exit(1)

    try:
        if senexe == "yt-dlp.exe":
            subprocess.check_call([senexe, "--extract-audio", "--audio-format", "mp3", url])
        else:
            subprocess.check_call([senexe, url])
    except subprocess.CalledProcessError as e:
        print(f"{red}Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("-y", "-s"):
        print(f"""
{cyan}Usage:
{white}{sys.executable} -y (Youtube Url)
{sys.executable} -s (Spotify Url)""")
        sys.exit(1)
    
    service_flag = sys.argv[1]
    url = sys.argv[2]
    
    if getattr(sys, 'frozen', False):
        if service_flag == "-y":
            smeth = os.path.join(sys._MEIPASS, "yt-dlp.exe")
            senexe = "yt-dlp.exe"
        elif service_flag == "-s":
            smeth = os.path.join(sys._MEIPASS, "spotdl.exe")
            senexe = "spotdl.exe"
    else:
        smeth = "yt-dlp.exe" if service_flag == "-y" else "spotdl.exe"
        senexe = smeth
    
    senloader(url, smeth, senexe)
