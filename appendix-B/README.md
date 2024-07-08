# Appendix B: Running Programs
note: use `-O` after `python3` to "optimize" by skipping `assert` checks

## Windows
* `.bat`
```bat
@py.exe C:\path\to\your\pythonScript.py %*
@pause
```
* `@` prevents it being displayed in terminal window
* `%*` forwards coommand line args to the python script
* `@pause` does the "press any key to continue..." thing
* If you store your `.bat` and `.py` files in `C:\Users\<username>` you can do win-R, enter the script name (without the `.bat` even) and press enter. Otherwise, for win-R, you need to do full path names.

## MacOS
* `.command` file extension
```command
#!/usr/bin/env bash
python3 /path/to/your/pythonScript.py
```
* `chmod u+x yourScript.command`
* can use spotlight search (cmd + space) to run it (if it's in your `/Users/matthewberthoud` folder

## Linux
* this part is about doing it with a gui basically... not very linux...

