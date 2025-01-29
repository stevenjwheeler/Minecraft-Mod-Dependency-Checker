import os
import zipfile
import toml
import json
import prettytable as pt

def list_dependencies(mods_folder):
    mods_info = {}

    for file_name in os.listdir(mods_folder):
        if file_name.endswith('.jar'):
            jar_path = os.path.join(mods_folder, file_name)
            with zipfile.ZipFile(jar_path, 'r') as jar_file:
                for name in jar_file.namelist():
                    if name.endswith('mods.toml'):
                        with jar_file.open(name) as toml_file:
                            content = toml_file.read().decode('utf-8')
                            data = toml.loads(content)
                            if 'mods' in data and data['mods']:
                                mod_id = data['mods'][0].get('modId', 'unknown')
                                if mod_id != 'unknown':
                                    dependencies = data.get('dependencies', {}).get(mod_id, [])
                                    mods_info[mod_id] = [
                                        dep['modId'] for dep in dependencies 
                                        if dep['modId'] not in ('forge', 'minecraft') and dep.get('mandatory', False)
                                    ]
                    elif name.endswith('fabric.mod.json'):
                        with jar_file.open(name) as json_file:
                            data = json.load(json_file)
                            mod_id = data.get('id', 'unknown')
                            if mod_id != 'unknown':
                                dependencies = data.get('depends', {})
                                mods_info[mod_id] = [
                                    dep for dep in dependencies.keys() 
                                    if dep not in ('forge', 'minecraft')
                                ]

    table = pt.PrettyTable()
    table.field_names = ["MOD NAME", "DEPENDENCIES"]
    table.hrules = pt.HRuleStyle.ALL 

    for mod, deps in mods_info.items():
        if deps:
            dep_list = ', '.join(deps)
        else:
            dep_list = "No mandatory dependencies found."
        table.add_row([mod, dep_list])
    
    table.align = "l"

    print(table)

# Ask for the mod folder path
print("""Minecraft Mod Dependency Checker V1.0.0
By Steven Wheeler (https://github.com/stevenjwheeler/Minecraft-Mod-Dependency-Checker/)

This tool reads the manifests in your mod folders .jar files and extracts information about the mandatory dependencies that each mod requires. 
This helps to determine what libraries your mods in your installation or modpack require to function. 
(For example, I created this tool to figure out what libraries I no longer needed after removing some mods from my modpack.)
""")
mods_folder_path = input("Enter the path to the mod folder to check: ").strip()
list_dependencies(mods_folder_path)
