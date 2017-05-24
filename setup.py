from distutils.core import setup
from os import path

DIRNAME = path.dirname(path.realpath(__file__))

name = lambda x : path.join(DIRNAME, x)

setup(name='usbkill',
      version='1.0-rc.4',
      description='usbkill is an anti-forensic kill-switch that waits for a change on your USB ports and then immediately shuts down your computer.',
      author='Hephaestos',
      author_email='hephaestos@riseup.net',
      license='GPLv3',
      url='https://github.com/hephaest0s/usbkill',
      
      packages=['usbkill'],
      scripts=[name('install/usbkill')],
      data_files=[ ('/etc/', [ name('install/usbkill.ini') ]) ]
     )
