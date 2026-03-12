
def binary_search(words, target):
    low = 0
    high = len(words) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if words[mid] == target:
            print (f'Target = {target}, Found at index = {mid}, Number of iterations = {iterations}')
            return mid

        elif words[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    print (f'Target = {target}, Found at index = -1, Number of iterations = {iterations}')
    return -1

def main():
    with open ("words.txt","r")as file:
        words = [line.strip() for line in file.readlines()]
        print('Number of words read:', len(words))

    while True:
        target = input ("Enter a word or exit to quit:").strip()
        if target.lower() == 'exit':
            print ("exiting program")
            break
        binary_search(words, target)
if __name__ == '__main__':
    main()

