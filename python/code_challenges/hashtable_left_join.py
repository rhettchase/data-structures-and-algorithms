from data_structures.hashtable import Hashtable

def left_join(syn_hash, ant_hash):
    joined_data = {}
    for key, value in syn_hash.items():
        joined_data[key] = [value] # put key value pairs from synonyms in the dictionary, with the value in a list

        # antonym exists, add to the list
        if key in ant_hash: # O(1)
            joined_data[key].append(ant_hash[key]) # append value
        else:
            joined_data[key].append("NONE")
    return joined_data


