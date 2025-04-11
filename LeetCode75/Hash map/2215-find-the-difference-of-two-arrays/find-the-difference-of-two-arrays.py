class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Create a dictionary which holds all the nums1 and nums2 with key as their array name and vaulue as value
        # Find the duplicate value and remove it
        # return the arrays with new values 

        #### You were thinking it wrong you need to convert them to sets to remove any dups

        ###----------------------------------------####
        ###--------Patter == compare two lists------###

        set1 = set(nums1)
        set2 = set(nums2)

        only_in_1 = list(set1-set2)
        only_in_2 = list(set2-set1)

        return [only_in_1, only_in_2]
        
        
