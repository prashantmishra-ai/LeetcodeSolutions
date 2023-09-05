/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
Node* copyRandomList(Node* head) {
    if (!head) return nullptr;

    // Step 1: Duplicate each node in the original list and interleave them
    Node* curr = head;
    while (curr) {
        Node* tmp = new Node(curr->val);
        tmp->next = curr->next;
        curr->next = tmp;
        curr = tmp->next;
    }

    // Step 2: Fix the random pointers for the duplicated nodes
    curr = head;
    while (curr) {
        if (curr->random) {
            curr->next->random = curr->random->next;
        }
        curr = curr->next->next;
    }

    // Step 3: Separate the original list from its duplicated counterpart
    curr = head;
    Node* newHead = curr->next;
    Node* newCurr = newHead;
    while (curr) {
        curr->next = curr->next->next;
        if (newCurr->next) newCurr->next = newCurr->next->next;
        curr = curr->next;
        newCurr = newCurr->next;
    }

    return newHead;
}
};