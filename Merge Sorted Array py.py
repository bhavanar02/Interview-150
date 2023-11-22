def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Test
nums1_1 = [1, 2, 3, 0, 0, 0]
m_1 = 3
nums2_1 = [2, 5, 6]
n_1 = 3
merge(nums1_1, m_1, nums2_1, n_1)
print(nums1_1)  # Output: [1, 2, 2, 3, 5, 6]