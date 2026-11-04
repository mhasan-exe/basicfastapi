val1 = bool(int(input("Enter 0 or 1: ")))
val2 = bool(int(input("Enter 0 or 1: ")))
gate = input("Enter the logic gate (AND, OR, NOT): ").strip().upper()
if gate == "AND":
    result = val1 and val2
    print(f"Result of {val1} AND {val2} is {result}.")
elif gate == "OR":
    result = val1 or val2
    print(f"Result of {val1} OR {val2} is {result}.")
elif gate == "NOT":
    result = not val1
    print(f"Result of NOT {val1} is {result}.")