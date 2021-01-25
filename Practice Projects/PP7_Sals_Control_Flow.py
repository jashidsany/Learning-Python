# Uses control flow by way of if-else statements.
ground_shipping_flat_charge = 20
premium_ground_shipping = 125
drone_shipping_flat_charge = 0

def ground_shipping_cost(weight):
  if (weight <= 2):
   cost = (weight * 1.50 + ground_shipping_flat_charge)
   return cost
  elif (weight > 2) and (weight <= 6):
    cost = (weight * 3.00 + ground_shipping_flat_charge)
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = (weight * 4.00 + ground_shipping_flat_charge)
    return cost
  else:
    cost = (weight * 4.75 + ground_shipping_flat_charge)
    return cost

def drone_shipping_cost(weight):
  if (weight <= 2):
   cost = (weight * 4.50 + drone_shipping_flat_charge)
   return cost
  elif (weight > 2) and (weight <= 6):
    cost = (weight * 9.00 + drone_shipping_flat_charge)
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = (weight * 12.00 + drone_shipping_flat_charge)
    return cost
  else:
    cost = (weight * 14.25 + drone_shipping_flat_charge)
    return cost

def cheapest_option(weight):
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)
  premium = premium_ground_shipping

  if (ground < drone) and (ground < premium):
    return("Ground shipping is the cheapest and it costs $" + str(ground))
  elif (drone < ground) and (drone <premium):
    return("Drone shipping is the cheapest and it costs $" + str(drone))
  else:
    return("Premium shipping is the cheapest and it costs $" + str(premium))

# test for ground
print(ground_shipping_cost(8.4))

# test for drone
print(drone_shipping_cost(1.5))

# test for 2.0lb of package
print(cheapest_option(2))

# test for 4.8lb of package
print(cheapest_option(4.8))

# test for 41.5lb of package
print(cheapest_option(41.5))
