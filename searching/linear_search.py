beasts = [ 'Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie']

print(beasts.index('Godzilla')) #linear - O(n)

for beast in range(len(beasts)):    #linear - O(n)
    if beasts[beast] == 'Godzilla':
        print(beast, beasts[beast])