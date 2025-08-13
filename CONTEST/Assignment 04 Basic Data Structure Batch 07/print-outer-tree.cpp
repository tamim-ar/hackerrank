
#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node *left;
    Node *right;
    Node(int val)
    {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node *input_tree()
{
    int val;
    cin >> val;
    Node *root;
    if (val == -1)
        root = NULL;
    else
        root = new Node(val);
    queue<Node *> q;
    if (root)
        q.push(root);
    while (!q.empty())
    {

        Node *p = q.front();
        q.pop();

        int l, r;
        cin >> l >> r;
        Node *myLeft, *myRight;
        if (l == -1)
            myLeft = NULL;
        else
            myLeft = new Node(l);
        if (r == -1)
            myRight = NULL;
        else
            myRight = new Node(r);

        p->left = myLeft;
        p->right = myRight;

        if (p->left)
            q.push(p->left);
        if (p->right)
            q.push(p->right);
    }
    return root;
}

// void LeftSideprint(Node *root)
// {
//     // if (root == NULL)
//     //     return;
//     if (root->left)
//     {
//         LeftSideprint(root->left);
//         cout << root->val << " ";
//         if (root->left == NULL && root->right)
//             LeftSideprint(root->right);
//         cout << root->val << " ";
//     }
// }
void LeftSideprint(Node *root)
{
    if (root == NULL)
        return;
    LeftSideprint(root->left);
    if (!root->left && root->right)
        LeftSideprint(root->right);
    cout << root->val << " ";
}
// void RightSideprint(Node *root)
// {
//     // if (root == NULL)
//     //     return;
//     if (root->right)
//     {
//         cout << root->right->val << " ";
//         RightSideprint(root->right);

//         if (root->right == NULL && root->left)
//             RightSideprint(root->left);
//     }
// }
void RightSideprint(Node *root)
{
    if (root == NULL)
        return;
    cout << root->val << " ";
    RightSideprint(root->right);
    if (!root->right  && root->left)
        RightSideprint(root->left);
}

int main()
{
    Node *root = input_tree();

    LeftSideprint(root->left);
    cout << root->val << " ";
    RightSideprint(root->right);

    return 0;
}