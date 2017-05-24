from distutils.core import setup
from os import path

DIRNAME = path.dirname(path.realpath(__file__))

name = lambda x : path.join(DIRNAME, x)

setup(name='usbkill',
      version='1.0-rc.4',
      description='killswitch is an anti-forensic kill-switch that waits for a change on your USB ports and then immediately shuts down your computer.',
      author='ashumallik',
      author_email='mallikashu@outlook.com',
      license='GPLv3',
      url='https://github.com/ashumallik/KILL-SWTICH.PY/blob/master/KillSwitch.py',
      
      packages=['killswitch'],
      scripts=[name('install/killswitch')],
      data_files=[ ('/etc/', [ name('install/install.ini') ]) ]
     )
