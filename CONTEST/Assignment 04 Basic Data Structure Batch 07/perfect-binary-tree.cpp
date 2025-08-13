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
    if (arr.empty() || arr[0] == -1) {
        cout << "NO\n";
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

    // Check if perfect
    queue<pair<Node*, int>> bfs;
    bfs.push({root, 0});
    int maxDepth = 0;
    vector<int> leafDepths;
    int nodeCount = 0;

    while (!bfs.empty()) {
        auto [node, depth] = bfs.front();
        bfs.pop();
        nodeCount++;
        maxDepth = max(maxDepth, depth);

        if (!node->left && !node->right) {
            leafDepths.push_back(depth);
        } else {
            if (!node->left || !node->right) {
                cout << "NO\n";
                return 0;
            }
            bfs.push({node->left, depth + 1});
            bfs.push({node->right, depth + 1});
        }
    }

    if (all_of(leafDepths.begin(), leafDepths.end(), [&](int d) { return d == maxDepth; }) &&
        nodeCount == (pow(2, maxDepth + 1) - 1)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
