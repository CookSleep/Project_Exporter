# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(SPEC))
# 定义输出目录为当前目录
output_dir = os.path.join(current_dir, 'build')

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('HarmonyOS_Sans_SC_Regular.ttf', '.'), ('README.md', '.'), ('LICENSE', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='项目文件导出工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='icon-3种尺寸.ico',
          distpath=output_dir)  # 指定输出目录