import sys
import subprocess

REQUIRED_PYTHON = (3, 8)
REQUIRED_PYINSTALLER = (4, 0)

# Needs quite a few updates, but supplying platform as an optional argument is good (default to detected OS)

def check_python_version():
    if sys.version_info < REQUIRED_PYTHON:
        print(f"Python version must be {REQUIRED_PYTHON} or higher.")
        sys.exit(1)

def check_pyinstaller_version():
    try:
        import PyInstaller
        if PyInstaller.__version__ < REQUIRED_PYINSTALLER:
            print(f"PyInstaller version must be {REQUIRED_PYINSTALLER} or higher.")
            sys.exit(1)
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def install_requirements():
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def build_project():
    print("Building project...")
    subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile", "your_main_script.py"])

if __name__ == "__main__":
    check_python_version()
    check_pyinstaller_version()
    install_requirements()
    build_project()