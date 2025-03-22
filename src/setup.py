import os
import re
import sys
import zipimport
sys.modules['zipimport'] = zipimport


from distutils.core import setup
# Add the site-packages directory where py2exe is located
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'bin', 'python', 'Lib', 'site-packages'))

# Import py2exe
import py2exe

# Modify paths relative to the location of setup.py
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the path to the directory containing setup.py
datafiles = []
dirs = ['', 'resources', 'resources/audio']
for directory in dirs:
    dirname = os.path.join(base_dir, directory)  # Ensure correct path usage
    for files in os.listdir(dirname):
        if (directory == ''):
            matchObj = re.search(r'map\d.txt', files, re.M|re.I)
            f1 = os.path.join(dirname, files)
            if matchObj:
                f2 = directory, [f1]
                datafiles.append(f2)
        else:
            f1 = os.path.join(dirname, files)
            if os.path.isfile(f1):
                f2 = directory, [f1]
                datafiles.append(f2)

setup(
    windows=[{
        'script': 'game.py',
        'dest_base': 'snakes-etc-on-a-plain',
        'icon_resources': [(0, 'resources/icons/icon.ico')]
    }],
    name='snakes-etc-on-a-plain',
    data_files=datafiles,
    options={
        'py2exe': {
            'dist_dir': '../release/win32',
            'dll_excludes': ['w9xpopen.exe'],
            'bundle_files': 0,
            'optimize': 2,
            'includes': ['zipimport']  # Explicitly include zipimport
        }
    },
    zipfile=None  # Ensure that py2exe doesn't create a separate zip file

)
