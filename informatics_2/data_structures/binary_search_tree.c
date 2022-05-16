#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *left, *right;
};
typedef struct node node;

void inorder(node *root) {
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    printf("%d ", root->value);
    inorder(root->right);
}

void preorder(node *root) {
    if (root == NULL) {
        return;
    }
    printf("%d ", root->value);
    preorder(root->left);
    preorder(root->right);
}

void postorder(node *root) {
    if (root == NULL) {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->value);
}

node *create_node(int value) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->value = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

node *insert_node(int value, node *root) {
    if (root == NULL) {
        return create_node(value);
    }
    if (value < root->value) {
        root->left = insert_node(value, root->left);
    } else if (value > root->value) {
        root->right = insert_node(value, root->right);
    }
    return root;
}

// helper for delete_node
node *min_node(node *root) {
    if (root == NULL) {
        return NULL;
    }
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

node *delete_node(int value, node *root) {
    if (root == NULL) {
        return NULL;
    }
    if (value < root->value) {
        root->left = delete_node(value, root->left);
    } else if (value > root->value) {
        root->right = delete_node(value, root->right);
    } else {
        // node has ONE child
        if (root->left == NULL) {
            node *temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            node *temp = root->left;
            free(root);
            return temp;
        }
        // node has TWO children
        node *temp = min_node(root);
        root->value = temp->value;
        root->right = delete_node(temp->value, root->right);
    }
    return root;
}

node *search_node(int value, node *root) {
    if (root == NULL) {
        return NULL;
    }
    if (value == root->value) {
        return root;
    } else if (value < root->value) {
        return search_node(value, root->left);
    } else {
        return search_node(value, root->right);
    }
}

int main() {
    node *root = NULL;
    for (int i = 0; i < 10; i++) {
        root = insert_node(i, root);
    }

    delete_node(8, root);
    inorder(root);
    printf("\n");
    insert_node(8, root);
    inorder(root);
    printf("\n");

    return 0;
}
