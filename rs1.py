


print("🤖 Robot Movement Simulator")

x = 0
y = 0
moves = 0
history = [(x, y)]

while True:
    print("\nCurrent position:", x, y)
    print("1. Right")
    print("2. Left")
    print("3. Up")
    print("4. Down")
    print("5. Stop")

    command = input("Choose a direction (1-5): ")

    if command == "1":
        if x < 4:
            x = x + 1
            moves = moves + 1
            history.append((x, y))
        else:
            print("Right boundary reached!")

    elif command == "2":
        if x > 0:
            x = x - 1
            moves = moves + 1
            history.append((x, y))
        else:
            print("Left boundary reached!")

    elif command == "3":
        if y < 4:
            y = y + 1
            moves = moves + 1
            history.append((x, y))
        else:
            print("Upper boundary reached!")

    elif command == "4":
        if y > 0:
            y = y - 1
            moves = moves + 1
            history.append((x, y))
        else:
            print("Lower boundary reached!")

    elif command == "5":
        print("Robot stopped!")
        break

    else:
        print("Invalid choice! Try again.")

print("Final position:", x, y)
print("Total moves:", moves)
print("Movement history:", history)
