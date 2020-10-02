#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Starts with ticket source None and rearranges tickets based on destination.
    """
    cache = {}
    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    next_route = cache['NONE']

    for i in range(0, length):
        route[i] = next_route
        next_route = cache[next_route]

    return route
