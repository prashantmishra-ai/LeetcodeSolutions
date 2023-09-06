/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int length = 0;
    ListNode* curr = root;
    while (curr) {
        length++;
        curr = curr->next;
    }

    int width = length / k, extra = length % k;

    vector<ListNode*> result;
    curr = root;
    for (int i = 0; i < k; i++) {
        ListNode* head = curr;
        for (int j = 0; j < width + (i < extra ? 1 : 0) - 1; j++) {
            if (curr) curr = curr->next;
        }
        if (curr) {
            ListNode* tmp = curr;
            curr = curr->next;
            tmp->next = nullptr;
        }
        result.push_back(head);
    }
    return result;
    }
};