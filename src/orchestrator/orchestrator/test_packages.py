# Copyright 2024 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

def run_package_inspect():
    import pkgutil

    def list_subpackages(package_name):
        package = __import__(package_name)
        path = getattr(package, '__path__', [])
        subpackages = [name for _, name, _ in pkgutil.iter_modules(path)]
        return subpackages

    # Replace 'your_package_name' with the actual name of the package you want to inspect
    package_name = 'orchestrator'
    subpackages = list_subpackages(package_name)

    print(f"Subpackages of {package_name}:")
    for subpackage in subpackages:
        print(subpackage)


if __name__ == "__main__":
    #agent_spot_arm.play()
    run_package_inspect()
