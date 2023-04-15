started = False
while True:
    command=input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started..")

    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped...")

    elif command=="help":
        print("""start- to start car
stop-to stop car
quit-to quit app
        """)

