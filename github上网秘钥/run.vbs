Dim Shell,Python,PyFile
Set Shell = CreateObject("Shell.Application")
Python="D:\ProgramData\Anaconda3\envs\tensorflow-gpu\python.exe"
PyFile="E:\PythonCode\github������Կ\����.py"
Shell.ShellExecute Python,PyFile,"","runas"