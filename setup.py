from setuptools import setup

setup(
    name="fpdb",
    packages=["fpdb"],
    license="MIT",
    install_requires=[
        "pywin32; os_name=='nt'",
    ],
)
