import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='quantastor-pkg',  
     version='0.0.1',
     scripts=['quantastor/qs_client.py'],
     author="Seth Cagampang",
     author_email="seth.cagampang@osnexus.com",
     description="QuantaStor REST API python library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/OSNEXUS/QSPyClient",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
 )
