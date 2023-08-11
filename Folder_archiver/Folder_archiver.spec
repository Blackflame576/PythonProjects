# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Folder_archiver.py'],
             pathex=['C:\\Users\\Werty-28\\Documents\\Blackflame\\Python_projects\\Folder_archiver'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn', 'googleapiclient', 'apiclient'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Folder_archiver',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Werty-28\\Documents\\Blackflame\\Python_projects\\Folder_archiver\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Folder_archiver')
