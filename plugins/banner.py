#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Name__ = "VulScanPro"
__Discription__ = "Automatic Web Vulnerability Scanner."
__Version__ = "1.0.0"
__Author__ = "Md. Nur Habib"

try:
    from colors import *
except ModuleNotFoundError:
    from plugins.colors import *
    

def BannerFunction():
    print(f"""{bold}{yellow}
          
 __      __    _  _____                 _____           
 \ \    / /   | |/ ____|               |  __ \  {blue}{__Version__}{yellow}        
  \ \  / /   _| | (___   ___ __ _ _ __ | |__) | __ ___  
   \ \/ / | | | |\___ \ / __/ _` | '_ \|  ___/ '__/ _ \ 
    \  /| |_| | |____) | (_| (_| | | | | |   | | | (_) |
     \/  \__,_|_|_____/ \___\__,_|_| |_|_|   |_|  \___/ 
     
     Automatic Web Vulnerability Scanner.

                          {red}by ＠ｔｈｅｎｕｒｈａｂｉｂ
          {reset}""")
