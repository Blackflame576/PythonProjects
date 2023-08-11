import os
import sys
from cx_Freeze import setup, Executable
import random

ListNumbers = ['1','2','3','4','5','6','7','8','9']
ListAlphabet = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
IconName = 'icon.ico'
ScriptName = 'HotSettings.py'
Version = '1.0'
Description = 'This my application'
isWindow = False
NameProgramm = f'{ScriptName.replace(".py","")}'
SecretActivationCode = ''
files = ['icon.ico']
def GenerateSecretActivationCode():
    global SecretActivationCode
    for i in range(1,5):
        a = random.choice(ListNumbers)
        b = random.choice(ListAlphabet)
        SecretActivationCode = SecretActivationCode.join(a + b)
    SecretActivationCode = SecretActivationCode + '-'
    print(SecretActivationCode)
    # for i in range(1,5):
    #     a = random.choice(ListNumbers)
    #     b = random.choice(ListAlphabet)
    #     SecretActivationCode = SecretActivationCode.join(a + b)
    # SecretActivationCode = SecretActivationCode + '-'
    print(SecretActivationCode)
    for i in range(1,5):
        a = random.choice(ListNumbers)
        b = random.choice(ListAlphabet)
        SecretActivationCode = SecretActivationCode.join(a + b)
    SecretActivationCode = SecretActivationCode + '-'
    for i in range(1,13):
        a = random.choice(ListNumbers)
        b = random.choice(ListAlphabet)
        SecretActivationCode = SecretActivationCode.join(a + b)
    print(SecretActivationCode)
GenerateSecretActivationCode()
target = Executable(
    script = ScriptName,
    base = "Win32GUI",
    icon = IconName
)

bdist_msi_options = {
    'upgrade_code': '{}-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % ("company_name", "product_name"),
    }

build_exe_options = {
    "include_files":files,
    # 'includes': ['atexit', 'tkinter'],
    }



setup(name=NameProgramm,
      version=Version,
      description=Description,
      executables=[target],
      options={
          'bdist_msi': bdist_msi_options,
          'build_exe': build_exe_options})