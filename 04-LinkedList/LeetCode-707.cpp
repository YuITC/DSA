// 707. Design Linked List
class Node
{
public:
    int val;
    Node* next;
    Node* prev;
    Node(int data)  : val(data), next(NULL), prev(NULL) {}
};

class MyLinkedList {
public:
    Node* head;
    Node* tail;

    MyLinkedList() {
        head = new Node(-1);
        tail = new Node(-1);

        head->next = tail;
        tail->prev = head;
    }
    
    int get(int index) {
        Node* ptr = head->next;
        int i = 0;
        while (i < index && ptr)
        {
            ptr = ptr->next;
            i ++;
        }

        if (ptr && ptr != tail && i == index)
            return ptr->val;
        return -1; 
    }
    
    void addAtHead(int val) {
        Node* newNode = new Node(val);

        newNode->prev = head;
        newNode->next = head->next;

        head->next->prev = newNode;
        head->next = newNode;
    }
    
    void addAtTail(int val) {
        Node* newNode = new Node(val);

        newNode->next = tail;
        newNode->prev = tail->prev;

        tail->prev->next = newNode;
        tail->prev = newNode;
    }
    
    void addAtIndex(int index, int val) {
        Node* ptr = head->next;
        int i = 0;
        while (i < index && ptr)
        {
            ptr = ptr->next;
            i ++;
        }

        Node* newNode = new Node(val);
        if (ptr && i == index)
        {
            newNode->next = ptr;
            newNode->prev = ptr->prev;

            ptr->prev->next = newNode;
            ptr->prev = newNode;            
        }
    }
    
    void deleteAtIndex(int index) {
        Node* ptr = head->next;
        int i = 0;
        while (i < index && ptr)
        {
            ptr = ptr->next;
            i ++;
        }

        if (ptr && ptr != tail && i == index )
        {
            ptr->prev->next = ptr->next;
            ptr->next->prev = ptr->prev;              
        }
      
    }
};
