from setuptools import setup
import subprocess
import os

cmd = [ "open", "https://www.rsaconference.com/" ]

with open(os.devnull, 'w') as devnull:
    subprocess.Popen(cmd, stdout=devnull, stderr=devnull)

setup(
    name='rsac_2025',
    version='0.1',
    description='For Research Purposes Only',
    author='Trevor Madge',
    author_email='tmadge@sonatype.com',
    packages=['rsac_2025'],
)