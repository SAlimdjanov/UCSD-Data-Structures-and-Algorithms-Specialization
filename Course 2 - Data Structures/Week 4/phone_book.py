""" 
phone_book.py

"""


class Query:
    """
    Creates a query

    """

    def __init__(self, query):
        self.type = query[0]
        self.number = query[1]
        if self.type == "add":
            self.name = query[2]


def process_query(query, contacts):
    """
    Process input queries

    Args:
        query (Query): Query object
        contacts (dict): Dictionary of contacts

    Returns:
        str: Name associated with a queried phone number

    """
    if query.type == "add":
        contacts[query.number] = query.name
    elif query.type == "del":
        if query.number in contacts:
            del contacts[query.number]
    else:
        response = "not found"
        if query.number in contacts:
            response = contacts[query.number]
        return response


if __name__ == "__main__":
    num_n = int(input())
    contacts_dict = {}
    for _ in range(num_n):
        input_query = Query(input().split())
        result = process_query(input_query, contacts_dict)
        if result:
            print(result)
