from app.operations import Operations as ops

def calculator():
    print("Welcome to the Calculator REPL. Type 'exit' to quit")

    while True:
        u_in = input("Enter an operation: add, subtract, multiply, or divide, and two numbers. Or type 'exit' to quit: ")

        if u_in.lower() == "exit":
            print("Exiting calculator.")
            break

        try:
            op, n1, n2 = u_in.split()

            n1, n2 = float(n1), float(n2)
        except ValueError:
            print("Invlalid input. Follow the format: <operation> <first number> <second number>")
            continue

        if op == "add" or op == "addition":
            r = ops.add(n1, n2)     
        elif op == "sub" or op == "subtract" or op == "subtraction":
            r = ops.sub(n1, n2) 
        elif op == "multiply" or op == "multiplication":
            r = ops.mult(n1, n2) 
        elif op == "divide" or op == "division":
            try:
                r = ops.div(n1, n2)
            except ValueError as e:
                print(e)
                continue
        else:
            print(f"Unknown operation '{op}', try a valid operation")
            continue

        print(f"Result: {r}")