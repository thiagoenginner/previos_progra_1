function with boolean values / numbers / strings
    int("Numero/booleano") converts a decimal number or a boolean value into an integer. tambien puede convertir un string con un entero en un numero entero.
    float("Numero/booleano") convierte un numero entero o un valor booleano en un numero decimal. tambien puede convertir un string con un decimal en un numero decimal.
    converts an integer or a boolean value into a decimal number.
    abs("Numero") returns the absolute value (positive version) of an integer or a decimal number.

funciones con iterables:
    tuple("iterable") converts an iterable into an immutable tuple. *
    sum("iterable") returns the sum of the elements in an iterable that contains only numbers.
    max("iterable") returns the largest number or the lexicographically greatest string from an iterable
    min("iterable") returns the smallest number or the lexicographically smallest string from an iterable.
    list("iterable") converts an iterable, including a range object, into a list.
    sorted("iterable", reverse = True) sorts an iterable in ascending order by default. If you add the reverse parameter,
    the function sorts it in descending order. In both cases, the original order of the iterable remains unchanged.
    it always returns a list as the result.
    
    enumerate("iterable") returns an sequence of index-value tuples (but is not a list),
    wich can be used in a loop like for index, elemento in enumerate(iterable).
    
    map("funcion", "iterable") applies a function to each element of an iterable. To see the result,
    you should convert it into a list first. it does not modify the orginal iterable.
    
    filter("funcion", "iterable") works similarly to map(), but instead of saving the results of applying the function,
    it uses the function´s output to determine which elements to keep. 
    
other functions:
    lambda "parameter/s": "expression" receives zero or more parameters,
    operates on them through a single expression, and returns a value.
    open("archivo", "modo", encoding= "utf-8")
    open a file to read, write or append() it through an encoding system, like UTF-8. 
    
instruccion:
    continue skips the remaining code in the current iteration and immediately starts the next iteration of the loop. 
    break exits the loop immediately. Useful for stopping loops early when a condition is met.
    import "modulo" allows you to use a module in your program, such as math. A module is a file that contains python code
    (functions, classes, or variables) that you can import and reuse in other programs.
    raise "excepcion" generates a exception and stops the execution of the program. manually triggers an exception, stopping the program
unless handled with try-except.
    assert "condicion", "mensaje" pone una condicion para seguir con el programa. Si no se cumple, genera un excepcion e imprime un mensaje (opcional).
    del "diccionario" remove a dictionary, key-value pairs or other objects (lists, variables, etc.).
    example removing a key-value:
        # my_dict = {"a": 1, "b": 2}
        # del my_dict["a"]  


errors/exceptions:
    ZeroDivisionError is triggered when dividing by zero.
    ValueError is triggered when a function receives an argument of the right type but with an invalid value.
    example: trying to convert a string into an integer:
    # x = int("hello")  # ❌ ValueError: invalid literal for int() with base 10: 'hello'
    # clarification: strings can contain either text or numbers, and int() is designed to work with strings only if
    #  they represents numbers.
    AssertionError is triggered when an assert statement valuates to false.
    exception catch any exception (that occurs inside the try block).
    OSError is triggered when an operating system-related error occurs, suchas file handling issues,
        permission error, or unvailable system resources.
    IndexError is triggered when you try to access an invalid index in a sequence (an iterable
        that supports numerical indexing and slicing such as a list, tuple, or string).
    FileNotFoundError is a very common operating system issue, which is why Python decided to create it, as it makes
        debugging easier. the file might not exist, or there could be an issue with
        the path (like incorrect or inaccessible paths).
    NameError is triggered when you try to use a variable or function that hasnt been defined or doesnt exist in the
        current scope. *scope refers to the region within a program where a particular variable or function is accessible or defined.
        For example, local scope refers to variables that  are defined inside a function, while global scope refers  to variables that
        are defined outside of any function or class.

modules:
    random allows to use the following functions:
        random.random() returns a random real number between 0 and 1, including 0 but not 1.
        random.randint("start value", "end value") returns a random integer within a specified range,
            including both the start and end values.
        random.choice("iterable") returns a random element from a non-empty iterable. *if  the iterable is empty, it will raise
        an execption:
            #IndexError: Cannot choose from an empty sequence
        random.shuffle("list") alters the orden of the elements in a list, modifying the original one.
        
clausula:
    else: controlo el flujo del programa. Se ejecuta solo si no se produjo ninguna excepcion (finally lo va a hacer siempre).
    is a statement used to define a block of code that will run if a specific condition is not met. *Its most commonly used with
    if, for/while and in try/except blocks.
    #with an if statement: the else block runs when the condition in the if statement is false.
    #with a for or while loop: the else block runs after the loop finishes, but only if the loop wasnt interrupted by a break
    #	statement.
    #with a try/except block: the else block runs only if no exception was raised in the try block.
    
especificadores de conversion:
    %"numero entero"d, %"variable" 
    %"numero decimal"f, %"variable" especifica un ancho a la hora de imprimir un numero decimal.
    ***Se pueden imprimir dos variables identificando cada una.***

other parameters:
    sep="separator" in Pythons print function specifies the separator between multiple arguments.
        For example:
        #print("Hello", "world", "!", sep="-")
        # Output: Hello-world-!
unpacker:
    *"iterable" unpacks elements from any iterable. its used in the following contexts:
        #printing without brackets or commas.
        #	numbers = [1, 2, 3]
        #	print(*numbers)  # Output: 1 2 3

        #passing multiple arguments to a function.
        #   def add(a, b, c):
        #   return a + b + c
        #   values = [1, 2, 3]
        #   print(add(*values))  # Output: 6

        #merging iterables into a new list.
        #   list1 = [1, 2, 3]
        #   list2 = [4, 5, 6]
        #   merged = [*list1, *list2]
        #   print(merged)  # Output: [1, 2, 3, 4, 5, 6]

        #capturing multiple values in a variable.
        #   def func(a, b, *rest):
        #   print(a, b, rest)
        #   func(1, 2, 3, 4, 5)  # Output: 1 2 (3, 4, 5)

    
operadores:
    in verifica la presencia de un elemento.
    not in verifica la no presencia de un elemento.

methods of lists:
    "list".insert("index","element") inserts an element at the specified index in a list.
        If the index is within the range, it will shift the other elements to the right.
        If the index is out of range (greater than length of the list), it will add the element at the end of the list.
    "list".pop("index") removes and returns an element at the specified index in a list.
        If no index is provided, it removes and returns the last element by default.
    
    "list".remove("element") removes the first ocurrence of the specified element.
        If the element is not found, it raises a ValueError.
    
    "list" o "string".index("element", "start index", "end index not included") searches for the first ocurrence of the element within a
        specified range, and returns the index of th element.
        If the element is not found, it raises a ValueError.
        You can define the start and end indices to specify the range in which to search.
    
    "list" o "string".count("element") returns the number of ocurrences of a specified element in a list.
    "list".clear() removes all elements from the list, leaving it empty.
    "list".reverse() reverses the orden of the elements in a list, modifying the original one.
        If the list is empty, it wont cause any error.
    "list".sort(reverse=True) sorts a list in ascending order by default.
        If you add the reverse parameter, the function sorts it in descending order, modifyng the original one.
    "copy"="original".copy() copies a list.*
    
    
--------------------------------------------------------------------------------------------------------------------------------    
    "sep".join("string/list") returns a single string, where the elements of the iterable are joined together using "sep" as
        a separator.
    
--------------------------------------------------------------------------------------------------------------------------------   

methods of string:
    
    "string".split("separator") splits a string into a list of substrings using "separator" as a delimiter.
        If no separator is provided, it splits by whitespaces.
        Consecutive spaces are trated as a single separator when no argument is given. The string is not modified.
    
    "string".replace("substring to remove", "substring to add", "maximum number of times")
        replaces an substring by another one, with the option of determine how many times. The original string remains unchanged
        because the strings are immutable in python.
    
    "string".isalpha() returns True if all characters in the string are alphabetic (letters only), otherwise returns False.
    "string".isdigit() returns True if all characters are digits (0-9), otherwise returns False.
    "string".isalnum() returns True if the strings contains digits and/or numbers, with no spaces or special characters, otherwise returns False.
    "string".isupper() returns True if all the alphabetic characters in the string are capitalized, otherwise returns False.
    "string".islower() returns True if all the aphabetics characters in the string are lowercase, otherwise returns False.
    
    "string".upper() converts all the alphabetic characters in the string to uppercase and returns a new string with those changes.
    "string".lower() converts all the alphabetic characters in the string to lowercase and returns a new string with those changes.
    "string".capitalize() converts the first alphabetic character in uppercase and all other alphabetic characters to lowercase.
        it returns a new string with those changes.
    "string".title() converts the first alphabetic charcater of each word to uppercase and all other alphabetic characters to lowercase.
        it returns a new string with those changes.
    
    "string".center("width","fillchar") centers the string in a broad and stuffed determined.
    "string".ljust("width", "fillchar") aligns the string to the left within a field of specified width,
        and fills the remaining space with the specified fillchar.
    "string".rjust("width", "fillchar") aligns the tring to the right within a field of specified width,
        and fills the raminin space with the specified fillchar.
    "string".zfill("width") aligns the string to the right within a field of specified width, but fills the remaining space with zeros.
    
    "string".strip("another string") removes each character from the argument in the orden they appear,
        but only from the beginning and the end of the string.
    "string".lstrip("another string") removes each character from the argument in the orden they appear,
        but only from the left side of the string.
    "string".rstrip("another string") removes each character from the argument in the orden they appear,
        but only from the right side of the string.
    
    "string".find("substring") returns the index of the first occurrence of the substring within the string.
        if the substring is not found, it returns -1.
    "string".rfind("substring") returns the index of the last occurrence of the substring withing the string.
        if the substring is not found, it returns -1.
        
methods of files:
    "file".close() is used to close the file after you are done with it. closing a file is important because it frees up system resources and
       ensures that any data written to the file is properly saved.
    "file".write("string") writes the specified string to the file, but it does not automatically add a newline after the string.
        If you want the string to be written on a new line, you need to explicitly include the newline character (\n) at the end of the string.
    "file".writelines("list") writes a list of strings to a file, where each string is written consecutively without adding new lines
        automatically. If you want each string to appear on a new line, you must ensure that each string in the list includes a newline character (\n).
    "file".read("number of bytes") reads a specified number of bytes from the file.
    "file".readline() reads a single line from the file, stopping at the newline character (\n).
    "file".seek("number of bytes") moves the file cursor to a specified byte within the file.
        The characters in a file encoded in ASCII take 1 byte each.
        These include English letters (A-Z, a-z), digits (0-9) and basic symbols.
        The characters in a file encoded in UTf-8 can take 1 to 4 bytes, depending on the character:
        - emojis typically use  4 bytes.
        - some special symbols may use 3 bytes.
        - accented letters often use 2 bytes. 

methods of sets:
    "set".add("element") adds an element to the set, but only if its not already present, since sets do not allow duplicate values.
    "set".pop() removes and returns an arbitrary element. this element is the most likely to be returned based on pythons internal storage,
        which determines the order.
    "set".remove("element") removes the specified element. 
        If the element does not exist in the set, it raises a KeyError.
    "set".clear() removes all elements from the set, leaving it empty.
        
methods of dictionaries:
    "dictionary".get("key","default value") returns the value associated with the specified key. You can provide a default value to avoid a KeyError,
        which is raised if the key does not exist or have a value.
    "dictionary".pop("key", "default value") removes the key-value pair and returns the value.
        You can provide a default value as a second argument to avoid a KeyError, which is raised if the key does not exist or have a value.
    "dictionary".keys() returns a sequence containing all the keys from the dictionary.
    "dictionary".values() returns a sequence containing all the values from the dictionary.
    "dictionary".items() returns a sequence contaning the key-value pairs from the dictionary as a tuples.
        dict.fromkeys("sequence", "value") creates a dictionary using a specified sequence (strings, lists, tuples, etc)
        as keys, and assigns a specified value to each key.
    
    
    


    
