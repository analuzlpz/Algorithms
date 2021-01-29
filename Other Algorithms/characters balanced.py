# Complete the isBalanced function below.
from queue import LifoQueue


def isBalanced(s):
    characters = {"{": "}", "[": "]", "(": ")"}
    stack = LifoQueue()
    result = True

    for character in s:
        if character in characters.keys():
            stack.put(character)
        else:
            if (stack.empty()):
                result = False
                break
            else:
                element_prev = stack.get()
                if characters[element_prev] != character:
                    result = False
                    break

    if stack.empty() and result:
        result_ret = "YES"
    else:
        result_ret = "NO"
    return result_ret


t = int(input())

for t_itr in range(t):
    s = input()

    result = isBalanced(s)

    print(str(result))
