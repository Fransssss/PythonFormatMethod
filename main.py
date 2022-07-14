# format method

original_poem = "The rose is red, the violet is blue the honey is sweet, and so are you"
blank_poem = "The rose is {}, the violet is {}, the honey is {}, and so are you"

# Sir Edmund Spense
print("\n== A Poem by Sir Edmund Spense ==")
print("1. Original Poem")
print("2. Re-write Poem")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\nThe original poem:\n [ {} ]". format(original_poem))
    elif choice == '2':
        change_red = input("Name a color: ")
        change_blue = input("Name a color: ")
        change_taste = input("Name a taste: ")
        rewrite_poem = blank_poem.format(change_red,change_blue,change_taste)
        print("\nThe rewrite poem:\n [ {} ]".format(rewrite_poem))
    else:
        print("\n[Invalid input]")

    print("\n== A Poem by Sir Edmund Spense ==")
    print("1. Original Poem")
    print("2. Re-write Poem")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")

