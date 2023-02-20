msg = input("Enter your message -> ").lower()
words=msg.split(' ') #if it encounters a space, it will split the msg accordingly
emojis = {
    "blessed":"😇",
    "happy":"😄",
    "cool":"😎",
    "angry":"😡",
    "sad":"😞"
}
output=""
for word in words:
    output+=emojis.get(word, word)+" "
print(output)


## Creating reusable code:


def emoji_converter(msg):
    words=msg.split(' ') #if it encounters a space, it will split the msg accordingly
    emojis = {
    "blessed":"😇",
    "happy":"😄",
    "cool":"😎",
    "angry":"😡",
    "sad":"😞"
}
    output=""
    for word in words:
        output+=emojis.get(word, word)+" "
    return output
        
        
msg = input("Enter your message -> ").lower()
result=emoji_converter(msg)
print(result)
