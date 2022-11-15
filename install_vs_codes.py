
# import OS module
import os
 
# Get the list of all files and directories
#path = "U://Computing//Programs//VS Code Extensions"
path = 'U:\\Computing\Programs\\VS Code Extensions\\'
dir_list = os.listdir(path)
cmd = "code "
print("Files and directories in '", path, "' :")

for f in dir_list:
    opt_string =  ' --install-extension "'+path+f+'" '
    print(opt_string)
    cmd += opt_string


print( cmd)
with open('command.txt', 'w') as f:
    f.write(cmd)
