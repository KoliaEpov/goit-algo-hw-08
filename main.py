import heapq


def minConnectOrder(cabel_list):
    heapq.heapify(cabel_list)
    connect_count = 0
    while len(cabel_list) > 1:
        smallest_first = heapq.heappop(cabel_list)
        smallest_second = heapq.heappop(cabel_list)
        cost = smallest_first[0] + smallest_second[0]
        name = smallest_first[1] + smallest_second[1]
        heapq.heappush(cabel_list, (cost, name))
        connect_count += cost

    return connect_count


def main():
    cabel_list = [
        (2, "cabel1"),
        (5, "cabel2"),
        (8, "cabel3"),
        (3, "cabel4"),
        (2, "cabel5"),
        (2, "cabel6"),
        (1, "cabel7"),
        (2, "cabel8"),
        (5, "cabel9"),
    ]

    print(minConnectOrder(cabel_list))


if __name__ == "__main__":
    main()
