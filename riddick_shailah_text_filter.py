banned = ['Turkey','Dog','Fox','Cat','Chicken']
message = input('Input Message: ')
def text_filter(new_message):
    return ' '.join(new_message)

message_list = message.split()
new_message = [word for word in message_list if word not in banned]

print(text_filter(new_message))
