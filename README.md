# Introduction to Python

1. Python is a general purpose high level programming language.
2. Python was developed by Guido Van Rossam in 1989 while working at National Research Institute at Netherlands.
3. But officially Python was made available to public in 1991. The official Date of Birth for Python is : Feb 20th 1991.
4. Python is recommended as first programming language for beginners.

## Examples

Q. To print Hello World

In Java:

    public class HelloWorld
    {
        p s v main(String[] args)
        {
            SOP("Hello World");
        }
    }

In C:

    #include<stdio.h>
    void main()
    {
        print("Hello World")
    }

In Python:

    print("Hello World")

Q. To print the sum of 2 numbers

In Java:

    public class Add
    {
        public static void main(String[] args)
        {
            int a,b;
            a=10;
            b=20;
            System.out.println("The Sum:"+(a+b));
        }
    }

In C:
    #include <stdio.h>
    void main()
    {
        int a,b;
        a=10;
        b=20;
        printf("The Sum:%d",(a+b));
    }


In Python:
    a=10
    b=20
    print("The Sum:",(a+b))


## Where we can use Python:

We can use everywhere. The most common important application areas are

1. For developing Desktop Applications
2. For developing web Applications
3. For developing database Applications
4. For Network Programming
5. For developing games
6. For Data Analysis Applications
7. For Machine Learning
8. For developing Artificial Intelligence Applications
9. For IOT.. etc.

## Features of Python:

1. Simple and easy to learn:

Python is a simple programming language. When we read Python program,we can feel like
reading english statements.

The syntaxes are very simple and only 30+ kerywords are available.

When compared with other languages, we can write programs with very less number of lines. Hence more readability and simplicity.

We can reduce development and cost of the project.


2. Freeware and Open Source:

We can use Python Worldware without any licence and it is freeware.

Its source code is open,so that we can we can customize based on our requirement.

Eg: Jython is customized version of Python to work with Java Applications.

3. High Level Programming language:

Python is high level programming language and hence it is programmer friendly language.

Being a programmer we are not required to concentrate low level activities like memory
management and security etc..


4. Platform Independent:

Once we write a Python program,it can run on any platform without rewriting once again.

Internally PVM is responsible to convert into machine understandable form.


5. Portability:

Python programs are portable. ie we can migrate from one platform to another platform
very easily. Python programs will provide same results on any paltform.


6. Dynamically Typed:

In Python we are not required to declare type for variables. Whenever we are assigning
the value, based on value, type will be allocated automatically.Hence Python is considered
as dynamically typed language.

But Java, C etc are Statically Typed Languages b'z we have to provide type at the beginning
only.

This dynamic typing nature will provide more flexibility to the programmer.


7. Both Procedure Oriented and Object Oriented:

Python language supports both Procedure oriented (like C, pascal etc) and object oriented
(like C++,Java) features. Hence we can get benefits of both like security and reusability etc.


8. Interpreted:

We are not required to compile Python programs explcitly. Internally Python interpreter
will take care that compilation.

If compilation fails interpreter raised syntax errors. Once compilation success then PVM
(Python Virtual Machine) is responsible to execute.


9. Extensible:

We can use other language programs in Python. The main advantages of this approach are:

1. We can use already existing legacy non-Python code
2. We can improve performance of the application


10. Embedded:

We can use Python programs in any other language programs.
i.e we can embedd Python programs anywhere.


11. Extensive Library:

Python has a rich inbuilt library.
Being a programmer we can use this library directly and we are not responsible to implement the functionality.


## Limitations of Python:

1. Performance wise not up to the mark b'z it is interpreted language.
2. Not using for mobile Applications

## Flavors of Python:

1.CPython:

It is the standard flavor of Python. It can be used to work with C lanugage Applications

2. Jython or JPython:

It is for Java Applications. It can run on JVM

3. IronPython:

It is for C#.Net platform

4.PyPy:

The main advantage of PyPy is performance will be improved because JIT compiler is
available inside PVM.

5.RubyPython

For Ruby Platforms

6. AnacondaPython

It is specially designed for handling large volume of data processing.

## Python Versions:

Python 1.0V introduced in Jan 1994.
Python 2.0V introduced in October 2000.
Python 3.0V introduced in December 2008.

Note: Python 3 won't provide backward compatibility to Python2.
i.e there is no guarantee that Python2 programs will run in Python3.

## Identifier

A name in Python program is called identifier. It can be class name or function name or module name or variable name.

a = 10

Rules to define identifiers in Python:

1. The only allowed characters in Python are

    a. alphabet symbols(either lower case or upper case).

    b. digits(0 to 9).

    c. underscore symbol(_).

2. By mistake if we are using any other symbol like $ then we will get syntax error.

    a. cash = 10 √

    b. ca$h = 20 

2. Identifier should not starts with digit.

    a. 123total

    b. total123 √

3. Identifiers are case sensitive. Of course Python language is case sensitive language.

    a. total=10
    b. TOTAL=999
    c. print(total) #10
    d. print(TOTAL) #999

4. We cannot use reserved words as identifiers

    Eg: def=10

6. There is no length limit for Python identifiers. But not recommended to use too lengthy
identifiers.


Q. Which of the following are valid Python identifiers?

1) 123total 
2) total123 √
3) java2share √
4) ca$h 
5) _abc_abc_ √
6) def 
7) if 


Note:

1. If identifier starts with _ symbol then it indicates that it is private

2. If identifier starts with __(two under score symbols) indicating that strongly private identifier.

3.If the identifier starts and ends with two underscore symbols then the identifier is language defined special name,which is also known as magic methods.

    Eg: __add__

## Reserve Words

In Python some words are reserved to represent some meaning or functionality. Such type of words are called Reserved words.
There are 33 reserved words available in Python.


Note:

1. All Reserved words in Python contain only alphabet symbols.

2. Except the following 3 reserved words, all contain only lower case alphabet symbols.

True

False

None


Eg:

    a= true 

    a=True √

To List Reserved Word 

    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



## Data Tyoes in Python

Data Type represent the type of data present inside a variable.
In Python we are not required to specify the type explicitly. Based on value provided,the
type will be assigned automatically.Hence Python is Dynamically Typed Language.

Python contains the following inbuilt data types


1. int

We can use int data type to represent whole numbers (integral values)

Eg:

    a=10
    type(a) #int


2. float

We can use float data type to represent floating point values (decimal values).

Eg: 

    f=1.234
    type(f) float

We can also represent floating point values by using exponential form (scientific notation).

Eg: 

    f=1.2e3
    print(f) 1200.0

instead of 'e' we can use 'E'

The main advantage of exponential form is we can represent big values in less memory.


3.complex

A complex number is of the form 

assets\images\Complex Data Types.PNG

a and b contain intergers or floating point values. 

Eg:

    3+5j
    10+5.5j
    0.5+0.1j

In the real part if we use int value then we can specify that either by decimal,octal,binary or hexa decimal form. But imaginary part should be specified only by using decimal form.

Note: Complex data type has some inbuilt attributes to retrieve the real part and imaginary part.

    c=10.5+3.6j
    c.real==>10.5
    c.imag==>3.6


4.bool

We can use this data type to represent boolean values. The only allowed values for this data type are:

True and False

Internally Python represents True as 1 and False as 0

    b=True
    type(b) =>bool
Eg:

    a=10
    b=20
    c=a<b
    print(c)==>True

True+True==>2
True-False==>1


5.str

str represents String data type.

A String is a sequence of characters enclosed within single quotes or double quotes.

    s1='Hello'
    s1="Hello"

By using single quotes or double quotes we cannot represent multi line string literals.

    s1="Hello
    World"

For this requirement we should go for triple single quotes(''') or triple double quotes(""")

    s1='''Hello
    World'''
    s1="""Hello
    World"""

We can also use triple quotes to use single quote or double quote in our String.

    ''' This is " character'''
    ' This i " Character '

We can embed one string in another string

    '''This "Python class very helpful" for java students'''

Slicing of Strings:

slice means a piece

[ ] operator is called slice operator,which can be used to retrieve parts of String

In Python Strings follows zero based index. 

1. The index can be either +ve or -ve.
2. +ve index means forward direction from Left to Right.
3. -ve index means backward direction from Right to Left.

Note:

1. In Python the following data types are considered as Fundamental Data types

    int

    float

    complex

    bool

    str



6. bytes

bytes data type represens a group of byte numbers just like an array.


7.bytearray

bytearray is exactly same as bytes data type except that its elements can be modified.

8.range

range Data Type represents a sequence of numbers.
The elements present in range Data type are not modifiable. i.e range Data type is
immutable.

9.list

If we want to represent a group of values as a single entity where insertion order required to preserve and duplicates are allowed then we should go for list data type.

1. insertion order is preserved
2. heterogeneous objects are allowed
3. duplicates are allowed
4. Growable in nature
5. values should be enclosed within square brackets.


10.tuple

tuple data type is exactly same as list data type except that it is immutable.i.e we cannot change values.

Tuple elements can be represented within parenthesis.

11.set

If we want to represent a group of values without duplicates where order is not important then we should go for set Data Type.

1. insertion order is not preserved
2. duplicates are not allowed
3. heterogeneous objects are allowed
4. index concept is not applicable
5. It is mutable collection
6. Growable in nature

12.frozenset

It is exactly same as set except that it is immutable. Hence we cannot use add or remove functions.

13.dict

If we want to represent a group of values as key-value pairs then we should go for dict data type.

Eg:

    d={101:'durga',102:'ravi',103:'shiva'}

14.None

None means Nothing or No value associated. If the value is not available,then to handle such type of cases None introduced. 

It is something like null value in Java.

Eg:

    def m1():
        a=10
        print(m1())

Note: Python contains several inbuilt functions

1. type()
   to check the type of variable
2. id()
   to get address of object
3. print()
   to print the values

In Python everything is object


## Escape Character

In String literals we can use esacpe characters to associate a special meaning. The following are various important escape characters in Python.

1) \n   New Line
2) \t   Horizontal tab
3) \r   Carriage Return
4) \b   Back space
5) \f   Form Feed
6) \v   Vertical tab
7) \'   Single quote
8) \"   Double quote
9) \\   back slash symbol


## Constants

Constants concept is not applicable in Python. But it is convention to use only uppercase characters if we don’t want to change value.

    MAX_VALUE=10

It is just convention but we can change the value.



