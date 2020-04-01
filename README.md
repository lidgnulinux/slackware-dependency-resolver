# Slackware Dependency Resolver

A simple script that tells you what packages a package depends on and more.


## Installation

Clone the repo, make main script executable and run it with desired parameters.

## Usage

#### Get all dependencies of a package recursivly

    $ ./sdr.py {pkg-name}

Example:

    $ ./sdr.py llvm
    {'gcc', 'mpfr', 'ncurses', 'zlib', 'gmp', 'libmpc', 'gcc-g++', 'libffi'}

It also lets you choose between different options available:

    $ ./sdr.py python
    Seems there are options to choose from for "python":
    [0] openssl-solibs
    [1] openssl

    Which one do you choose? 1
    
    {'icu4c', 'gmp', 'libffi', 'mpfr', 'gamin', 'gdbm', 'db48', 'gcc-g++', 'zlib',
    'gcc', 'ncurses', 'bzip2', 'expat',  'readline', 'sqlite', 'openssl', 'glib2', 'libmpc'}
