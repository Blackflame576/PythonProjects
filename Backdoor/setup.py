import os
import sys 
from cx_Freeze import setup, Executable
import json


DefaultIgnoreFiles = [".git","db.sqlite3",".sql",".log","env",".so"]
DefaultIgnoreFolders = ["__pycache__","env","venv"]
HomeDir = os.path.dirname(os.path.realpath(__file__))
ListDir = os.listdir(HomeDir)
IgnoreFilePath = os.path.join(HomeDir,"IgnoreFiles.json")
IgnoreFolderPath = os.path.join(HomeDir,"IgnoreFolders.json")
IncludeFiles = []
IconName = 'icon.ico'
ScriptName = input("Script name:")
Version = '1.0'
Description = ''
isWindow = False
NameProgramm = f'{ScriptName.replace(".py","")}'
CompanyName = input("Company name:")
if os.path.exists(IgnoreFilePath):
    pass
else:
    IgnoreFile = open(IgnoreFilePath,"w+")
    json.dump(DefaultIgnoreFiles,IgnoreFile,ensure_ascii=False,sort_keys=True, indent=2)
    IgnoreFile.close()
if os.path.exists(IgnoreFolderPath):
    pass
else:
    IgnoreFolder = open(IgnoreFolderPath,"w+")
    json.dump(DefaultIgnoreFolders,IgnoreFolder,ensure_ascii=False,sort_keys=True, indent=2)
    IgnoreFolder.close()
IgnoreFile = open(IgnoreFilePath,"r+")
ListIgnoreFiles = json.load(IgnoreFile)
IgnoreFile.close()
IgnoreFolder = open(IgnoreFolderPath,"r+")
ListIgnoreFolders = json.load(IgnoreFolder)
IgnoreFolder.close()
for object in ListDir:
    if os.path.isfile(object):
        extension = os.path.splitext(object)[1]
        for filename in ListIgnoreFiles:
            if object == filename or object == extension:
                pass
            else:
                IncludeFiles.append(object)
    elif os.path.isdir(object):
        for namedir in ListIgnoreFolders:
            if object == namedir:
                pass
            else:
                IncludeFiles.append(object)
target = Executable(
    script = ScriptName,
    # base = "Win32GUI",
    icon = IconName
)

bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (f"{CompanyName}", f"{NameProgramm}"),
    }

build_exe_options = {
    "include_files":IncludeFiles,
    # 'includes': ['atexit', 'tkinter'],
    }



setup(name=NameProgramm,
      version=Version,
      description=Description,
      executables=[target],
      options={
          'bdist_msi': bdist_msi_options,
          'build_exe': build_exe_options})
# os.path.splitext()[1]