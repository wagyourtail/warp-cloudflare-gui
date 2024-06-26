import os
import sys
from pathlib import Path

cur_path = sys.path[0]

os.system("pip3 install -U pip wheel setuptools")
os.system("pip3 install -r requirements.txt")
os.system("mkdir -p ~/.local/share/icons")
os.system("cp {}/icons/logo.png ~/.local/share/icons/warp_gui.png".format(cur_path))

desktop_file = '{}/.local/share/applications/warp-gui.desktop'.format(Path.home())

file = open(desktop_file, 'w+')
file.write(f'''[Desktop Entry]
Name=Warp Cloudflare 
Version=1.0
Comment=A gui app base on warp-cli for linux
Exec=/bin/sh {cur_path}/main.sh
Icon=warp_gui
Terminal=false
Path={cur_path}
Type=Application
''')
print('Desktop file created at "{}"'.format(desktop_file))


