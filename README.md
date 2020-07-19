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

### Example 1:
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

### Example 2:

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
        assert isLeapYear(2020) == "2020 is a leap year"
Now the output will be as follows:

    pytest test_leapy.py
Output:

    ================================================= test session starts =================================================
    platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: C:\Users\charan\Desktop\Unit_Testing_Python\Example2
    collected 1 item
    
    test_leapy.py .                                                                                                  [100%]
    
    ================================================== 1 passed in 0.12s ==================================================
    
### Example 3:

Now we will implement another function and also test it with wrong statement or code error and look how the output will be

<li>Let us think that we need to write a program that checks whether the given input Email address is valid or not</li>
The rules of a vaild Email address will be :
<ol>
<li>All the letters should be in lowercase</li>
<li>Should end with @domain.com /@domain.in </li>
<li>should have only one @</li>
etc..
</ol>
We are going to import regular expression toolkit as it has many inbuilt functions for these kind of tasks

The code will be as follows:

    import re 
  
    # Make a regular expression 
    # for validating an Email 
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
          
    # Define a function for 
    # for validating an Email 
    def check(email):  
        # pass the regular expression 
        # and the string in search() method 
        if(re.search(regex,email)):  
            return "Valid Email"  
          

Now check for some cases by giving inputs as some wrong as well as correct cases.

### Important note:
We are writing these test cases to validate our function in all type of cases like we should also check them whether the function is working correctly in edge cases or not so it is better to think and write all the test and edge cases before writing the function so that we will be having an idea of what could go wrong.This will give an idea of writing a better function.

Now create another test module and import the above module into it.Now the code will look like-

**Note:
We are going to match strings here in another method using re module**  

    import re

    from mailcheck import *
    
    def test_check():
        #we use re module functions for matching strings in first assert statement
        
        value = check("contact@email.com")
        assert re.match("Valid Email",value)
        
        #this should fail as it is not a vaild email
        assert check("madhucharan") == "Valid Email"
        
It gives an assertion error as it fails the case as we gave an invalid email.
It also gives us a detailed explanation about the wrong case

    ================================================= test session starts =================================================
    platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: C:\Users\charan\Desktop\Unit_Testing_Python\Example3
    collected 1 item
    
    test_mailcheck.py F                                                                                              [100%]
    
    ====================================================== FAILURES =======================================================
    _____________________________________________________ test_check ______________________________________________________
    
        def test_check():
            #we use re module functions for matching strings in first assert statement
            value = check("contact@gmail.com")
            assert re.match("Valid Email",value)
            #this should fail as it is not a vaild email
    >       assert check("madhucharan") == "Valid Email"
    E       AssertionError: assert None == 'Valid Email'
    E        +  where None = check('madhucharan')
    
    test_mailcheck.py:10: AssertionError
    ================================================== warnings summary ===================================================
    mailcheck.py:5
      C:\Users\charan\Desktop\Unit_Testing_Python\Example3\mailcheck.py:5: DeprecationWarning: invalid escape sequence \.
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    -- Docs: https://docs.pytest.org/en/latest/warnings.html
    =============================================== short test summary info ===============================================
    FAILED test_mailcheck.py::test_check - AssertionError: assert None == 'Valid Email'
    ============================================ 1 failed, 1 warning in 0.45s =============================================
    
Note:
we can improve the above code by extending the if statement to classify wrong emails as well.The code will be like this-

        if (re.search(regex, email)):
            return "Valid Email"

        else:
            return "Invalid Email"
            
### Example 4:
We will write a function on handling exceptions with pytest
 
We will discuss a simple example of division by zero and see how to handle exception

    import pytest

    def div(value):
            return value / 0
    
        
 The test code will be as follows 
 
    from divide import *
    import pytest
    def test_div():
        with pytest.raises(ZeroDivisionError):
            div(2)

The output will be passed and it will be as follows:

    test_divide.py::test_div PASSED                                          [100%]
    
    ============================== 1 passed in 0.02s ==============================
    
    Process finished with exit code 0   
    
    
**Note:** If there is no exception raised now it will raise the exception and the output will be-

    test_divide.py::test_div FAILED                                          [100%]
    test_divide.py:2 (test_div)
    def test_div():
            # with pytest.raises(ZeroDivisionError):
    >           div(2)
    
    test_divide.py:5: 
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    value = 2
    
        def div(value):
    >           return value / 0
    E           ZeroDivisionError: division by zero
    
    divide.py:4: ZeroDivisionError



### Example 5:

Here we will implement a different approach and also we will try to run the code in a different manner.Lets check this

let us assume that we are writing a function that takes 2D numpy array as input and it will divide the array into two parts by dividing the no.of rows.

So we need to input the array as 2D and if the array dimention is not 2D it is going to raise an exception.

This example can help us in data science or ml process where we always divide training and testing data sets.

The function will be as follows:

    
    def split(data):
        no_rows = data.shape[0]
        firsthalf =no_rows-0.5*no_rows
        return firsthalf
        
Now lets look at the first test function by passing a 2D array

    from splitdata import *
    import numpy as np
    def test_split():
        data= np.array([[2,1],[3,4],[5,6],[9,8]])
        #we know that first half should be 2 rows and lets check it
        assert split(data)==2,"they are not equal and there is a mistake"

**Note: You can observe here that we can attach a string after the assert statement and it will print the string if the test goes wrong**


### Example 7:

We will mostly use pytest in deep learning also.

Lets take a case that the function will take some shape arguments as inputs and intialises input arrays to feed into input layers in a deep neural network.

We have no time to check them everytime my checking their shape if its correct or not.So we will initialize a test function for that

Before writing the function lets get some intuition on the arrays/vectors shapes in DNN

Let,

The weight matrix shape will be of (current layer size,previous layer size)
the bias matrix shape will be of (current layer size,1)

Lets initialize a function for it 

    import numpy as np

    def initializing(n_p,n_i,n_o):
    
        #let ni= current layer size
        #let npp=previous layer size
        #let no=size of output layer which is fed into next layer
        W1 = np.random.randn(n_i, n_p) * 0.01
        b1 = np.zeros((n_i, 1))
        W2 = np.random.randn(n_o, n_i) * 0.01
        b2 = np.zeros((n_o, 1))
        return W1,W2,b1,b2
        
The test function should check the data of the input everytime so that it will make our work easy

    import numpy as np
    from initialization import *
    def test_shape():
        W1,W2,b1,b2= initializing(5,3,2)
        assert (W1.shape == (3,5))
        assert (b1.shape == (3, 1))
        assert (W2.shape == (2, 3))
        assert (b2.shape == (2, 1))
        
As the shapes were correct the output will be 

    test_initialization.py::test_shape PASSED                                [100%]

    ============================== 1 passed in 0.01s ==============================
    
    Process finished with exit code 0
    
 This pytest will help a lot in deep neural network as mistakes happens frequently in the shapes of the vectors and other calculations too like calculating gradient/activation functions etc.
 
 #Example 7:
 
 We will write a function that takes a sentence as an input and outputs a list of words in that sentence
 
 the function is as follows:
 
    def formlist(statement):
    list= statement.split()
    return list
the test function will be :

    
    from make_list import *
    def test_formlist():
        statement = "This is pytest"
        assert formlist(statement)==['This','is','pytest']
 
      
The output is right as they were equal


We can furthur continue the above test lets say we input a sentence it should remove the repeated words and give output so we can check with the following test

    def test_unique():
    statement = "This is pytest example.Check This"
    assert list(set(formlist(statement))).sort()==['This ' ,'is','pytest','example.Check'].sort()
    
**Note** : Here I have just written the following in assert statement but these statements will be in a function but not like the above.The assert statement just checks the return value and the expected output.


###Example 8:

Some times we need to initialize the variables in everytest case as in the above examples.To overcome that there are some methods that will initialize at the beginning of the tests

They are :

1.SetUp()
2.TearDown()

Setup is for initialization and Teardown will revoke the variables initialized at the end

The initializations example will be as follows:

    def Setup(self):
        statement = "This is pytest"
     
    def TearDown(self):
         pass

NOTE:



<ul>
<li>To have a detailed explanation of the test output we can run pytest name.py -V
 </li>
 
 <li>We can also run "pytest" and python automatically checks for the test modules and runs them if they were present in the path directory </li>

</ul>

