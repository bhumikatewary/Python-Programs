amt = input("Enter cash amount in digits between 1-5: ")
digit_map = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}
output=""
for ch in amt:
    output+=digit_map.get(ch,"!")+" "
print(output)
