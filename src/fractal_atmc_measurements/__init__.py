"""Package description."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("fractal_atmc_measurements")
except PackageNotFoundError:
    __version__ = "uninstalled"
