#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack <int> s1, s2;
      string str1, str2;
      for (int i=0; i<s.length(); i++){
        if (s[i] == '#' && !s1.empty()){
          s1.pop();
        }else if (s[i]!='#'){
          s1.push(s[i]);
        }
      }
      for (int i=0; i<t.length(); i++){
        if (t[i] == '#' && !s2.empty()){
          s2.pop();
        }else if (t[i]!='#'){
          s2.push(t[i]);
        }
      }
      while (!s1.empty()){
          str1 += s1.top();
          s1.pop();
      }
      while (!s2.empty()){
          str2 += s2.top();
          s2.pop();
      }
      if (str1 == str2){
        return true;
      }else{
        return false;
      }
    }
};

int main(){
  Solution s;
  string s1, s2;
  cin >> s1 >> s2;
  cout << s.backspaceCompare(s1, s2);
  return 0;
}