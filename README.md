# Minecraft Mod Dependency Checker

## Version: 1.0.0

### Description
This tool reads the manifests in your mod folders .jar files and extracts information about the mandatory dependencies that each mod requires.
This helps to determine what libraries your mods in your installation or modpack require to function.
(For example, I created this tool to figure out what libraries I no longer needed after removing some mods from my modpack.)

### Prerequisites
- Python 3.x
- Required Python modules: `toml`, `prettytable`

### Installation
1. Download and install Python from [python.org](https://www.python.org/).
2. Install the required Python modules:
   ```sh
   pip install toml prettytable```

### Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where list_dependencies.py is located.
3. Run the script:
	```sh
	python run.py```
4. When prompted, enter the path to your mod folder.

### Output
The script will display a table with the mods and their mandatory dependencies.

### License
This project is licensed under the MIT License.