#include <stdio.h>
#include <stdlib.h>

// Vector node definition
typedef struct sadish {
    double data;
    struct sadish *next;
} sadish;

// Matrix node definition (linked list of vectors/rows)
typedef struct avyuh {
    struct sadish *vector;
    struct avyuh *next;
} avyuh;

// Helper: allocate a single vector element
sadish *createNode(double val) {
    sadish *node = (sadish *)malloc(sizeof(sadish));
    node->data = val;
    node->next = NULL;
    return node;
}

// Function to read a vector (sadish) from a .dat file
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

// Helper: display an entire avyuh matrix row by row
void printMat(avyuh *mat) {
    int row_idx = 1;
    for (avyuh *row = mat; row != NULL; row = row->next) {
        printf("Row L%d: [ ", row_idx++);
        for (sadish *curr = row->vector; curr != NULL; curr = curr->next) {
            printf("%.0lf ", curr->data);
        }
        printf("]\n");
    }
}

// Search function from Problem 62
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
    // 1. Load the two vector lists from the .dat files
    sadish *l1 = load_vector("l1.dat");
    sadish *l2 = load_vector("l2.dat");

    if (!l1 || !l2) {
        printf("Failed to load vectors from files.\n");
        return 1;
    }

    // 2. Package L1 and L2 into an avyuh matrix (Row 1 = L1, Row 2 = L2)
    avyuh *A = (avyuh *)malloc(sizeof(avyuh));
    A->vector = l1;

    A->next = (avyuh *)malloc(sizeof(avyuh));
    A->next->vector = l2;
    A->next->next = NULL;

    // 3. Print the avyuh matrix before modification
    printf("--- Initial Avyuh Matrix (L1 & L2) ---\n");
    printMat(A);

    // 4. Access L1 and L2 directly through the avyuh structure
    sadish *ptr1 = A->vector;       // Row 1 (L1)
    sadish *L2   = A->next->vector; // Row 2 (L2)

    // Execute Problem 62 removal algorithm on L1 using L2
    while (ptr1->next != NULL) {
        double query = ptr1->next->data;
        if (find(query, L2)) {
            sadish *temp = ptr1->next;
            ptr1->next = ptr1->next->next;
            free(temp);
        } else {
            ptr1 = ptr1->next;
        }
    }

    // 5. Print the updated avyuh matrix
    printf("\n--- Modified Avyuh Matrix ---\n");
    printMat(A);

    // 6. Count remaining elements in Row 1 (L1)
    int count = 0;
    for (sadish *curr = A->vector; curr != NULL; curr = curr->next) {
        count++;
    }
    printf("\nNumber of nodes remaining in L1: %d\n", count);

    return 0;
}

