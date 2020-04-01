#!/usr/bin/python3

import sys
import json

"""
Slackware Dependency Resolver (SDR)

Author: Milad As (Ravexina)
Github: https://github.com/ravexina/slackware-dependency-resolver

COMES WITH NO GUARANTEE
It depends on a list of dependencies provided by salixos.org

"""


class Dependencyr:

    def __init__(self):
        # Load the json data
        file = open('./slackware-packages.json')
        self.packages = json.load(file) #file.read()
        file.close()

        # Generate necessary data
        self.packages_data = {}
        for pkg in self.packages['packages']:
            try:
                self.packages_data[pkg['name']] = pkg['deps']
            except:
                self.packages_data[pkg['name']] = []

        self.queue = []
        self.checked = []

    def first_degree_depends(self, pkg_name):
        deps = self.packages_data[pkg_name]

        # Check for multiple optios like [openssl-solibs/openssl] as 
        # a single dependency
        dep_lst = []
        for dep in deps:
            if type(dep) is type([]):
                print('Seems there are options to choose from for "' + pkg_name + '":')
                for index, name in enumerate(dep):
                    print('[' + str(index) + ']', name)
                choice = int(input('\nWhich one do you choose? '))
                dep_lst.append(dep[choice])
            else:
                dep_lst.append(dep)

        return dep_lst

    def recursive_depends(self, *pkgs_names):
        for pkg in pkgs_names:
            self.queue.extend(self.first_degree_depends(pkg))
            self.checked.append(pkg)

        new_pkgs = set(self.queue) - set(self.checked)

        if len(new_pkgs) > 0:
            self.recursive_depends(*new_pkgs)

        return set(self.queue)


package_name = sys.argv[1]
dependency_resolver = Dependencyr()

dep_list = dependency_resolver.recursive_depends(package_name)
print(dep_list)
