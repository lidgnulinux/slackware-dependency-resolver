# Slackware Dependency Resolver

A python script that tells you what packages a package from official slackware package set depends on.
It relies on a list of dependencies provided by salixos.org.

> [Packages.json](https://download.salixos.org/x86_64/slackware-15.0/PACKAGES.json)


## Installation

Clone the repo, make main script executable and run it with desired parameters.

## Usage

#### Get all dependencies of a package recursivly

    $ ./slackware-dependency-resolver.py {pkg-name}

Example:

    $ ./slackware-dependency-resolver.py llvm
    {'gcc', 'mpfr', 'ncurses', 'zlib', 'gmp', 'libmpc', 'gcc-g++', 'libffi'}

It also lets you choose between different options available:

    $ ./slackware-dependency-resolver.py python
    Seems there are options to choose from for "python":
    [0] openssl-solibs
    [1] openssl

    Which one do you choose? 1
    
    {'icu4c', 'gmp', 'libffi', 'mpfr', 'gamin', 'gdbm', 'db48', 'gcc-g++', 'zlib',
    'gcc', 'ncurses', 'bzip2', 'expat',  'readline', 'sqlite', 'openssl', 'glib2', 'libmpc'}
    
Alternative : 

```
$ deps-slack {pkg-name}

$ ~/.local/bin/deps-slack tar
Seems there are options to choose from for "tar":
[0] aaa_libraries
[1] acl

Which one do you choose? 1
Seems there are options to choose from for "tar":
[0] aaa_libraries
[1] attr

Which one do you choose? 1
attr aaa_libraries acl
 
