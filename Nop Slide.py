import sys
import random

count = 10
function = "nop_slide"

def main():
    global count

    if (len(sys.argv) > 1):
        count = abs(int(sys.argv[1]))

    # File.
    f = open(f"{function}.S", 'w')

    # Directives.
    f.write("  .text\n\n")
    f.write(f"  .global {function}\n")
    f.write(f"  .type   {function}, @function\n")
    f.write(f"{function}:\n")

    # Function prologue.
    f.write("  pushq %rbp\n")
    f.write("  movq %rsp, %rbp\n")

    # Read TSC - start.
    f.write("  rdtscp\n")
    f.write("  movl %eax, %ebx\n")

    # 'nop' slide.
    string = ("nop", "fnop")
    for _ in range(count):
    	f.write(random.choice(string))
    	f.write("\n")
        # f.write("  nop\n")

    # Read TSC - end.
    f.write("  rdtscp\n")
    f.write("  subl %ebx, %eax\n")

    # Function epilogue.
    f.write("  popq %rbp\n")
    f.write("  retq\n")

    f.close()

if __name__ == "__main__":
	main()
