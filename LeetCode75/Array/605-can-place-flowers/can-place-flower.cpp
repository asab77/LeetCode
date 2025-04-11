class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0;
        int length = flowerbed.size();

        while (i < length) {
            if (flowerbed[i] == 0 &&
                (i == 0 || flowerbed[i - 1] == 0) &&
                (i == length - 1 || flowerbed[i + 1] == 0)) {
                
                flowerbed[i] = 1;
                n--;
                i += 2;
            } else {
                i++;
            }
        }

        return n <= 0;
    }
};
