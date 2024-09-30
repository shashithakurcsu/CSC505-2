#  This program will will print out the names and number of pages in your prototype and the sequence or flow of the pages.
#  Define a dictionary to store the pages and their sequence
pages = {
    1: "Home Screen",
    2: "Create New List Screen",
    3: "List Detail Screen",
    4: "Item Add/Edit Screen",
}

# Print the number of pages in the prototype
print(f"Total pages in the prototype: {len(pages)}\n")

# Print the sequence of pages in the prototype
print("Sequence of pages in the prototype:")
for page_num, page_name in pages.items():
    print(f"Page {page_num}: {page_name}")

# Print the user flow explanation
print("\nFlow of the pages:")
print("1. Home Screen lists all shopping lists and provides options to create a new list.")
print("2. From the Home Screen, user can navigate to the Create New List Screen.")
print("3. After creating or selecting a list, the List Detail Screen shows the items.")
print("4. User can add or edit items on the Item Add/Edit Screen.")
