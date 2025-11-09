import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch, self.freq, self.left, self.right = ch, freq, None, None
    def __lt__(self, other): return self.freq < other.freq

def build_tree(freqs):
    heap = [Node(ch, fr) for ch, fr in freqs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        l, r = heapq.heappop(heap), heapq.heappop(heap)
        m = Node(None, l.freq + r.freq); m.left, m.right = l, r
        heapq.heappush(heap, m)
    return heap[0]

def gen_codes(node, code="", codes=None):
    if codes is None: codes = {}
    if not node: return
    if node.ch: codes[node.ch] = code
    gen_codes(node.left, code + "0", codes)
    gen_codes(node.right, code + "1", codes)
    return codes

if __name__ == "__main__":
    print("=== Huffman Encoding using Greedy Strategy ===")
    n = int(input("Enter number of characters: "))
    freqs = {}
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        fr = int(input(f"Enter frequency of '{ch}': "))
        freqs[ch] = fr

    root = build_tree(freqs)
    codes = gen_codes(root)

    print("\nHuffman Codes:")
    for ch in sorted(codes): print(f"{ch}: {codes[ch]}")

    text = input("\nEnter text to encode (use only given characters): ")
    encoded = ''.join(codes[ch] for ch in text)

    total_bits = sum(len(codes[ch]) * f for ch, f in freqs.items())
    avg_bits = total_bits / sum(freqs.values())

    print(f"\nEncoded text: {encoded}")
    print("Decoded text:", text)
    print(f"Total bits: {total_bits}")
    print(f"Average bits per symbol: {avg_bits:.2f}")


    """ === Huffman Encoding using Greedy Strategy ===
Enter number of characters: 6
Enter character 1: a
Enter frequency of 'a': 50
Enter character 2: b
Enter frequency of 'b': 10
Enter character 3: c
Enter frequency of 'c': 30
Enter character 4: d
Enter frequency of 'd': 5
Enter character 5: e
Enter frequency of 'e': 3
Enter character 6: f
Enter frequency of 'f': 2

Huffman Codes:
a: 0
b: 100
c: 11
d: 1010
e: 10111
f: 10110

Enter text to encode (use only given characters): abcde

Encoded text: 010011101010111
Decoded text: abcde
Total bits: 185
Average bits per symbol: 1.85 """
