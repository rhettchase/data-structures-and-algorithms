from data_structures.queue import Queue

def duck_duck_goose(players_list, k):
    queue = Queue()

    for player in players_list:
        queue.enqueue(player)

    while not queue.is_empty():
        print("Starting new round")  # Indicate the start of a new round
        for i in range(k): # for k times
            player = queue.dequeue()
            if i < k - 1: # if i = k, the player is the Goose and they do not enqueue
                queue.enqueue(player)
    return player

# Example usage
players_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
k = 3
result = duck_duck_goose(players_list, k)
print(f"The winner is: {result}")
