#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
contacts_array = []


def add_contact(cont):
    contacts_array.append(cont)


def get_count_match_contacts(partial):
    count = 0
    for name in contacts_array:
        if name.startswith(partial):
            count += 1
    return count


def contacts(queries):
    result = []

    for query in queries:
        if len(query) > 1:
            if query[0] == "add":
                add_contact(query[1])
            elif query[0] == "find":
                result.append(get_count_match_contacts(query[1]))

    return result


queries_rows = int(input())

queries = []

for _ in range(queries_rows):
    queries.append(input().rstrip().split())

result = contacts(queries)

print('\n'.join(map(str, result)))
