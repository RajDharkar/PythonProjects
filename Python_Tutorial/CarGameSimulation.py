#why it printing this bruh

started = False
while True:
    command = input(">").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "start":
        if not started:
            print("Car started...Ready to go!")
            started = not started
        else:
            print("whatchu trynna do bruh")
    elif command == "stop":
        if started:
            print("Car stopped")
            started = not started
        else:
            print("whatchu trynna do bruh")
    elif command == "quit":
        break
    else:
        print("I'm sorry, I don't understand that")

