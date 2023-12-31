// 1472. Design Browser History
class Node {
public:
    string data;
    Node* next;
    Node* prev;
    Node ()          : next(NULL), prev(NULL) {}
    Node (string val): data(val), next(NULL), prev(NULL) {}
};

class BrowserHistory {
public:
    Node* cur = new Node();

    BrowserHistory(string homepage) {
        cur = new Node(homepage);
    }
    
    void visit(string url) {
        Node* newNode = new Node(url);
        cur->next = newNode;
        newNode->prev = cur;
        cur = cur->next;
    }
    
    string back(int steps) {
        while (cur->prev && steps > 0)
        {
            cur = cur->prev;
            steps -= 1;
        }
        return cur->data;
    }
    
    string forward(int steps) {
        while (cur->next && steps > 0)
        {
            cur = cur->next;
            steps -= 1;
        }
        return cur->data;
    }
};
