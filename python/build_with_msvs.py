#!/usr/bin/env python

# The simple procedure:
# 1. Enter the VC folder
# 2. Call the vcvarsall.bat file with different parameter according to bits
# 3. Enter the project folder
# 4. Call MSBuild /t:clean with the .sln file
# 5. Call MSBuild /t:rebuild /p:Configuration=/specified backend/ .sln file

path_to_msvs_amd64 = os.path.abspath(r"C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC")
path_to_msvs_x86 = os.path.abspath(r"C:\Program Files\Microsoft Visual Studio 10.0\VC")
path_to_icl_amd64 = os.path.abspath(r"C:\Program Files (x86)\Intel\Composer XE 2013\bin")
path_to_icl_x86 = os.path.abspath(r"C:\Program Files\Intel\Composer XE 2013\bin")

def build_target(platform, compiler, solution, target):
    command_list = []

    set_env_script = "vcvarsall.bat %s" % platform

    if platform == 'amd64' and compiler == 'msvs':
        path_to_build_folder = os.path.join(work_path, 'windows_amd64_msvs')
    elif platform == 'x86' and compiler == 'msvs':
        path_to_build_folder = os.path.join(work_path, 'windows_x86_msvs')
    elif platform == 'amd64' and compiler == 'icl':
        path_to_build_folder = os.path.join(work_path, 'windows_amd64_icl')
    elif platform == 'x86' and compiler == 'icl':
        path_to_build_folder = os.path.join(work_path, 'windows_x86_icl')

    if platform == 'amd64':
        path_to_msvs = path_to_msvs_amd64
        path_to_icl = path_to_icl_amd64
    elif platform == 'x86':
        path_to_msvs = path_to_msvs_x86
        path_to_icl = path_to_icl_x86

    project_name = solution + ".vcxproj"

    if compiler == 'msvs':
        command_list.append(r'cd %s' % path_to_msvs)
        command_list.append(r'call %s' % set_env_script)
        command_list.append(r'cd %s' % path_to_build_folder)
        command_list.append(r'call MSBuild /t:clean %s' % project_name)
        command_list.append(r'call MSBuild /t:rebuild /p:Configuration=%s %s' %(target, project_name))
    elif compiler == 'icl':
        command_list.append(r'cd %s' % path_to_msvs)
        command_list.append(r'call %s' % set_env_script)
        command_list.append(r'cd %s' % path_to_icl)
        if platform == 'amd64':
            command_list.append(r'call iclvars.bat intel64 vs2010')
        elif platform == 'x86':
            command_list.append(r'call iclvars.bat ia32 vs2010')
        command_list.append(r'cd %s' % path_to_build_folder)
        command_list.append(r'call MSBuild /t:clean %s' % project_name)
        command_list.append(r'call MSBuild /t:rebuild /p:Configuration=%s %s' % (target, project_name))

    # open a file to write build command
    build_script = 'build_target.bat'
    with open(build_script, 'w') as f:
        for command in command_list:
            f.write('%s%s' % (command, os.linesep))

    p_build = subprocess.Popen(build_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p_build.communicate()
    build_result = p_build.returncode

    return build_result

