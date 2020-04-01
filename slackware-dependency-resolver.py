#!/usr/bin/python3

import sys
import json

"""
Slackware Dependency Resolver (SDR)

Author: Milad As (Ravexina)
Github: https://github.com/ravexina/slackware-dependency-resolver

The script relies on a list of dependencies provided by salixos.org

===============================
=== COMES WITH NO GUARANTEE ===
===============================

"""


class DependencyResolver:

    def __init__(self):
        file = open('./slackware-packages.json')
        self.packages = json.load(file)
        file.close()

        # Reform data as a key [package] pair [deps] dictionary
        self.packages_data = {}
        for pkg in self.packages['packages']:
            try:
                self.packages_data[pkg['name']] = pkg['deps']
            except:
                self.packages_data[pkg['name']] = []

        self.queue = []    #  List of actual dependencies
        self.checked = []  #  To skip checking packages we already have checked


    def first_degree_depends(self, pkg_name):
        deps = self.packages_data[pkg_name]

        #  Check for multiple options which come as a list. like: [openssl-solibs, openssl]
        dep_lst = []
        for dep in deps:
            # Multiple options as a dependency is available
            if type(dep) is type([]):
                #  Skip asking for options that one already have been selected from
                #  to avoid re-prompting about same options over and over
                if not set(dep).isdisjoint(self.queue):
                    continue

                #  Show a list of available options to user to select from
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
            #  There are still packages that we did not check their chain of dependencies
            self.recursive_depends(*new_pkgs)

        return set(self.queue)


package_name = sys.argv[1]
dependency_resolver = DependencyResolver()
dep_list = dependency_resolver.recursive_depends(package_name)

print(dep_list)
