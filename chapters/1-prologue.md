# Notes from Learning Python by Mark Lutz

## Python features that makes it simple, powerful and readable
so much so that it's used from scripting to large scale development

### 1. Dynamic typing
When you type anything in python file, it becomes an object just like how anything that exists on the earth is an object. Python automatically knows their type. so there isn't any need for explicit writing about the type.
Below data work simply out of the box

  
```10
'this is a string'
10 + 10
'i am a superman' + 'and also a supervillian'```


Note: Duck typing enables to lookup for the + operator method on the object's tree hierarchy , 
and polymorphism(part of OOP) helps to execute the method when found. Hence the same operator 
+ behaves differently for a number and a string because both of these objects have them implemented for their specific needs.

### 2. Automatic memory management
- When I type anything in python file, it gets a space and an address for it when the python  runs the file after reading it first. Just like if i move to a city, i need a space to live and an address to that space.
- Recall how anything on python is an object. So each object that lives inside python file has a 'space' called memory which is allocated automatically when python runs the file.
- If any of these objects remain unused then python is smart enough to know it doesn't need to exists and removes their memory location automatically.
- However, it helps to know that after the python finishes reading the file then all the memories allocated during reading of the file gets released unless python was specifically told to cache some of the object address for any future use.
10 --> gets a memory address eg. <1000x677292020>
when unsued the memory space is reclaimed by a process called garbage collection.

**Execution Flow:**
Writing code --> python reads the file from top to bottom just like a human would read, making sure all the code doesn't have mistakes in the language.
Translate code --> python compiles the code into another format called bytecode. 
Bytecode --> this code is OS agonastic, which means it's universal such that it can be used on any OS that has python interpreter installed
Runtime --> The python interpreter, python virtual machine installed in the OS then each bytecode instructions: automatically identifies the object type, allocation memory for each objects, searching and find method location of objects in the class hierarchy tree.
Machine Code(PVM <-> CPU) --> Python virtual machine interprets each line of bytecode and calls on the precompiled machine code equivalent C function while passing the objects into the function.
Pre compile C Function: The C functions then dispatch the machine code to the CPU for execution. The function returns the pointer to the 
Output: Python virtual machine picks the data and formats it into human readable form using pythons internal tools. 
Note for Note: The output need not be complied into bytecode and then back to human readable form because unlike code in .py file which are instructions that need to complied, the output is merely pointer to the objects in the memory which the PVM is fully capable of format in human readable form.

### 3. Programming in the large support
Here are the tool set that python provides in order to support writing large and complex systems.
1. Modules, Classes, Exceptions... these tools help in organising and managing the code as components which eases maintenance, testing, readability pain which invaribly accompanies a large sysem code.
2. Essentially python supports both Procedural and Object Oriented. 
--> Procedural being a controlled flow of the program
--> Object Oriented focusing on resusability and customization.
--> Python also supports pure functional programming which can be used alongside Procedural and OOP to ehance and run large systems 

### 4. Built in objects
Python provides objects out of the box that helps in storing anything from simple to complex data. And the size of these objects can be shrunk and expanded on demand without worrying about the memory issue when right set of data structure objects are applied to support the cause
Recall:
- how in python every object is a space in the memory and all that names given to these objects are merely pointers to this memory location. for eg.  

```    name = 'joe'
    repeat_name = name```
    
Here both name and repeat_name point to the same memory address of the string object 'joe'.
- python keeps track of these reference pointers and as soon as the pointer's count hits 0, the memory allocated to the string object becomes available to be reclaimed. and python employs garbage collector to do the job
- interesting thing is that, when objects are allocated memory address during their execution or runtime the address are valid only as long as the execution is in progress. once the execution or runtime completes its run or execution all the memory allocations are freed.
- it means when the code is run again, fresh set of memory address are allocated to the objects 
- python removes the burden of managing memories from the user/developer and takes it on itself
- if one tries to access a pointer that doesn't point any memory address python simply raises error same way when an index in a list is accessed beyond its boundary

### 5. Built in tools
In order to support all the built in objects, python provides number of powerful and clever operations that helps in processing these objects in a succnit and efficient way

### 6. Library utilities
Python has large collection of precoded libraries that makes it effective to avoid reinventing the wheel but simply use them out of the box to solve standard problems in the system such as file read write, working with a presistent db, interacting with os and file systems. Much of these are utilized at the application level.
In an essence, using libraries encourages code reusability 

### 7. Third pary utilities
Python encourages developers to develop and share utilities that are not part of python's offical library. This has resulted in massive collection of third party libraries and framework that has directly impacted the productivity, and ease of development. Some of the popular tools are:
Web development: Django, Flask, FastAPI
Data analysis and science: NumPy, pandas, SciPy, Matplotlib, Seaborn
Machine learning and AI: TensorFlow, PyTorch, scikit-learn
Web scraping: BeautifulSoup, Scrapy
Testing: pytest, unittest (though unittest is part of the standard library)
Environment and packaging: virtualenv, pipenv, Poetry
APIs and HTTP: requests, httpx
Database ORM: SQLAlchemy, Tortoise ORM, peewee
Asynchronous programming: asyncio (core), aiohttp (third-party)
Automation: Selenium, PyAutoGUI
