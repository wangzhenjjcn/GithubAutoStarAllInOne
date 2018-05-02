@echo off
set filepath=%~dp0
echo GitHubStar running
 xcopy "%filepath%settings.py" "%filepath%GitHubStar"  /C   /Y 
cd %filepath%
cd GitHubStar
start run.bat
cd ..
echo GitAutoFork running
xcopy "%filepath%settings.py" "%filepath%GitAutoFork" /C  /Y 
cd %filepath%
cd GitAutoFork
start run.bat
cd ..
echo GitHubFollow running
xcopy "%filepath%settings.py" "%filepath%GitHubFollow" /C  /Y 
cd %filepath%
cd GitHubFollow
start run.bat
cd ..
