dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breeds in dog_breeds_available_for_adoption:
  print(breeds)
  if dog_breed_I_want == breeds:
    print("They have the dog I want!")
    break # using break does not iterate the rest of the loop 
