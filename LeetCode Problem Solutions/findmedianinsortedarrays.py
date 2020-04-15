class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        imax = len(nums1)
        jmax = len(nums2)
        i = 0
        j = 0
        
        while i < imax and j < jmax:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
                
            else: #nums2 > nums1
                nums3.append(nums2[j])
                j += 1
                
        while i == imax and j < jmax: 
            nums3.append(nums2[j])
            j += 1
            
        while i < imax and j == jmax:
            nums3.append(nums1[i])
            i += 1
            
        
        if len(nums3) % 2 == 0: # even
            median_index_floor = (len(nums3)-1) // 2
            median_index_ceiling = median_index_floor + 1
            median = (nums3[median_index_floor] + nums3[median_index_ceiling]) / 2
            return median
        
        
        else: #odd
            median_index = len(nums3) // 2
            return nums3[median_index]
