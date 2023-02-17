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
