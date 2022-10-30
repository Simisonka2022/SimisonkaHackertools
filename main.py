import pygame
from pystyle import Colors, Colorate  
import webbrowser
import time
from colorama import Fore
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
  ███████╗ ██████╗ ██╗██╗  ██╗████████╗
  ██╔════╝██╔════╝ ██║██║  ██║╚══██╔══╝
  █████╗  ██║  ███╗██║███████║   ██║   
  ██╔══╝  ██║   ██║██║██╔══██║   ██║   
  ███████╗╚██████╔╝██║██║  ██║   ██║   
  ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝""",1))

time.sleep(2)
name = input(Fore.LIGHTWHITE_EX + ' Whats Your Name? ')
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(2)
print(' Welcome', name)
time.sleep(2)
url = "https://www.google.com/search?q=hack "+name
webbrowser.open_new(url)
time.sleep(3)
webbrowser.open('https://discord.gg/MJQqT2QK')