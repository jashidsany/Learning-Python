# __init__(), our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup.
# __iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. For more information on iterators, review Python’s documentation of Iterator Types.
# __len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
# __contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.

# These methods allow UserGroup to act like a list using syntax Python programmers will already be familiar with. If all you need is something to act like a list you could absolutely have used a list, but if you want to bundle some other information (like a group’s permissions, for instance) having syntax that allows for list-like operations can be very powerful.

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
