"""nmap_wrapper.py - small wrapper example"""

import subprocess

def run_scan(target):
    print(f"Running nmap scan against {target}")
    # subprocess.run(['nmap','-sV',target])

if __name__ == '__main__':
    run_scan('127.0.0.1')
