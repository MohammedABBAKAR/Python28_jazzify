# Instant JAZZ
# Create a function which concatenates the number 7 to the end of every chord in a list.
# Ignore all chords which already end with 7.

# Examples
# jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

# jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

# jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

# jazzify([]) ➞ []
# Notes
# Return an empty list if the given list is empty.
# You can expect all the tests to have valid chords.


def jazzify(lst):
    if lst == []:
        return lst
    else:
        return [item + "7" for item in lst]
print(jazzify([]))
print(jazzify(["G", "F", "C"]))



def jazzify(lst):
    lst2 =[]
    if lst == []:
        return lst
    for item in lst:
        if "7" in item:
            lst2.append(item)
            return lst2
        else:
            lst2.append(item + "7")
            return lst2
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))


# Return Inside Loop: The return statements inside the loop cause the function to return after processing just one item, 
# which is not what you want.



def jazzify(lst):
    lst2 = []
    for item in lst:
        if "7" in item:
            lst2.append(item)  
        else:
            lst2.append(item + "7")  
    return lst2  # Return the complete list after processing all items

# Example usage
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))  # Output: ['F7', 'E7', 'A7', 'Ab7', 'Gm7', 'C7']
print(jazzify(["F", "E", "A", "Ab", "Gm", "C"]))         # Output: ['F7', 'E7', 'A7', 'Ab7', 'Gm7', 'C7']








def jazzify(lst):
    # Create a new list to store the jazzified chords
    jazzified_list = []
    
    # Iterate through each chord in the provided list
    for chord in lst:
        # Check if the chord already ends with '7'
        if chord.endswith('7'):
            jazzified_list.append(chord)  # No modification needed
        else:
            jazzified_list.append(chord + '7')  # Append '7' to the chord
    
    return jazzified_list

# Example usage
print(jazzify(["G", "F", "C"]))            # Output: ["G7", "F7", "C7"]
print(jazzify(["Dm", "G", "E", "A"]))      # Output: ["Dm7", "G7", "E7", "A7"]
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))  # Output: ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
print(jazzify([]))                        # Output: []
