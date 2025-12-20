import os


# =================================
# Simple Hash Table (Chaining)
# =================================
class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Simple hash function: h(x, y) = (x + y) mod M
        return (key[0] + key[1]) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        bucket = self.table[h]

        for item in bucket:
            if item[0] == key:
                item[1].append(value)
                return

        bucket.append([key, [value]])

    def items(self):
        for bucket in self.table:
            for key, values in bucket:
                yield key, values


# =================================
# Main Solution
# =================================
def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "input.txt")
    output_path = os.path.join(base_dir, "output.txt")

    if not os.path.exists(input_path):
        print("Input file not found.")
        return

    with open(input_path, "r") as f:
        data = f.read().strip().split()

    if not data:
        return

    n = int(data[0])
    nums = list(map(int, data[1:]))

    blocks = []
    idx = 1

    for i in range(0, n * 3, 3):
        dims = sorted(nums[i:i + 3], reverse=True)
        x, y, z = dims
        blocks.append((x, y, z, idx))
        idx += 1

    # -----------------------------
    # Best single block
    # -----------------------------
    best_single_stability = -1
    best_single_index = -1

    for x, y, z, index in blocks:
        if z > best_single_stability:
            best_single_stability = z
            best_single_index = index

    # -----------------------------
    # Group blocks using Hash Table
    # -----------------------------
    groups = HashTable()

    for x, y, z, index in blocks:
        groups.insert((x, y), (z, index))

    # -----------------------------
    # Best pair of blocks
    # -----------------------------
    best_pair_stability = -1
    best_pair_indices = (-1, -1)

    for (x, y), block_list in groups.items():
        if len(block_list) < 2:
            continue

        block_list.sort(reverse=True)

        z1, idx1 = block_list[0]
        z2, idx2 = block_list[1]

        pair_stability = min(y, z1 + z2)

        if pair_stability > best_pair_stability:
            best_pair_stability = pair_stability
            if idx1 < idx2:
                best_pair_indices = (idx1, idx2)
            else:
                best_pair_indices = (idx2, idx1)

    # -----------------------------
    # Final Answer
    # -----------------------------
    if best_single_stability >= best_pair_stability:
        num_blocks = 1
        indices = str(best_single_index)
        max_diameter = best_single_stability
    else:
        num_blocks = 2
        indices = f"{best_pair_indices[0]} {best_pair_indices[1]}"
        max_diameter = best_pair_stability

    with open(output_path, "w") as f:
        f.write(f"{num_blocks}\n")
        f.write(f"{indices}\n")
        f.write(f"{max_diameter}\n")


if __name__ == "__main__":
    solve()
