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
    if (arr.size() < 2) return 0;

    long long level = arr.back();
    arr.pop_back();

    if (arr.empty() || arr[0] == -1) {
        cout << "Invalid\n";
        return 0;
    }

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

    queue<pair<Node*, int>> bfs;
    bfs.push({root, 0});
    vector<long long> result;

    while (!bfs.empty()) {
        auto [node, depth] = bfs.front();
        bfs.pop();

        if (depth == level) {
            result.push_back(node->val);
        }
        if (node->left) bfs.push({node->left, depth + 1});
        if (node->right) bfs.push({node->right, depth + 1});
    }

    if (result.empty()) {
        cout << "Invalid\n";
    } else {
        for (int j = 0; j < result.size(); j++) {
            cout << result[j];
            if (j + 1 < result.size()) cout << " ";
        }
        cout << "\n";
    }

    return 0;
}
