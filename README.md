# befunpy
**befunpy** is an dynamic-sized and extensible Befunge-93 interpreter written in Python.

**befunpy**'s origin is a [Befunge interpreter](https://gist.github.com/Camroku/98f795da992bc55d133687d1854e36b7) made in QoLang which was made by the author of this interpreter.

## Extensions
Copy the extension's file to `extensions` folder, and add `extsi.registerext("extensionname")` to `exts.py`.

Example:
```sh
# Assuming we're in /home/user/befunpy which is this repository
copy ../Downloads/mygreatextension.py ./extensions/mygreatextension.py
echo "extsi.registerext(\"mygreatextension\")" >> exts.py
```