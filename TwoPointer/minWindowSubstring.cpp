class Solution { //TC->O(m+m(or)n) but a little less than m SC->O(128)
public:
    string minWindow(string s, string t) {
        if(s.size()==0 || t.size()==0)
            return "";
        vector<int> char_count(128,0);
        for(auto i:t){
            char_count[i]++;
        }
        int i=0,j=0,min=INT_MAX,start = 0,required = t.size(); // we need start for starting from where the minimum window start and required for tracking the characters that we are in need of
        while(i<=s.size() && j<=s.size()){ // two pointer i and j start of the window and end of the window
            if(required){
                if(i==s.size())
                    break; //finish the process we can to send of the string we cannot generate stil more windows
                char_count[s[i]]--;
                if(char_count[s[i]]>=0)
                    required--;   //this means that the character we are searching for can so we are decrementing
                i++; //go to next character
            }
            else{
                if(i-j < min){
                    min = i-j;
                    start = j;
                }
                char_count[s[j]]++;
                if(char_count[s[j]]>0)
                    required++;   //we are doing this because we may get the target character in the future so make required++ so we can search for other characters of t in s
                j++; // moving the window start to next so that the window will shrink
            }
        }
        return min==INT_MAX?"":s.substr(start,min); //substr(startpositin,how many characters)
    }
};
