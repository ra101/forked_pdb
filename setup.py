from setuptools import setup

setup(
    name='fpdb',
    version='1.0',
    packages=['fpdb',],
    license='MIT',
    install_requires=[
        "pywin32; os_name=='nt'",
    ],
)