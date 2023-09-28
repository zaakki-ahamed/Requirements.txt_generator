# Requirements.txt_generator
If you've written a Python script and want to share it on GitHub, it's essential to include a "Requirements.txt" file. This file lists all the packages and their version numbers required to run your script. This tool is designed to simplify that process for you.


## How to Use

Follow these simple steps to generate a "Requirements.txt" file for your project:

1. **Copy the Script**: Copy the provided script into the folder containing your Python script(s) for which you need to extract the requirements.

2. **Run the Program**: Execute the script. It will recursively search through all subfolders to identify the packages used in your Python scripts.

3. **Access Your "Requirements.txt"**: After running the script, you'll find a "Requirements.txt" file generated in the same directory. This file will contain the package names and their associated version numbers.

Now, you can easily share your Python project on GitHub, ensuring that others can easily set up the required environment.

Feel free to customize the generated "Requirements.txt" file as needed.


## Important Notes

* The script currently goes through the folder and subfolders it's located it in. It's for the sake of simplicity. If you prefer to set the path manually, change the following line -

`scripts_directory = "./"`

* Only the base packages names (Eg: selenium, flask, etc.) will be in the output by default. If you want to include the subpackages (Eg: selenium.webdriver, flask.cli, etc.), change the following line to False-

`display_only_main_package = True`

* By default, all packages including libraries included with Python will be part of the output. If you want to exclude the default packages, change the following line to False-

`show_default_packages = True`