def shutdown(command):
   if command == "Yes":
    print("system shuttting down")
   elif command == "No":
     print("system shutting down")
   else:
        print("sorry")

command = input("Enter a command,yes or no:")
shutdown(command)