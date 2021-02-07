import sys


def check_list(lst, nums):
    pos = {}  # the position of each number in the list
    sg = {}  # the graph
    for i in nums:
        pos[i] = []
        sg[i] = []  # empty
    for i in range(len(lst)):
        j = lst[i]
        pos[lst[i]].append(i)
    for k in range(len(nums)):
        for l in range(k+1, len(nums)):
            i = nums[k]
            j = nums[l]
            if pos[i] and pos[j]:  # both appear in the lst
                if pos[i][0] < pos[j][0] < pos[i][-1]:  # j is between i
                    sg[j].append(i)
                elif pos[j][0] < pos[i][0] < pos[j][-1]:  # i is between j
                    sg[i].append(j)
    return sg


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    p = []
    N = int(input())
    nums = set()
    for i in range(N):
        p.append([])
        for j in list(input()):
            j = int(j)
            nums.add(j)
            p[i].append(j)
    graph = []
    nums = list(nums)
    for i in nums:
        graph.append(set())
    for i in range(N):
        # check each row
        row = p[i]
        col = [p[j][i] for j in range(N)]
        sg = check_list(row, nums)
        for j in sg:
            for k in sg[j]:
                graph[j].add(k)
    print(graph)





if __name__ == "__main__":
    main('art')
