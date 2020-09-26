class Stack:

    def __init__(self):
        self.container = []

    def push(self, elem):
        self.container.append(elem)

    def size(self):
        return len(self.container)

    def top(self, index):
        return self.container[index]

    def pop(self):
        return self.container.pop()


def solve():
    bubbles = list(map(int, input().split()))
    stack = []
    i = 0
    while i < len(bubbles):
        stack.append(bubbles[i])
        if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]:
            color = stack[-1]
            stack.pop()
            stack.pop()
            stack.pop()
            while i < len(bubbles) and bubbles[i] == color:
                i += 1
        else:
            i += 1
    print(len(bubbles) - len(stack))


if __name__ == "__main__":
    solve()
