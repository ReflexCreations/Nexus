import platform
import importlib

_platform = platform.system().lower()

try:
    PlatformModule = importlib.import_module(f".{_platform}", package="src.platform")
except ImportError:
    PlatformModule = importlib.import_module(".unsupported", package="src.platform")

os_interface = PlatformModule.Platform()