# Extensions
Extensions are the way to add features to BefunPY. This page will teach you these:
* Creating an extension
* Distributing your extension
* Installing an extension

## Creating an extension
To create a very simple extension, all you need is a Python file in `extensions/` directory with a `register` function accepting 2 arguments in it: (`myextension.py` in our example)
```py
# My great extension

def register(regfunc, reglist):
    pass
```
This extension does nothing, and isn't even enabled. To enable the extension, add this line in `exts.py`:
```py
extsi.registerext("myextension")
```
Now our extension is enabled, but still does nothing because we didn't tell it to. Let's add a function to print "Hello, world!":
```py
# My great extension

def myext_hw():
    print("Hello, world!")

def register(regfunc, reglist):
    pass
```
Cool, but this won't work because this function need to handle 3 arguments and return them in case it modified them:
```py
# My great extension

def myext_hw(settings, program, stack):
    print("Hello, world!")
    return (settings, program, stack)

def register(regfunc, reglist):
    pass
```
Now the last thing to do is to register this function. Let's say we want this function to be called when the interpreter finds a `h` character:
```py
# My great extension

def myext_hw(settings, program, stack):
    print("Hello, world!")
    return (settings, program, stack)

def register(regfunc, reglist):
    regfunc('h', myext_hw)
```
Perfect! Now we can test it:
```
"A test extension:"52*;>:v
                       ^,_h@
```
Output:
```
A test extension:
Hello, world!
```
Congratulations! You have a working extension now!

### Well, what's `reglist` for?
It's for when you want to handle more than one characters with the same function. The function has to handle another argument, the character. This is an example usage:
```py
def bp_int(settings, program, stack, character):
    util.push(stack, int(character))
    return (settings, program, stack)


def register(regfunc, reglist):
    reglist(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], bp_int)
```

## Distributing your extension
We don't have something like a package manager yet (and we probably won't in near future), but you can follow these steps:
1. Create a repository for your extension
2. Create the `LICENSE` file and put your license in it (Github can do this for you while creating the repository)
3. Upload your extension
4. Create the `README.md` (or `README` if you don't like Markdown) file and put your extension's description and installation steps in it (Github can do this for you too)
5. Open an issue, telling you have created an extension and want it to be featured in the README.md file of BefunPY repository.
6. When you get approved, your extension will be listed in README.md!

## Installing an extension
So, you want to install an extension that doesn't have installation steps in its README file? Follow these steps:
1. Download the `.py` file
2. Put it in `extensions` folder
3. Add this line, changing `extension` to the `.py` file's name without the `.py` part:
```py
extsi.registerext("extension")
```
