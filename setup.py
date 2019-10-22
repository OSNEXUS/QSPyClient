import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='QSPyClientLib',  
     version='1.0',
     scripts=['qspyclient','qs_client.py'],
     author="Seth Cagampang",
     author_email="seth.cagampang@osnexus.com",
     description="QuantaStor REST API python library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/OSNEXUS/QSPyClient",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD 2-Clause 'Simplified' License",
         "Operating System :: OS Independent",
     ],
 )
