#include<iostream>
#include <queue>
using namespace std;

struct node {
        int data;
        node* left;
        node* right;
};

class BST {
private:
    node* root;
public:
    BST() {
        root = NULL;
    }

    ~BST() {
        root = makeEmpty(root);
    }

    node* makeEmpty(node* t) {
        if(t == NULL)
            return NULL;
        {
            makeEmpty(t->left);
            makeEmpty(t->right);
            delete t;
        }
        return NULL;
    }
    node* insert(int x, node* t)
    {
        if(t == NULL)
        {
            t = new node;
            t->data = x;
            t->left = t->right = NULL;
        }
        else if(x < t->data)
            t->left = insert(x, t->left);
        else if(x > t->data)
            t->right = insert(x, t->right);
        return t;
    }

    void inor(node* t) {
        if(t == NULL)
            return;
        inor(t->left);
        cout << t->data << " ";
        inor(t->right);
    }

    bool find(node* t, int x) {
        if(t == NULL)
            return 0;
        else if(x < t->data)
            return find(t->left, x);
        else if(x > t->data)
            return find(t->right, x);
        else
            if (x == t->data) return 1;
		else return 0;
    }

	void show_level(node *root) {
		queue <node*> A;
		A.push(root);
		while (!A.empty()){
			node* tmp=A.front();
			A.pop();
			cout<<tmp->data<< " ";
			if (tmp->left) A.push(tmp->left);
			if (tmp-> right) A.push(tmp->right);
		}
	}

    void insert(int x) {
        root = insert(x, root);
    }

    void display() {
        inor(root);
        cout << endl;
    }

    bool search(int x) {
        find(root, x);
    }

	void show_level(){
		show_level(root);
		cout<< endl;
	}
};

int main() {
    BST t;
    t.insert(20);
    t.insert(25);
    t.insert(15);
    t.insert(10);
    t.insert(30);
    if (t.search(20)) t.insert(32);
	t.display();
	t.show_level();
    return 0;
}
