from setuptools import setup, find_packages

setup(
    name='gspreadeasy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'google-auth==2.26.2',
        'google-auth-oauthlib==1.2.0', 
        'gspread==5.12.4'
        'pandas==2.1.4', 
      ],
    # Additional metadata about your package.
    author='Antoine Eripret',
    author_email='antoine.eripret.dev@gmail.com',
    description='A simple wrapper for Gspread',
    url='https://github.com/antoineeripret/gsc_wrapper',
)