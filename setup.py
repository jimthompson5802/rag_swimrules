from setuptools import setup, find_packages

setup(
    name='rag_swimrules',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A retrieval augmented generation testbed for testing a notebook based chatbot.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'transformers',
        'torch',  # Add any other dependencies required for your project
        'numpy',  # Example additional dependency
        'pandas'  # Example additional dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)