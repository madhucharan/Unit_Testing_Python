# Unit Testing in Python

First we need to know about what is unit testing, When and Why do we use them

<p>We often check our code whenever we write functions or classes by passing some variables just to make sure the code is working properly as we thought.Lets say we have changed our code after some point of time. Now we have to again test this function by passing some arguments and verify if its correct or not. 

It is okay if we have two to four functions of code but imagine we are working as a software engineer and we have to write lot of functions and test them before productionizing the code.

But we know that its a naive approach of testing our functions in this case and it will waste our time as it is inefficient. But there is a better way instead of this manual process and it is called **UNIT TESTING**.
</p>

### Unit Testing
Unit testing, a testing technique using which individual modules are tested to determine if there are any issues by the developer himself. It is concerned with functional correctness of the standalone modules.

The main aim is to isolate each unit of the system to identify, analyze and fix the defects.

The benifits of unit testing are:

<ul>
<li>Reduces Defects in the Newly developed features or reduces bugs when changing the existing functionality.</li>
<li>Reduces Cost of Testing as defects are captured in very early phase.</li>
<li>Improves design and allows better refactoring of code.</li>
<li>Unit Tests, when integrated with build gives the quality of the build as well.</li>
</ul>

### Life Cycle of unit testing
(Image source : Tutorials point)

<img src="https://www.tutorialspoint.com/software_testing_dictionary/images/unit_testing.jpg" alt="unit testing lifecycle" width="50%" height="60%">

<p>
There are several ways for unit testing.We can use 
1.Unittest library which is python standard library
2.Pytest library (it is also widely used even though it is not a standard library)

we are going to use pytest library here to test some of the functions to know how to use it.

Note:

1. Unit Testing not only saves our time but also gives us the grip of our code so that we can track it.

2. It also helps an unknown person just by looking at our testcases to better understand our code before looking at the functions.
</p>

### Installation:

<p> We are going to install it by running the following command on the command line</p>

    pip install pytest
<p>Note:

We are going to run the code on command line 

If you are using any IDE like pycharm and if you want to run the module/test code in the IDE itself you may want to install the pytest in the IDE itself

**For installation in pycharm :**
Go to File -> settings-> Project:Current project name -> Project interpreter -> Click + on top right -> search for pytest and install it  
</p>

Lets look at an example code and then we can go for some test cases for practical understanding.

<li>Let us think that the below code is saved as func.py module.</li>

    def sum(a,b):
        sum=a+b
        return sum

This is our code and we need to test it for verifying our implementation

Generally we pass two values and check its giving right value or not.But in a general scenario where it is hard to track every function whenever it is created and it is modified as it takes time.

<li>So we need to use pytest as an alternative.To use pytest we need to create a separate module and write our test cases there and we should name the testing module as test_name.py and this is a naming convention used so that python will recognize this module as a test module.</li>

<li>Import the code module (here func.py) into test_func (here in test_name - name can be anything and I have named it as "func" because I am going to test the func module. </li>

    import func.py
    ***
    The same naming convention applies to the functions in our testing module 
    and the test functions should also start with testname
    ***
    def test_sum():
        assert sum(10,5) == 15
        
Now save it and open command line and go to the path where these modules are saved and run the following command:

    pytest test_func.py

### Output

If our test case is correct we will get output as:

    test_func.py .
    
Here **.** refers to correct answer

If our test case fails we will get **F** instead of **.** 

The output for a fail case would be like :

    test_func.py F

And then it will show the error where our code went wrong.

Now lets work on pytest by creating some unit tests by ourselves so that we will get hands on experience.

Note: All the code will be placed  in the repository to check and run in your own system.

### Example 1
Lets say we have a function that takes birth year as an input and outputs the age of the person in years.Lets try this code

Name the module as agepred.py

    def age(year):
    return 2020-year

    def age_in_weeks(year):
    ##this function assumes that a year has exactly 52 weeks
    return (2020-year)*52

    
Now create an another module called test_agepred.py and import agepred into it.

Make sure they are in same directory otherwise it raises an error.

    from agepred import *
    
    def test_age():
    assert(age(2000)==20)

    def test_age_in_years():
    assert age_in_weeks(2010)==520

Now save and run the following command on the terminal:

    pytest test_agepred.py

The output will be as follows:

    ================================================= test session starts =================================================
    platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: C:\Users\charan\Desktop\Unit_Testing_Python\Example1
    collected 1 item

    test_agepred.py .                                                                                                [100%]

    ================================================== 1 passed in 0.02s ==================================================

Lets go to another example and we will try different features in pytest module too for each example

### Example 2

In this example we will be writing a function to find whether the entered year is a leap year or not 

Name the module as Leapy.py and create a function in it as isLeapYear()

    def isLeapYear(year):
    
    if (year % 4) == 0:  
       if (year % 100) == 0:  
           if (year % 400) == 0:  
               print("{0} is a leap year".format(year))  
           else:  
               print("{0} is not a leap year".format(year))  
       else:  
           print("{0} is a leap year".format(year))  
    else:  
       print("{0} is not a leap year".format(year))  

Now create a test function for this in a new module called test_leapy.py and the code will be as follows:

    import leapy
    #here we can import it in another way from above example or we can also use
    #from leapy import *
    
    def test_isLeapYear():
        assert(isLeapYear(2020) == "2020 is a leap year"
Now the output will be as follows:

    pytest test_leapy.py
Output:

    ================================================= test session starts =================================================
    platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: C:\Users\charan\Desktop\Unit_Testing_Python\Example2
    collected 1 item
    
    test_leapy.py .                                                                                                  [100%]
    
    ================================================== 1 passed in 0.12s ==================================================
    
### Example 3

Now we will implement another function and also test it with wrong statement or code error and look how the output will be

