book=["matilda","mashmallow_land","dog_days","The_boy_in_the_striped_pijamas","benji"]
copy_counts=["3","0","5","10","31"]

library={book: count for book,count in zip(book,copy_counts)}
print("this is the stock :",library)

available_books=[books for books in book if int(library[books])>0]
print(f"available_books:{available_books}\n")

choice=(input(f"what book out of:{available_books}do you want to borrow: "))


if choice not in library or library[choice]==0:
    print("book un available")
    exit()

library[choice]=int(library[choice])-1
late_fee=[1,4,5,3,7]
extra_fee=int(input(f"enter extra fee of "))

updated_fees=list(map(lambda fee: fee + extra_fee,late_fee))
print("updated late fees:",updated_fees)

book_index=book.index(choice)
chosen_fee=updated_fees[book_index]
print(f"late fee for {choice} after update:{library[choice]}")

print(choice,"borrowed! reamaining copies:",library[choice],"\n")

print("="*10,"library book checker","="*10)
print("library book borrowed:",choice)
print("extra_fee:",extra_fee)
print("updated_fee:",updated_fees)
print("late fee :",late_fee)
print("="*20)

