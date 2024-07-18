# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('HarmonyOS_Sans_SC_Regular.ttf', '.'), ('icon-3种尺寸.ico', '.'), ('README.md', '.'), ('LICENSE', '.')],
    hiddenimports=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='项目文件导出工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon-3种尺寸.ico'
)

# 仅在 macOS 上添加 BUNDLE
import sys
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='项目文件导出工具.app',
        icon='icon-3种尺寸.icns',
        bundle_identifier=None,
    )
