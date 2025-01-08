import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_USERNAME = "hadihassanbaloch"
AUTHOR_NAME = "Hadi Hassan"
SRC_REPO = "kdClassifier" 
AUTHOR_EMAIL = "12hadihasan@gmail.com"

setuptools.setup(
    
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    long_description= long_description,
    description= "Small Python Package for CNN app",
    long_description_content_type="text/markdown",
    url = f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}',  
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src"),
)