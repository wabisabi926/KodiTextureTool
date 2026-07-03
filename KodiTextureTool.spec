import sys
import os

sys.setrecursionlimit(5000)

block_cipher = None

a = Analysis(
    ['Kodi TextureTool.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('locales', 'locales'),
        ('utils', 'utils'),
        ('runtimes', 'runtimes'),
        ('help.md', '.'),
        ('changelog.txt', '.'),
        ('version.json', '.'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtPrintSupport',
        'PySide6.QtNetwork',
        'qtawesome',
        'reportlab',
        'reportlab.pdfgen',
        'reportlab.platypus',
        'reportlab.lib.pagesizes',
        'reportlab.lib.styles',
        'reportlab.lib.colors',
        'reportlab.lib.units',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KodiTextureTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/fav.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='KodiTextureTool',
)
