# -*- mode: python -*-

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
MERGE((b, 'glviewer','glviewer.exe'), (a, 'lasviewer','lasviewer.exe'))
pyzB = PYZ(b.pure, b.zipped_data,
             cipher=block_cipher)
exeB = EXE(pyzB,
          b.scripts,
          b.binaries,
          b.zipfiles,
          b.datas,
          name='glviewer',
          debug=False,
          strip=False,
          upx=True,
          console=True )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='lasviewer',
          debug=False,
          strip=False,
          upx=True,
          console=True )
