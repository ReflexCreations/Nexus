import os
import sys

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, src_dir)

from src.application import Application

def main():
    Application()

if __name__ == "__main__":
    main()