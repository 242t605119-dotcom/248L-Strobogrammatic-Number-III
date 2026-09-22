class Solution:
    def strobogrammaticInRange(self, low, high):
        pairs = [
            ('0', '0'),
            ('1', '1'),
            ('6', '9'),
            ('8', '8'),
            ('9', '6')
        ]

        count = 0

        def build(left, right):
            nonlocal count

            if left > right:
                if len(low) <= len(current) <= len(high):
                    if len(current) == len(low) and current < low:
                        return
                    if len(current) == len(high) and current > high:
                        return
                    count += 1
                return

            for a, b in pairs:
                if left == 0 and right > 0 and a == '0':
                    continue

                current[left] = a
                current[right] = b

                if left == right:
                    if a in '018':
                        build(left + 1, right - 1)
                else:
                    build(left + 1, right - 1)

        for length in range(len(low), len(high) + 1):
            current = [''] * length
            build(0, length - 1)

        return count
