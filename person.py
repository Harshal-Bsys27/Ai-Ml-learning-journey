"""Tiny class example demonstrating basic OOP."""

class Person:
    def __init__(self, name: str, age: int = None):
        self.name = name
        self.age = age

    def greet(self) -> str:
        if self.age is not None:
            return f"Hi, I'm {self.name} and I'm {self.age} years old."
        return f"Hi, I'm {self.name}."


if __name__ == "__main__":
    p = Person("Harshal", 26)
    print(p.greet())
    p2 = Person("Alex")
    print(p2.greet())
