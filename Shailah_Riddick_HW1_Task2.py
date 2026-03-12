def main():
    back_stack = []
    forward_stack = []
    current_page = "http://www.google.com/"
    
    while True:
        command = input().strip()
        
        # QUIT
        if command == "QUIT":
            break
        
        # BACK
        elif command == "BACK":
            if not back_stack:
                print("Ignored")
            else:
                forward_stack.append(current_page)
                current_page = back_stack.pop()
                print(current_page)
        
        # FORWARD
        elif command == "FORWARD":
            if not forward_stack:
                print("Ignored")
            else:
                back_stack.append(current_page)
                current_page = forward_stack.pop()
                print(current_page)
        
        # VISIT
        elif command.startswith("VISIT"):
            parts = command.split()
            
            if len(parts) != 2:
                print("Ignored")
            else:
                url = parts[1]
                back_stack.append(current_page)
                current_page = url
                forward_stack.clear()
                print(current_page)
        
        # Invalid command
        else:
            print("Ignored")


#Driver 
if __name__ == "__main__":
    main()