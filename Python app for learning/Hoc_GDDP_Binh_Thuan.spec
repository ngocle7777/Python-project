# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Hoc_GDDP_Binh_Thuan.py'],
    pathex=[],
    binaries=[],
    datas=[('vebt.mp3', '.'), ('negative.mp3', '.'), ('Fredji - Happy Life (Vlog No Copyright Music).mp3', '.'), ('Fredji - Flying High (Vlog No Copyright Music).mp3', '.'), ('correct-.mp3', '.'), ('button-click.mp3', '.'), ('bienxanh.mp3', '.'), ('lop10_button_image.png', '.'), ('amnhac_bg.jpg', '.'), ('back_menu_button.png', '.'), ('background.jpg', '.'), ('Background_van.jpg', '.'), ('backgroundintro.jpg', '.'), ('diali_bg.jpg', '.'), ('LOGO.ico', '.'), ('logo.png', '.'), ('main background.jpg', '.'), ('music_button_image.jpg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Hoc_GDDP_Binh_Thuan',
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
)
