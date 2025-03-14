from setuptools import setup

setup(
    name='nrpc-cli',
    version='1.0.1',
    packages=[
        'nrpc_cli'
    ],
    install_requires=[
        'pyzmq',
    ],
    author='Aare Pikaro',
    author_email='aare.pikaro@example.com',
    description='Native RPC communication library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/aarepikaro/nrpc-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'term = nrpc_cli.term:start',
            'termex = nrpc_cli.term:start_ex',
            'show = nrpc_cli.show:start',
            'killall = nrpc_cli.kill:start',
        ],
    }
)
