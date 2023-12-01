from __future__ import annotations


class ListNode(object):

    def __init__(self, previous_node, next_node, value):
        self.previous: ListNode = previous_node
        self.next: ListNode = next_node
        self.value: ListNode = value

    def clear(self):
        self.previous = None
        self.next = None
        self.value = None

    def __str__(self):
        return f"(value={self.value}, next_node={self.next})"


class LinkedList(object):

    def __init__(self):
        self.first: ListNode | None = None
        self.current: ListNode | None = None
        self.last: ListNode | None = None

    def add_all(self, linked_list):
        linked_list: LinkedList
        tmp = self.current
        linked_list.to_first()

        while linked_list.has_access():
            self.append(linked_list.current)
            linked_list.next()
        self.current = tmp

    def append(self, value):
        if self.first is None:
            node = ListNode(None, None, value)
            self.first = node
            self.current = node
            self.last = node
            return node
        else:
            node: ListNode = ListNode(self.last, None, value)
            self.last.next = node
            self.last = node
            return node

    def insert(self, value):
        if self.is_empty():
            return self.append(value)
        if value == self.last.value:
            return self.append(value)
        if self.current == self.first:
            tmp = self.current
            self.current = self.current.next
            node = self.insert(value)
            self.current = tmp
            return node

        prev = self.current.previous

        node = ListNode(self.current.previous, self.current, value)

        prev.next = node
        node.previous = prev

        node.next = self.current
        self.current.previous = node

        return node

    def remove(self):
        if not self.is_empty() and self.has_access():
            if self.current == self.first:
                tmp = self.first
                self.first = self.first.next
                self.current = self.first
                tmp.clear()
                return
            elif self.current == self.last:
                self.last.previous.next = None
                tmp = self.last
                self.last = self.last.previous
                self.current = self.last
                tmp.clear()
            else:
                prev = self.current.previous
                tmp = self.current
                nxt = self.current.next

                nxt.previous = prev
                prev.next = self.current.next
                tmp.clear()

            if self.is_empty():
                self.last = None

    def remove_value(self, value):
        tmp = self.current
        self.to_first()
        while self.has_access():
            if self.get_value() is value:
                self.remove()
                break
            self.next()
        self.current = tmp

    def set_value(self, value):
        if self.has_access():
            self.current.value = value
        else:
            raise NoSuchElementException("No node present.")

    def get_value(self):
        if self.current is not None:
            return self.current.value
        return None

    def clear(self):
        self.to_first()
        while self.has_access():
            self.remove()

    def has_access(self):
        return self.current is not None

    def next(self):
        if self.has_access():
            self.current = self.current.next
        else:
            raise NoSuchElementException("No node present.")
        return self.current

    def is_empty(self):
        return self.first is None

    def to_first(self):
        self.current = self.first

    def to_last(self):
        self.current = self.last

    def values(self) -> list:
        tmp = self.current
        self.to_first()
        values = []
        while self.has_access():
            values.append(self.get_value())
            self.next()
        self.current = tmp

        return values

    def __str__(self):
        return f"(first={self.first}, current={self.current}, last={self.last})"


def from_list(l: list) -> LinkedList:
    ll = LinkedList()

    for x in l:
        ll.append(x)

    return ll


class NoSuchElementException(Exception):

    def __int__(self, message):
        self.args = message
