"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linkedlist data structure

animal_shelter = FIFO/Queue, can select type of animal (dog vs cat)
    -2 linked lists (dog & cat)
        - add to end
        - remove from beginning

Animal class:
    -breed: id's as cat or dog
    -next_animal: points to next animal regardless of breed
    
Dog class(Animal):
    -next_dog: points to next dog

Cat class(Animal):
    -next_cat: points to next cat

Animal shelter:
    -add: adds animal object, sets next_animal and next_cat/dog
    -remove_first(breed): removes the first animal or dog/cat if specified in breed
    -peek(breed): peeks at first animal or dog/cat if specified in breed
    -isEmpty

"""

class Animal:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        return str(self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = 'dog'
        self.next_dog = None

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = 'cat'
        self.next_cat = None


class animalShelter:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = data
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next: # Travsering the linked list
            if current_node.breed == new_node.breed: # While traversing compare new_node to current_node
                if new_node.breed == 'dog' and current_node.next_dog is None: 
                    current_node.next_dog = new_node
                elif new_node.breed == 'cat' and current_node.next_cat is None:
                    current_node.next_cat = new_node
            current_node = current_node.next
        current_node.next = new_node # Once you hit the last node add new_node
        if current_node.breed == new_node.breed:
            if new_node.breed == 'dog':
                current_node.next_dog = new_node
            else:
                current_node.next_cat = new_node            


    def remove_first(self, breed = None):
        if self.head is None:
            return
        
        current_animal = self.head
        if breed is None:
            print('Removing:', self.head)
            self.head = self.head.next
        elif breed == current_animal.breed:
            print('Removing:', self.head)
            self.head = self.head.next
        else:
            while current_animal.next:
                if breed == current_animal.next.breed:
                    print('Removing:', current_animal.next)
                    current_animal.next = current_animal.next.next
                    return
                else:
                    current_animal = current_animal.next

    
    def peek(self, breed = None):
        current_animal = self.head
        if self.head is None:
            return
        elif breed is None:
            return self.head
        elif breed == current_animal.breed:
                return current_animal
        else:
            while current_animal.next:
                if breed == current_animal.next.breed:
                    # print('Current animal:', current_animal.next, current_animal.next.breed)
                    return current_animal.next
                else:
                    current_animal = current_animal.next
                    

    def isEmpty(self):
        return self.head is None
    
    def viewAll(self):
        if self.head is None:
            return
        
        current_node = self.head
        while current_node:
            print(current_node, current_node.breed)
            current_node = current_node.next
    
# Testing:

shelter = animalShelter()
dog1 = Dog('d1')
dog2 = Dog('d2')
dog3 = Dog('d3')
cat1 = Cat('c1')
cat2 = Cat('c2')
cat3 = Cat('c3')
shelter.add(dog1)
# shelter.add(dog2)
# shelter.add(dog3)
shelter.add(cat1)
shelter.add(cat2)
shelter.add(cat3)
print('Roster:')
shelter.viewAll()
print('Peek first:', shelter.peek())
print('Peek first dog:', shelter.peek('dog'))
print('Peek first cat:', shelter.peek('cat'))
shelter.remove_first()
print('Peek first:', shelter.peek())
print('Peek first dog:', shelter.peek('dog'))
print('Peek first cat:', shelter.peek('cat'))
print('Roster:')
shelter.viewAll()
shelter.remove_first('dog')
print('Peek first:', shelter.peek())
print('Peek first dog:', shelter.peek('dog'))
print('Peek first cat:', shelter.peek('cat'))
print('Roster:')
shelter.viewAll()
shelter.remove_first('cat')
print('Peek first:', shelter.peek())
print('Peek first dog:', shelter.peek('dog'))
print('Peek first cat:', shelter.peek('cat'))
print('Roster:')
shelter.viewAll()


                

