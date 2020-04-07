/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
*/

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> valueMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            //Verify whether the map contains the complement number to reach the target.
            if (valueMap.containsKey(target - nums[i])) {
                result[0] = valueMap.get(target - nums[i]);
                result[1] = i;
                return result;
            }
            valueMap.put(nums[i], i);
        }
        throw new IllegalArgumentException("No match pair found to reach target of " + target);
    }
}

