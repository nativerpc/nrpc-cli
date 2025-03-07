#
#   Contents:
#
#       start
#
import os
import colorama
import sys


def start():
    if '-v' in sys.argv or '--version' in sys.argv:
        print('v1.0.1')
    else:
        colorama.init()
        print('Killing processes')
        # TODO: avoid special casing
        os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe powershell.exe')
        os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe node.exe')
        os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe python.exe')
        os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe test_show.exe')
        os.system('C:\\git\\nrpc-cli\\staging_modules\\pstools\\pskill.exe test_show_client.exe')
        print('Success')

if __name__ == '__main__':
    start()
