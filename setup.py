import setuptools

with open("README.md", "r") as fh:
    long_description_txt = fh.read()

setuptools.setup(
    name='quantastor-pkg',  
    version='1.0.2',
    scripts=['quantastor/qs_client.py'],
    author="Seth Cagampang",
    author_email="seth.cagampang@osnexus.com",
    description="QuantaStor REST python library",
    long_description=long_description_txt,
    long_description_content_type="text/markdown",
    url="https://github.com/OSNEXUS/QSPyClient",
    packages=setuptools.find_packages(),
    install_requires=['urllib3',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],

 )
