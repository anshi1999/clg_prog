def Basics():
    name = "CHAPTER 1 : VARIABLES & DATA TYPES"
    what = "Variable is a name to a memory location in a program. It simply contains any value.Also known as identifiers."
    rule = """Variable have set of rule to write which is given below.
1) Identifiers can be the combination of uppercase and lowercase letters,digits or an underscore(_).
So myVariable, variable_1, variable_for_print are some example.
2) An identifier can not start with digit. So while variable_1 is valid but 1variable is not valid.
3) We can't use special symbols like !,#,@,&,%,$ etc. Also we can't use special key words assign to python for specific purpose.
4) It can be of any length.
TO BECOME A GOOD PROGRAMMER YOUR VARIABLE NAME SHOULD BE SIMPLE SHORT AND MEANINGFUL."""
    data_types = """PRIMARY DATATYPES OF PYTHON IS : "
              1) Integer = +ve, -ve, 0
              2) String = "anything into quotes will behave as str."
              3) Float = digits with decimals
              4) Boolean = True or False(any conditional statement whose answer will be in true or false with CAPITAL T and F
              5) None = No value is given.
    Python is Implicit typed language."""
    key_words = """KEYWORDS= these are reserved words in python and they are case sensitive(lowercase and uppercase)
    Can't be used as Indentifiers. These are as follows.
     
and,  else,  in,  return,  as,  except,  in,  True,  assert,  finally,  lambda,  try,  break,
False,  nonlocal,  with,  class,  for,  None,  while,  continue,  from,  not,  yield,  def,  global
or,  del,  if,  pass,  elif,  import,  raise."""
    comments = """ SINGLE LINE = USE #.....
                MULTI LINE = USE ''' .....'''"""
    type_casting = """It is a way to convert one datatype to another."""
    user_def_input =""" It can be taken simply as :  a= input()
    we can also do type casting as per our requirements as b = int(input())
    for float as c = float(input())"""
    print(name,"\n",what,"\n",rule,"\n",data_types, "\n",type_casting "\n", key_words,"\n",comments,"\n", user_def_input )
Basics()












