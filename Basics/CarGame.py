command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car is already started")
        else:
            started=True
            print("Car started!")
    elif command=="stop":
        if not started:
            print("Car is in the stop position, enter start to run it")
        else:
                started=False
                print("Car stopped.")
    elif command=="quit":
        print("Exited Game!")
        break;
    elif command=="help":
        print("""
    start -> start the Car
    stop -> stop the Car
    help -> for instructions
    quit -> exit the game
        """)
    else:
        print("Invalid Command")
