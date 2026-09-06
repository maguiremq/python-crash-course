# 5-13. Your Ideas: At this point, you’re a more capable programmer than you
# were when you started this book. Now that you have a better sense of how
# real-world situations are modeled in programs, you might be thinking of some
# problems you could solve with your own programs. Record any new ideas you
# have about problems you might want to solve as your programming skills continue
# to improve. Consider games you might want to write, datasets you might
# want to explore, and web applications you’d like to create.

import random

states = [
    'florida'
    , 'georgia'
    , 'massachussetts'
]

crimes = [
    'resisting arrest without violence'
    , 'domestic violence'
    , 'driving under the influence'
    , 'racketeering'
    , 'drug possession'
]

store_states_counts = list()

for state in states:
    for crime in crimes:
        store_states_counts.append(state)
        store_states_counts.append(crime)
        store_states_counts.append(random.randint(1, 100))

print(store_states_counts)


    

