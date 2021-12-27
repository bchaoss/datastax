from typing import Any

from datastax.linkedlists import LinkedList


def test(array: list[Any] = None) -> None:
    ll = LinkedList(array)
    print(f"Head: {ll.head}")  # printing head
    print(ll)  # Printing linkedList itself


test([*range(10)])
test()  # constructing with nothing
test([])  # constructing with empty list
test([None])  # constructing wih a null value
test([None, 1, 2, 3, 4, 5])  # constructing with values where first item being NULL
#########################
LL = LinkedList([1, 2, 3, 4, 5, 6])  # Insertion inside filled list
LL.insert(10)  # Insertion at the front
LL.append(100)  # Insertion at the back
print(LL)
######################
LL = LinkedList()  # Insertion inside empty list
LL.insert(1)  # Insertion at the front
LL.append(2)  # Insertion at the back
print(LL)

LL = LinkedList()
print(LL)
LL.insert(10)
LL.insert(11)
LL.append(90)
LL.insert(199)
LL.append(109)
print(LL)

D = LinkedList([*range(5)])
D.insert(10)
D.insert(20)
D.append(199)
print(D)
# print(D.__str__(True))
