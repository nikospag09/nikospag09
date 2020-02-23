def synartisi(x):
    print([ord(c) for c in x])  # Gia metatropi oloklirou string
    for value in [ord(c) for c in x]:
        if value > 1:  # tipwnei an o xaraktiras sto ascii code einai prwtos arithmos
            for i in range(2, value // 2):
                if (value % i) == 0:
                    print(value, "is not a prime number")
                    break
            else:
                print(value, "is a prime number")

        else:
            print(value, "is not a prime number")

synartisi(input("Enter a String:"))

