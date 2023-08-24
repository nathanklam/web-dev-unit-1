total_count = {'aluminum':135, 'plastic':102, 'paper':213}

def sort_items(item_string):
    for letter in item_string:
        if letter == "A":
            total_count["aluminum"] += 1
        elif letter == "P":
            total_count["plastic"] += 1
        elif letter == "R":
            total_count["paper"] += 1
        else:
            print("you cannot recycle this item")
    print(total_count)
    
sort_items('AAPAARRRRPAAPPRRP') 