from distutils.core import setup
import py2exe

setup(name="lasviewer",
      version="0.1",
      description="Aplicacion que visualiza una lista de ficheros LiDAR",
      author="Ivan del Viejo",
      author_email="ivandelviejo@gmail.com",
      url="https://github.com/ivanuco",
      license="GPL",
      scripts=['./src/viewer/lasviewer.py'],
      console=['./src/viewer/lasviewer.py'],
      options={"py2exe": {"bundle_files": 1,"includes":["./src/viewer/glviewer.py"]}},
      zipfile=None
    )