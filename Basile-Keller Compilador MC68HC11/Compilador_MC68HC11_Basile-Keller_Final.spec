# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Compilador_MC68HC11_Basile-Keller_Final.py'],
             pathex=['C:\\Users\\andre\\Desktop\\Basile-Keller Compilador MC68HC11'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Compilador_MC68HC11_Basile-Keller_Final',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
