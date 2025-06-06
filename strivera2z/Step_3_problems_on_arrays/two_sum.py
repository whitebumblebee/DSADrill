"""
problem link:
https://www.naukri.com/code360/problems/reading_6845742?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""

def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    book_set = set(book)
    for book in book_set:
        if (target - book) in book_set:
            return "YES"
    return "NO" 