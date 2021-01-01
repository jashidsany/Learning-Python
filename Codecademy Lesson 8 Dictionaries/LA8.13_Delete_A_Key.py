# Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:
# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
# When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this.
# Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains")
# adds the value of stamina grians to health_points using +=
health_points += available_items.pop("power stew")
# adds the value of power stew to health_points using +=
health_points += available_items.pop("mystic bread", 0)
# adds the value of mystic bread to health_points using +=, however mystic bread does not exist in the available_items dictionary so we pass in a default value of 0
print(available_items)
print(health_points)
