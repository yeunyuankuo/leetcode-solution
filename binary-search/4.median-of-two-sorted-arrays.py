class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # time: O(log(min(nums1, nums2)))
        # space: O(1)
        total = len(nums1) + len(nums2)
        half = total // 2

        # we want A to be the smaller length of the two arrays
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # do binary search on the A array
        # l, r keeps track of the left and right pointer of A array
        l, r = 0, len(A) - 1
        while True:
            midA = (l + r) // 2
            midB = half - midA - 2 # elements before and including midA and midB will add up to be the left half of the total array

            leftA = A[midA] if midA >= 0 else float("-infinity")
            rightA = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            leftB = B[midB] if midB >= 0 else float("-infinity")
            rightB = B[midB + 1] if (midB + 1) < len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    # odd: the central element (the median) is the next smallest element after leftA and leftB
                    return min(rightA, rightB) # why only compare rightA, rightB?
                else: 
                    # even
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

            # If rightA < leftB, it means our partition is too far left, and we need to move right; thus we adjust the left pointer l.
            if rightA < leftB:
                l = midA + 1
            else:
                r = midA - 1