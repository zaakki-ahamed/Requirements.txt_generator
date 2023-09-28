import ast
import importlib_metadata
import os
import re
import sys

# Directory containing your Python scripts
#Currently walks the current folder
scripts_directory = "./"

# Toggle output options
display_only_main_package = True  # Set to True to only display main package names
show_default_packages = False  # Set to True to display all packages, including default ones

# Function to recursively collect imported modules/packages
def collect_imports(file_path, collected_imports):
    with open(file_path, "r") as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        collected_imports.append(name.name)
                elif isinstance(node, ast.ImportFrom):
                    for name in node.names:
                        if node.level > 0:
                            # Handle relative imports by appending the module name
                            module_name = node.module
                            for _ in range(node.level - 1):
                                module_name = module_name.split('.')[0]
                            collected_imports.append(f"{module_name}.{name.name}")
                        else:
                            collected_imports.append(f"{node.module}.{name.name}")
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

# Function to get package version using importlib_metadata
def get_package_version(package_name):
    try:
        return importlib_metadata.version(package_name)
    except importlib_metadata.PackageNotFoundError:
        return None

# Blank ;ist to collect imported packages
imported_packages = []

# Collect imported packages from all Python scripts in the directory
for root, _, files in os.walk(scripts_directory):
    for file in files:
        if file.endswith(".py") and file != os.path.basename(__file__):
            script_path = os.path.join(root, file)
            collect_imports(script_path, imported_packages)

# Remove duplicates and sort
imported_packages = sorted(set(imported_packages))

main_packages = set()

if display_only_main_package:
    # Use regular expressions to extract main package names
    for package in imported_packages:
        match = re.match(r"^(\w+)", package)
        if match:
            main_packages.add(match.group(1))
else:
    main_packages = imported_packages

with open("Requirements.txt", "w") as requirements_file:
    #Print python version
    python_version = sys.version.split()[0]
    py = f"python == {python_version}\n"
    requirements_file.write(py)
    print(py)

    #Loop to go through package list
    for package in main_packages:
        #Condition to check if default packages should be excluded or not
        if show_default_packages==False and (package in sys.builtin_module_names or package in sys.modules):
            continue  # Skip iteration if package name is found in the native list
        version = get_package_version(package)
        #If version number is available
        if version:
            package_version = f"{package} == {version}\n"
            requirements_file.write(package_version)
            print(package_version)
        # If version number is not available
        else:
            package_name = f"{package}\n"
            requirements_file.write(package_name)
            print(package_name)

print("Requirements have been written to requirements.txt")