"""
Working with a list
Poshun Lin

Making lists and modify them. This file is to add more items to the previous list.
No starter code was used. This program was written from scratch

01/31/2026
"""

from Lab3_Poshun_list import items
items.extend(["tent poles","a set of closthes","lighter","toothbrush","cup"])
items.sort(reverse=True)
print(items)