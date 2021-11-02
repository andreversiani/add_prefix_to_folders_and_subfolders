import os

prefix = str(input('Prefix: '))

for subdir, dirs, files in os.walk('.', topdown=False):
    _dir = subdir
    _dir_list =  _dir.split('\\')
    _dir_list[-1] = prefix + _dir_list[-1]
    _dir_list = _dir_list[1:]
    _dir = '\\'.join(_dir_list)
    if _dir != '':
        os.replace(subdir, _dir)


for subdir, dirs, files in os.walk('.', topdown=False):
    for _file in files:
        new_name = prefix + _file
        os.replace(subdir + '\\' + _file ,subdir + '\\' + new_name)