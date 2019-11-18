import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
     name='ml-magic',  
     version='0.1',
     scripts=['ml-magic'] ,
     author="Bob van der Helm",
     author_email="bvanderh@gmail.com",
     description="A ML supportive library for analysis",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/bwvdhelm/ml-magic",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved",
         "Operating System :: OS Independent",
     ],
)