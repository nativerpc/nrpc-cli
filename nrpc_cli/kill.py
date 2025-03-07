#
#   Contents:
#
#       start
#
import os
import colorama


def start():
    colorama.init()
    print('Killing processes')
    os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe powershell.exe')
    os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe python.exe')
    print('Success')

if __name__ == '__main__':
    start()
