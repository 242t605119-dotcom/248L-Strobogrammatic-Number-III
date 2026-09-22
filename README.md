# LeetCode 248 - Strobogrammatic Number III

## Problem

Given two strings `low` and `high`, return the number of strobogrammatic numbers that lie in the inclusive range `[low, high]`.

A strobogrammatic number looks the same when rotated 180 degrees.

## Example

### Input

```text
low = "50"
high = "100"
```

### Output

```text
3
```

The strobogrammatic numbers in the range are:

```text
69
88
96
```

## Approach

Generate all possible strobogrammatic numbers for every length between the lengths of `low` and `high`.

Build each number from the outside toward the center using these valid pairs:

```text
00
11
69
88
96
```

The number cannot start with `0` unless it contains only one digit.

After constructing a number, check whether it falls within the given range.

## Algorithm

1. Generate numbers for every length from `len(low)` to `len(high)`.
2. Build each number using valid strobogrammatic digit pairs.
3. Avoid leading zeroes.
4. For odd lengths, allow only `0`, `1`, or `8` in the center.
5. Compare each generated number with `low` and `high`.
6. Count the valid numbers.
7. Return the count.

## Complexity

* Time Complexity: `O(5^(n/2))`
* Space Complexity: `O(n)`

Where `n` is the maximum length of the numbers.

## Language

Python

## LeetCode

Problem: 248 - Strobogrammatic Number III

## Author

**T.Nandhini**
