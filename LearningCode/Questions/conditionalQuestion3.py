p1 = "buy now"
p2 = "Click this"
p3 = "lot of money"
p4 = "earn money"

msg = input("Enter a Comment ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This comment is spam")
else : 
    print("This is not spam Comment")