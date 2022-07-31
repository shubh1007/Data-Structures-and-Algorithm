#include<bits/stdc++.h> 
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;

    Node(int val)
    {
        data = val;
        left = NULL;
        right = NULL;
    }
};

int findHeightOftree(Node* root)
{
   if(root == NULL)
   {
       return -1;
   }

   int left_height = findHeightOftree(root->left);
   int right_height = findHeightOftree(root->right);

   return max(left_height,right_height)+1;
}


int main()
{
    // cout<<"Hello World\n";
    Node* root = new Node(1);
    root->right = new Node(2);
    root->left = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    /*
    */   
    cout<<findHeightOftree(root);    
    return 0;
}