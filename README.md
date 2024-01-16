# nop_slide
Python script that generates assembly code for a "nop slide" function based on the provided parameters. This project was made for my System Programming for Engineers class.

GLOBAL VARIABLES:
  count: Initialized to 10, this variable determines the number of "nop" instructions in the generated assembly code.
  function: Initialized to "nop_slide," this variable is used as the function name in the assembly code.
FUNCTION MAIN:
  Checks if command-line arguments are provided (sys.argv[1]). If provided, it sets count to the absolute value of the integer representation of the argument.
  Opens a file named "{function}.S" in write mode to write the generated assembly code.
  Writes assembly directives to define the function (function) as a global function.
  Writes the function prologue, including saving the base pointer and setting up the stack frame.
  Inserts a "nop slide" using randomly selected "nop" or "fnop" instructions repeated count times.
  Measures the time stamp counter (TSC) at the beginning and end of the "nop slide" using the rdtscp instruction.
  Computes the difference in TSC values and writes the result to the eax register.
  Writes the function epilogue, restoring the base pointer and returning from the function.
  Closes the file.
CONDITIONAL CHECK FOR TOP-LEVEL EXECUTION: If the script is executed as the main program, it calls the main function.

This script generates assembly code for a "nop slide" function. The function contains a specified number of "nop" instructions, and it measures the time stamp counter (TSC) before and after the "nop slide" to calculate the execution time. The generated assembly code is written to a file with the name "{function}.S," where {function} is replaced by the value of the function variable. The number of "nop" instructions is determined by the count variable, which can be provided as a command-line argument.
