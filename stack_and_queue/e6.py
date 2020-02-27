import unittest

from stack_and_queue.node import Node
from stack_and_queue.myqueue import MyQueue


class Animal:
    def __init__(self):
        pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter:
    def __init__(self):
        self.mixed_queue = MyQueue()
        self.dog_queue = MyQueue()
        self.cat_queue = MyQueue()

    def enqueue(self, animal):
        self.mixed_queue.add(animal)
        if isinstance(animal, Dog):
            self.dog_queue.add(animal)
        else:
            self.cat_queue.add(animal)

    def dequeue_any(self):
        animal = self.mixed_queue.remove()
        if isinstance(animal, Dog):
            self.dog_queue.remove()
        else:
            self.cat_queue.remove()

        return animal

    def dequeue_dog(self):
        animal = self.dog_queue.remove()  # 犬用のqueueから取り出す

        # 混合のqueueから取り出す
        if isinstance(self.mixed_queue.peek(), Dog):
            # 混合のqueueのpeekが犬のインスタンスの場合、peekを取り出して返す
            self.mixed_queue.remove()
            return animal

        # 混合のqueueのpeekが犬のインスタンスでない場合
        first = None
        while isinstance(self.mixed_queue.peek(), Cat):
            # 混合のqueueのpeekが猫のインスタンスである限り、混合用のqueueから取り出し続ける
            # その際、連結リストに保持する
            tmp = self.mixed_queue.remove()
            if not first:
                first = Node(tmp)
            else:
                first.appendToTail(tmp)

        # その後、連結リストに保持していた猫のインスタンスを順に混合用のqueueに詰め込む
        current = first
        while current:
            self.mixed_queue.add(current.data)
            current = current.next

        # 混合用のqueueから取り出した最初の猫のインスタンスが、peekになるように
        # queueの出し入れを行う
        while self.mixed_queue.peek() is not first.data:
            self.mixed_queue.add(self.mixed_queue.remove())

        return animal

    def dequeue_cat(self):
        animal = self.cat_queue.remove()  # 猫用のqueueから取り出す

        # 混合のqueueから取り出す
        if isinstance(self.mixed_queue.peek(), Cat):
            # 混合のqueueのpeekが猫のインスタンスの場合、peekを取り出して返す
            self.mixed_queue.remove()
            return animal

        # 混合のqueueのpeekが猫のインスタンスでない場合
        first = None
        while isinstance(self.mixed_queue.peek(), Dog):
            # 混合のqueueのpeekが犬のインスタンスである限り、混合用のqueueから取り出し続ける
            # その際、連結リストに保持する
            tmp = self.mixed_queue.remove()
            if not first:
                first = Node(tmp)
            else:
                first.appendToTail(tmp)

        # その後、連結リストに保持していた犬のインスタンスを順に混合用のqueueに詰め込む
        current = first
        while current:
            self.mixed_queue.add(current.data)
            current = current.next

        # 混合用のqueueから取り出した最初の犬のインスタンスが、peekになるように
        # queueの出し入れを行う
        while self.mixed_queue.peek() is not first.data:
            self.mixed_queue.add(self.mixed_queue.remove())

        return animal


class TestAnimalShelter(unittest.TestCase):
    def test_it(self):
        target = AnimalShelter()

        cat1 = Cat()
        cat2 = Cat()
        cat3 = Cat()
        cat4 = Cat()
        dog1 = Dog()
        dog2 = Dog()

        animals = [cat1, cat2, cat3, dog1, dog2, cat4]

        for animal in animals:
            target.enqueue(animal)

        self.assertIs(target.dequeue_any(), cat1)
        self.assertIs(target.dequeue_dog(), dog1)
        self.assertIs(target.dequeue_any(), cat2)
        self.assertIs(target.dequeue_cat(), cat3)
        self.assertIs(target.dequeue_cat(), cat4)
        self.assertIs(target.dequeue_dog(), dog2)
