#include <stdio.h>
#include <stdlib.h>

// Vector node definition matching your library's 'sadish' (and Problem 62's 'LIST')
typedef struct sadish {
    double data;
    struct sadish *next;
} sadish;

// Helper function to create a new vector node
sadish *createNode(double val) {
    sadish *node = (sadish *)malloc(sizeof(sadish));
    node->data = val;
    node->next = NULL;
    return node;
}

// Function to load values from a .dat file into a vector list
sadish *load_vector(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        printf("Error: Could not open file %s\n", filename);
        return NULL;
    }

    sadish *head = NULL;
    sadish *tail = NULL;
    double val;

    while (fscanf(fp, "%lf", &val) == 1) {
        sadish *newNode = createNode(val);
        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    fclose(fp);
    return head;
}

// Function to print a vector linked list
void print_vector(const char *name, sadish *list) {
    printf("%s: ", name);
    sadish *curr = list;
    while (curr != NULL) {
        printf("%.0lf", curr->data);
        if (curr->next != NULL) {
            printf(" -> ");
        }
        curr = curr->next;
    }
    printf(" -> NULL\n");
}

// Search function given in Problem 62
int find(double query, sadish *list) {
    while (list != NULL) {
        if (list->data == query) {
            return 1;
        }
        list = list->next;
    }
    return 0;
}

int main() {
    // 1. Load the two vector lists from .dat files
    sadish *L1 = load_vector("l1.dat");
    sadish *L2 = load_vector("l2.dat");

    if (!L1 || !L2) {
        printf("Failed to load vectors.\n");
        return 1;
    }

    // 2. Print initial vectors
    printf("--- Initial Vector Lists Loaded from .dat Files ---\n");
    print_vector("L1", L1);
    print_vector("L2", L2);

    // 3. Problem 62 Segment: Delete elements in L1 that exist in L2 (skipping head)
    sadish *ptr1 = L1;
    while (ptr1->next != NULL) {
        double query = ptr1->next->data;
        if (find(query, L2)) {
            sadish *temp = ptr1->next;
            ptr1->next = ptr1->next->next;
            free(temp); // Free deleted node
        } else {
            ptr1 = ptr1->next;
        }
    }

    // 4. Print modified L1 and remaining node count
    printf("\n--- After Execution of Problem 62 Code ---\n");
    print_vector("L1 (modified)", L1);

    int count = 0;
    for (sadish *curr = L1; curr != NULL; curr = curr->next) {
        count++;
    }
    printf("\nNumber of nodes remaining in L1: %d\n", count);

    return 0;
}

