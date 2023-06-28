from setuptools import setup, find_packages

install_requires = [
    'requests>=2.22.0',
    'hetnetpy',
    'tqdm',
    'pandas',
    'matplotlib_venn',
    'matplotlib>=3.1.1',
    'seaborn',
    'scikit-learn>=0.21.3',
    'scipy>=1.3.1',
    'wikidataintegrator==0.7.4'
]

setup(
    name='data_tools',
    author='Mike Mayers',
    author_email='mmayers@scripps.edu',
    url='https://github.com/mmayers12/data_tools',
    version='0.0.8',
    packages=find_packages(),
    license='LICENSE',
    description='Tools for manipulating data, particularly with the end goal of forming hetnet',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    python_requires='>=3.6',
)
