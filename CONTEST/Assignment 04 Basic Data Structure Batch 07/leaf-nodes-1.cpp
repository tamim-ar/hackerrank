#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long val;
    Node *left, *right;
    Node(long long v) : val(v), left(NULL), right(NULL) {}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> arr;
    long long x;
    while (cin >> x) arr.push_back(x);
    if (arr.empty() || arr[0] == -1) return 0;

    Node* root = new Node(arr[0]);
    queue<Node*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < arr.size()) {
        Node* cur = q.front();
        q.pop();

        if (i < arr.size() && arr[i] != -1) {
            cur->left = new Node(arr[i]);
            q.push(cur->left);
        }
        i++;

        if (i < arr.size() && arr[i] != -1) {
            cur->right = new Node(arr[i]);
            q.push(cur->right);
        }
        i++;
    }

    vector<long long> leaves;
    queue<Node*> bfs;
    bfs.push(root);
    while (!bfs.empty()) {
        Node* node = bfs.front();
        bfs.pop();

        if (!node->left && !node->right) {
            leaves.push_back(node->val);
        }
        if (node->left) bfs.push(node->left);
        if (node->right) bfs.push(node->right);
    }

    sort(leaves.rbegin(), leaves.rend());
    for (int j = 0; j < leaves.size(); j++) {
        cout << leaves[j];
        if (j + 1 < leaves.size()) cout << " ";
    }
    cout << "\n";

    return 0;
}
