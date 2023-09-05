from collections import Counter
song_data = [
    {
        "title": "Groove Machine",
        "artist": "Funk Fusion",
        "genre": "Funk",
        "duration": 180,
        "energy": 0.85,
        "danceability": 0.75,
        "tempo": 110,
    },
    {
        "title": "Sunset Serenade",
        "artist": "Chillwave Collective",
        "genre": "Electronic",
        "duration": 240,
        "energy": 0.55,
        "danceability": 0.65,
        "tempo": 100,
    },
    {
        "title": "Guitar Grooves",
        "artist": "Acoustic Ensemble",
        "genre": "Acoustic",
        "duration": 210,
        "energy": 0.6,
        "danceability": 0.4,
        "tempo": 80,
    },
    {
        "title": "Rock Anthem",
        "artist": "Electric Rebellion",
        "genre": "Rock",
        "duration": 280,
        "energy": 0.9,
        "danceability": 0.6,
        "tempo": 140,
    },
    {
        "title": "Jazz Reflections",
        "artist": "Smooth Jazz Quartet",
        "genre": "Jazz",
        "duration": 320,
        "energy": 0.4,
        "danceability": 0.3,
        "tempo": 90,
    },
]

#first "person (me)"
def collect_data(data, type):
    collected_data = []
    for i in range(len(data)):
        collected_data.append(data[i][type])
    return collected_data

collected_data = collect_data(song_data, "duration")
print(collected_data)
 
#second "person (me)"
def calculate_statistics(list, identifier):
    if identifier == "MEAN":
        total = sum(list)
        mean = total / len(list)
        print(mean)
    elif identifier == "MODE":
        counts = Counter(list)
    # Find the element(s) with the maximum count
        max_count = max(counts.values())
        mode = [element for element, count in counts.items() if count == max_count]
        print(mode)
    elif identifier == "MEDIAN":
        sorted_list = sorted(list)
        n = len(sorted_list)
        if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
            median = sorted_list[n // 2]
        else:
            # If the length of the list is even, the median is the average of the two middle elements
            middle1 = sorted_list[(n // 2) - 1]
            middle2 = sorted_list[n // 2]
            median = (middle1 + middle2) / 2
        print(median)

calculate_statistics(collected_data,"MEAN")
