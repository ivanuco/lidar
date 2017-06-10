from distutils.core import setup
#import py2exe
from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["numpy.lib.format"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="lasviewer",
      version="0.1",
      description="Aplicacion que visualiza una lista de ficheros LiDAR",
      author="Ivan del Viejo",
      author_email="ivandelviejo@gmail.com",
      url="https://github.com/ivanuco",
      license="GPL",
      options = {"build_exe": build_exe_options},
      executables = [Executable("./src/viewer/lasviewer.py", base=base)]
########      py2exe
#       scripts=['./src/viewer/lasviewer.py'],
#       console=['./src/viewer/lasviewer.py'],
#       options={"py2exe": {"bundle_files": 1,"includes":["./src/viewer/glviewer.py"]}},
#       zipfile=None
########      py2exe
    )