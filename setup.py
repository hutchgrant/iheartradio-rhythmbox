from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='iheartradio',
      version='1.0.4',
      description='iheartradio radio station fetcher for rhythmbox',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Grant Hutchinson(hutchgrant)',
      keyswords='iheartradio radio rhythmbox',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
        'Topic :: Multimedia :: Sound/Audio',
      ],
      license='MIT',
      url='https://github.com/hutchgrant/iheartradio-rhythmbox',
      packages=['iheartradio'],
      scripts=['bin/iheartradio'],
      install_requires=[
          'bs4', 
          'pyfiglet',
           'requests', 
           'lxml',
        ],
     )