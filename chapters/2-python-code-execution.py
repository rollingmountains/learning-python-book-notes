"""Python interpreter

Where does the code actually run or get executed and by whom?
--> All programming languages has to be translated or transformed or compiled into the language that the CPU that runs on the machine understands. 
--> The only language CPU understands is called Machine Code which interestingly always happend to have different combination of only two digits 0 and 1 representing the instruction to run the code. Kind of off(0) and on(1). But it gets stored as hex

    Eg: 10 equivalent of machine code is 00001010
    
--> All programming languages have their own mechanism to translate their human readable code to machine code. The mechanism is called interpreter.
--> Ultimately interpreter facilitates execution of the code by serving the human code as machine code to CPU

Python's mechanism

# 1. Most common python interpreter is CPython which runs on computers, smartphone...

High level flow

code.py file --> bytecode.pyc file --> machine code

-> code.py: lives in the cpu's disk. code written by developers based on python language
-> python interpreter: this is installed as python program in our machine. this also lives in the disk and is known as python virtual machine. installation bundles the tools required to format .py to .pyc using a compiler, python virtual machine to interpret the bytecode in the 
.pyc file and ship it to C function(a pre compile machine code function)
-> CPU: loads the objects from memory referenced by C function and executes the machine code and returns output memory reference back to PVM or python virtual machine

Complete Execution Flow:
Write code --> python compiler reads the file from top to bottom just like a human would read, making sure the code follows python's guideline. if the code errs compiler notifies the developer to fix it
Compile code --> python compiles the error free code into another format called bytecode. 
Bytecode --> this code is OS agonastic, which means it's universal such that it can be used on any OS that has OS compatible python interpreter installed
Runtime --> python virtual machine interprets each bytecode instructions: automatically identifies the object type, allocates memory for each objects, searches and finds method object location in the class hierarchy tree.
Machine Code(PVM <-> CPU) --> python virtual machine calls on the precompiled machine code equivalent C function while passing the objects memory location pointers into the function.
Pre compile C Function --> The C functions then dispatch the machine code to the CPU for execution. The CPU executes the machine code and sends back the output memory location poiners
Output --> Python virtual machine picks the object location pointers and formats it into human readable form using pythons internal tools. 
Note: The output need not be complied into bytecode and then back to human readable form because unlike code in .py file which are instructions that need to complied, the output is merely pointer to the objects in the memory which the PVM is fully capable to format in human readable form.

Where does all this compilation, interpretation and execution of machine code happen?
- In the RAM, random access memory of the OS. RAM is the playground for all the execution. python virtual machine, C function and the CPU access the RAM to pass and communicate the memory location of the object with each other.

Why have an intermediary layer and not simply translate human code to machine code upfront?
- This is a deliberate decision to remove the burden from developer to code the python statements that include explicit memory management, and declaration. This layer enbales the developer to do this

    print(10)
    
- During the runtime python interpreter, as the name says, interprets the bytecode that was compilec by the compiler and assigns type int to the object 10 and also makes note of the memory location of the object.
- Python also enables, developers to assing value or override method objects which actually get resolved during the runtime which gives absolute flexibility but this felxibility comes with a price. The price is slower execution speed than other compile ahead on time or compile just in time interpreters or engines used by pre historic languages like C and JAVA.
- The actual machine code execution speed is actually as close as C it's the runtime interpretation that slows the speed. However, for most common needs including large scale systems CPython is still good enough.
- This is all to say that developers or hobbiest can write the code and run it with no additional cost. Only only has to save the file in .py extension and execute with a command python code.py 

Note: Standalone executables
--> There are always people who tend to be a bit adventurous and for them there is an option to ship the python file as executables. These executables can be run as an application.
--> Example for macos executable
- Install a library called pyinstaller. Excellent example of using third pary library
- Create a python file with .py eg code.py
- run this from a command line tool from the directory same as the code.py is saved 
    pyinstaller --onefile --windowed hello.py
- this generates a executable inside a dist folder at the same location where code.py file exists
- inside the folder exists a executable with name same as the file name but doesn't have any exetension 
- click on the executables to see it run
- so the pyinstaller bundles the code file, and python interpreter in a pacakage and ships it. recall python needs an interpreter run the human code. and pyinstaller serves all as a bundle in one single pacakge
    
# 2. Other interpreters
Python community is always experimenting and as a part of that there are other interpreters for specific needs. Some of the noted below, this is a verbatim text from the book:
--> Jython and IronPython process Python programs for use in Java and .NET environments, respectively; they are alternative compilers for Python.
--> PyPy and Shed Skin are reimplementations of Python targeted at speed. PyPy speeds normal Python programs by using runtime type information and a JIT compiler to replace some Python bytecode with machine code as the program runs. Shed Skin speeds programs with an AOT compiler that translates a restricted subset of Python to C++, from which it can be fully compiled to machine code to be run as a program or used in others. Cython is a Python/C combination that can be compiled into machine-code extensions accessible to CPython code.”


    """
