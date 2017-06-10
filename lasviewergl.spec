# -*- mode: python -*-
import sys

block_cipher = None


a = Analysis(['src\\viewer\\lasviewer.py'],
             pathex=['C:\\LiClipse Workspace\\lidar'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
b = Analysis(['src\\viewer\\glviewer.py'],
             pathex=['C:\\LiClipse Workspace\\lidar'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
MERGE((b, 'glviewer',os.path.join('glviewer','glviewer.exe')), (a, 'lasviewer',os.path.join('lasviewer','lasviewer.exe')))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('build', 'pyi.'+sys.platform, 'lasviewer','lasviewer.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )

pyzB = PYZ(b.pure, b.zipped_data,
             cipher=block_cipher)
exe = EXE(pyzB,
          b.scripts,
          b.binaries,
          b.zipfiles,
          b.datas,
          name=os.path.join('build', 'pyi.'+sys.platform, 'glviewer','glviewer.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )