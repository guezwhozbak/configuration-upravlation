"Точка входа в программу"

import argparse
from src.shell import ShellGUI

def main():
    parser = argparse.ArgumentParser(description='Shell Emulator')
    parser.add_argument('--hostname', type=str, required=True, help='Hostname for the shell prompt')
    parser.add_argument('--fs_path', type=str, required=True, help='Path to the virtual file system zip file')
    parser.add_argument('--log_path', type=str, required=True, help='Path to the log file')
    parser.add_argument('--startup_script', type=str, required=True, help='Path to the startup script')

    args = parser.parse_args()

    shell = ShellGUI(args.hostname, args.fs_path, args.log_path, args.startup_script)
    shell.run()

if __name__ == '__main__':
    main()







