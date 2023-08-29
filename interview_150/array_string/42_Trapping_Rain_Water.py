"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

* n == height.length
* 1 <= n <= 2 * 104
* 0 <= height[i] <= 105
"""

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height):
    hlen = len(height)
    if hlen <= 2:
        return 0

    water = 0

    left, right = 1, hlen - 1
    lmax, rmax = height[0], height[-1]

    while left <= right:
        if height[left] > lmax:
            lmax = height[left]

        if height[right] > rmax:
            rmax = height[right]

        if lmax <= rmax:
            water += lmax - height[left]
            left += 1
        else:
            water += rmax - height[right]
            right -= 1
    return water


print(trap(height))
