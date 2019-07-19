#include <stdio.h>
#include <string.h>

#include <cassert>
#include <vector>
#include <tuple>

typedef std::tuple<char *, const char *, int> TestCase;

class Solution {
public:
	void replaceSpace(char *str,int length) {
        if (!str || length <= 0)
            return ;

        int oldCount = 0; // origin count
        int replaceCount = 0; // count to be added
        
        char *p = str;
        while (*p != '\0')
        {
            oldCount++;
            if (*p == ' ')
                replaceCount++;
            p++;
        }
        int newCount = oldCount + replaceCount * 2;
        if (newCount > length)
            return ;
        
        int pOldCount = oldCount;
        int pNewCount = newCount;
        
        while (pOldCount >= 0 && pNewCount > pOldCount)
        {
            if (str[pOldCount] == ' ')
            {
                str[pNewCount--] = '0';
                str[pNewCount--] = '2';
                str[pNewCount--] = '%';
            }
            else
            {
                str[pNewCount--] = str[pOldCount];
            }
            pOldCount--;
        }
	}
};

void assertTest(char *in, const char *out, int length)
{
    Solution().replaceSpace(in, length);
    printf("%s\n", in);
    assert(strcmp(in, out) == 0);
}

int main(int argc, const char *argv[])
{
    char in[100] = "hello world";
    char out[] = "hello%20world";
    assertTest(in, out, 100);

    Solution().replaceSpace(nullptr, 0);

    char in1[] = "";
    char in2[10] = "  ";
    char in3[4] = "b c";
    char in4[10] = "b c";
    char in5[10] = " abc";
    char in6[10] = "abc ";
    char in7[11] = "a  bc";

    std::vector<TestCase> testCaseVec{
        {in1, "", 0}, // empty string
        {in2, "\%20\%20", 10}, // string only contains space
        {in3, "b c", 4}, // string with space but not enough string length
        {in4, "b\%20c", 10}, // space in the string 
        {in5, "\%20abc", 10}, // space at begining
        {in6, "abc\%20", 10}, // space at ending
        {in7, "a\%20\%20bc", 10} // spaces in the middle 
    };


    for (auto testCase : testCaseVec)
        assertTest(std::get<0>(testCase), std::get<1>(testCase), std::get<2>(testCase));
    return 0;
}

