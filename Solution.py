import os

def solve():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(BASE_DIR, "input.txt")
    output_path = os.path.join(BASE_DIR, "output.txt")

    if not os.path.exists(input_path):
        print("Input file not found!")
        return

    with open(input_path, 'r') as f:
        data = f.read().strip().split()

    if not data:
        return

    n = int(data[0])
    blocks_data = list(map(int, data[1:]))

    blocks = []
    idx = 1
    for i in range(0, n * 3, 3):
        dims = sorted(blocks_data[i:i+3], reverse=True)
        x, y, z = dims
        blocks.append((x, y, z, idx))
        idx += 1

    best_single_stability = -1
    best_single_index = -1
    for x, y, z, index in blocks:
        if z > best_single_stability:
            best_single_stability = z
            best_single_index = index

    groups = {}
    for x, y, z, index in blocks:
        groups.setdefault((x, y), []).append((z, index))

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
            best_pair_indices = tuple(sorted((idx1, idx2)))

    if best_single_stability >= best_pair_stability:
        num_blocks = 1
        indices = str(best_single_index)
        max_diameter = best_single_stability
    else:
        num_blocks = 2
        indices = f"{best_pair_indices[0]} {best_pair_indices[1]}"
        max_diameter = best_pair_stability

    with open(output_path, 'w') as f:
        f.write(f"{num_blocks}\n{indices}\n{max_diameter}\n")


if __name__ == "__main__":
    solve()
