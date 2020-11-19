''' Module log_decorator.py'''
# Author: Saj Patel
# Date: 3rd Aug 2020
# Purpose: 
import time, sys
from decimal import Decimal

def log(file_name = None):
    def log_wrap(func):
        def wrapper_class(*args):
            if not file_name is None and isinstance(file_name, str):
                try:
                    if file_name[-3:] == "txt":
                        orig_stdout = sys.stdout
                        f = open(str(file_name), 'a')
                        sys.stdout = f
                        
                        # printing a line of stars
                        print("*" * 30)
                            
                        # printing the function name
                        print("Calling function", func.__name__)        

                        # printing the type of arguments supplied to the functions
                        if len(args) == 0:
                            print("No arguments.")
                        else:
                            print("Arguments:")
                            for arg in args:
                                arguments = ""
                                arguments += "- " + str(arg)
                                arguments += " of type " + type(arg).__name__
                                arguments += "."
                                print(arguments)

                        # printing the output of the function and recording the time take to excute the function.
                        print("Output:")
                        start = time.time()
                        func_execution = func(*args)
                        end = time.time()
                        result = end - start
                        print("Execution time:", round(Decimal(result), 5), "s.")

                        # printing the return value of the function
                        if func_execution is None:
                            print("No return value.")
                        else:
                            return_value = "Return value: "
                            return_value += str(func_execution)
                            return_value += " of type "
                            return_value += type(func_execution).__name__
                            return_value += "."
                            print(return_value)

                        # printing final line of stars
                        print("*" * 30)
                        
                        sys.stdout = orig_stdout
                        f.close()
                    else:
                        raise IOError()
                    
                except IOError:
                    # printing a line of stars
                    print("*" * 30)
                        
                    # printing the function name
                    print("Calling function", func.__name__)        

                    # printing the type of arguments supplied to the functions
                    if len(args) == 0:
                        print("No arguments.")
                    else:
                        print("Arguments:")
                        for arg in args:
                            arguments = ""
                            arguments += "- " + str(arg)
                            arguments += " of type " + type(arg).__name__
                            arguments += "."
                            print(arguments)

                    # printing the output of the function and recording the time take to excute the function.
                    print("Output:")
                    start = time.time()
                    func_execution = func(*args)
                    end = time.time()
                    result = end - start
                    print("Execution time:", round(Decimal(result), 5), "s.")

                    # printing the return value of the function
                    if func_execution is None:
                        print("No return value.")
                    else:
                        return_value = "Return value: "
                        return_value += str(func_execution)
                        return_value += " of type "
                        return_value += type(func_execution).__name__
                        return_value += "."
                        print(return_value)

                    # printing final line of stars
                    print("*" * 30)
             
            else:
                # printing a line of stars
                print("*" * 30)
                    
                # printing the function name
                print("Calling function", func.__name__)        

                # printing the type of arguments supplied to the functions
                if len(args) == 0:
                    print("No arguments.")
                else:
                    print("Arguments:")
                    for arg in args:
                        arguments = ""
                        arguments += "- " + str(arg)
                        arguments += " of type " + type(arg).__name__
                        arguments += "."
                        print(arguments)

                # printing the output of the function and recording the time take to excute the function.
                print("Output:")
                start = time.time()
                func_execution = func(*args)
                end = time.time()
                result = end - start
                print("Execution time:", round(Decimal(result), 5), "s.")

                # printing the return value of the function
                if func_execution is None:
                    print("No return value.")
                else:
                    return_value = "Return value: "
                    return_value += str(func_execution)
                    return_value += " of type "
                    return_value += type(func_execution).__name__
                    return_value += "."
                    print(return_value)

                # printing final line of stars
                print("*" * 30)

        return wrapper_class
                          
    return log_wrap
