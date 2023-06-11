import bisect
import operator


class SnapshotArray:
    def __init__(self, length: int):
        self.data = [[[0, 0]] for _ in range(length)]
        self.current_snapshot_id = 0

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][-1] == self.current_snapshot_id:
            self.data[index][-1][0] = val
            return

        self.data[index].append([val, self.current_snapshot_id])

    def snap(self) -> int:
        self.current_snapshot_id += 1
        return self.current_snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.data[index], snap_id, key=operator.itemgetter(-1)) - 1
        return self.data[index][snap_index][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)pass


if __name__ == "__main__":
    # print(Solution().replace_this_with_solution_method_name(["SnapshotArray", "set", "snap", "set", "get"],
    #                                                         [[3], [0, 5], [], [0, 6], [0, 0]]))
    s = SnapshotArray(4)
    s.snap()
    s.snap()
    s.set(2, 4)
    s.snap()
    s.set(1, 4)
    print(s.data)