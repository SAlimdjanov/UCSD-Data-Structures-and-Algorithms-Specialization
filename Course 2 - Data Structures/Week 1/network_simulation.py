""" 
network_simulation.py

"""

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    """
    Buffer class

    """

    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        """
        Simulates the processing of network packets

        Args:
            request (named tuple): Instance of the request named tuple

        Returns:
            named tuple: Indicates the packet processing status
        """
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)

        if len(self.finish_time) >= self.size:
            return Response(True, -1)

        if not self.finish_time:
            start_time = request.arrived_at
        else:
            start_time = max(self.finish_time[-1], request.arrived_at)

        finish_time = start_time + request.time_to_process
        self.finish_time.append(finish_time)

        return Response(False, start_time)


def process_requests(requests, buffer):
    """
    Processes input requests using a given buffer

    Args:
        requests (int list): List of network requests
        buffer (class Buffer): Buffer object

    Returns:
        int list: Response list

    """
    responses = []

    for request in requests:
        responses.append(buffer.process(request))

    return responses


def main():
    """
    main method

    """
    buffer_size, n_requests = map(int, input().split())
    requests = []

    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
