class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();

        unordered_map<int , int> freq;
        for(int x:nums){
            freq[x]++;

        }
        for(int i = 0;i<n;i++){
            if(freq[nums[i]] > 1) return true;
        }
        return false;

        
    }
};