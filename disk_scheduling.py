import sys

def print_header(title):
    print(f"\n{'='*50}")
    print(f"{title:^50}")
    print(f"{'='*50}")

def print_table_header():
    print(f"{'Step':<5} | {'From':<6} | {'To':<6} | {'Seek Distance':<15}")
    print("-" * 45)

def fcfs(requests, head):
    print_header("FCFS Disk Scheduling")
    current = head
    total_seek = 0
    sequence = [head]

    print_table_header()

    for i, req in enumerate(requests, 1):
        distance = abs(req - current)
        total_seek += distance
        print(f"{i:<5} | {current:<6} | {req:<6} | {distance:<15}")
        current = req
        sequence.append(req)

    print(f"\nTotal Seek Time: {total_seek}")
    return total_seek, sequence


def sstf(requests, head):
    print_header("SSTF Disk Scheduling")
    current = head
    total_seek = 0
    sequence = [head]
    pending = requests.copy()

    print_table_header()

    step = 1
    while pending:
        closest = min(pending, key=lambda x: abs(x - current))
        distance = abs(closest - current)
        total_seek += distance

        print(f"{step:<5} | {current:<6} | {closest:<6} | {distance:<15}")

        current = closest
        sequence.append(closest)
        pending.remove(closest)
        step += 1

    print(f"\nTotal Seek Time: {total_seek}")
    return total_seek, sequence


def scan(requests, head, disk_size, direction="up"):
    print_header(f"SCAN Disk Scheduling ({direction.upper()})")
    current = head
    total_seek = 0
    sequence = [head]

    reqs = sorted(requests)
    left = [r for r in reqs if r < head]
    right = [r for r in reqs if r >= head]

    if direction == "up":
        path = right + [disk_size - 1] + left[::-1]
    else:
        path = left[::-1] + [0] + right

    print_table_header()

    for step, req in enumerate(path, 1):
        distance = abs(req - current)
        total_seek += distance

        print(f"{step:<5} | {current:<6} | {req:<6} | {distance:<15}")

        current = req
        sequence.append(req)

    print(f"\nTotal Seek Time: {total_seek}")
    return total_seek, sequence


def cscan(requests, head, disk_size):
    print_header("C-SCAN Disk Scheduling")
    current = head
    total_seek = 0
    sequence = [head]

    reqs = sorted(requests)
    left = [r for r in reqs if r < head]
    right = [r for r in reqs if r >= head]

    path = right + [disk_size - 1, 0] + left

    print_table_header()

    for step, req in enumerate(path, 1):
        distance = abs(req - current)
        total_seek += distance

        print(f"{step:<5} | {current:<6} | {req:<6} | {distance:<15}")

        current = req
        sequence.append(req)

    print(f"\nTotal Seek Time: {total_seek}")
    return total_seek, sequence


def main():
    try:
        if len(sys.argv) > 1:
            req_str = sys.argv[1]
            head = int(sys.argv[2])
            disk_size = int(sys.argv[3])
            requests = list(map(int, req_str.split()))
        else:
            req_str = input("Enter request queue (space separated): ")
            requests = list(map(int, req_str.split()))
            head = int(input("Enter initial head position: "))
            disk_size = int(input("Enter disk size: "))
    except:
        print("\nUsage:")
        print('python3 disk.py "98 183 37 122 14 124 65 67" 53 200')
        return

    print("\nInput Summary:")
    print(f"Requests: {requests}")
    print(f"Initial Head: {head}")
    print(f"Disk Size: {disk_size}")

    results = {}

    results["FCFS"], _ = fcfs(requests, head)
    results["SSTF"], _ = sstf(requests, head)
    results["SCAN"], _ = scan(requests, head, disk_size)
    results["C-SCAN"], _ = cscan(requests, head, disk_size)

    print("\n" + "="*50)
    print(f"{'ALGORITHM':<20} | {'TOTAL SEEK TIME':<20}")
    print("-" * 50)

    for algo, seek in results.items():
        print(f"{algo:<20} | {seek:<20}")

    print("="*50)

    best = min(results, key=results.get)
    worst = max(results, key=results.get)

    print(f"\nBest Algorithm  : {best}")
    print(f"Worst Algorithm : {worst}")


if __name__ == "__main__":
    main()
