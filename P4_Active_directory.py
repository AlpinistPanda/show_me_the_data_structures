class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == None:
        return "User input missing"
    elif group == None:
        return "Group input missing"
    if not isinstance(group, Group):
        return "Invalid group!"

    users = group.get_users()
    groups = group.get_groups()

    for sub_user in users:
        if sub_user == user:
            return True
    for sub_group in groups:
        return is_user_in_group(user, sub_group)
    return False


# all assert should be pass
parent = Group("parent")
assert(is_user_in_group("parent", parent) == False)
child = Group("child")
sub_child = Group("subchild")
sub_sub_child = Group("sub2child")

sub_sub_child.add_user("sub2child")
assert(is_user_in_group("sub2child", parent) == False)
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_user("youngqueenz")

sub_child.add_group(sub_sub_child)
assert(is_user_in_group("sub2child", sub_child) == True)
child.add_group(sub_child)
parent.add_group(child)
assert(is_user_in_group("youngqueenz", parent) == True)

assert(is_user_in_group('youngqueenz', 'group') == "Invalid group!")
assert(is_user_in_group('youngqueenz') == 'Group input missing')
assert(is_user_in_group(group=parent) == "User input missing")
