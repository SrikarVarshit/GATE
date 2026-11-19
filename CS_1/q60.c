#include <stdio.h>

int main(void) {
    int q0, q1, q2, q3;

    printf("Enter initial state (Q0 Q1 Q2 Q3): ");
    if (scanf("%d %d %d %d", &q0, &q1, &q2, &q3) != 4) {
        return 1;
    }

    int init_q0 = q0, init_q1 = q1, init_q2 = q2, init_q3 = q3;
    int count = 0;

    printf("\n| Step | Present State |  FF Inputs   |  Next State  |\n");
    printf("|------|---------------|--------------|--------------|\n");
    printf("|      | Q0 Q1 Q2 Q3   | D0 D1 D2 D3  | Q0 Q1 Q2 Q3  |\n");
    printf("|------|---------------|--------------|--------------|\n");

    do {
        /* Johnson counter excitation equations */
        int d0 = !q3;
        int d1 = q0;
        int d2 = q1;
        int d3 = q2;

        /* Next state evaluation */
        int next_q0 = d0;
        int next_q1 = d1;
        int next_q2 = d2;
        int next_q3 = d3;

        printf("| %-4d |   %d  %d  %d  %d   |  %d  %d  %d  %d   |   %d  %d  %d  %d   |\n",
               count + 1, q0, q1, q2, q3, d0, d1, d2, d3, next_q0, next_q1, next_q2, next_q3);

        q0 = next_q0;
        q1 = next_q1;
        q2 = next_q2;
        q3 = next_q3;
        count++;
    } while (!(q0 == init_q0 && q1 == init_q1 && q2 == init_q2 && q3 == init_q3));

    printf("------------------------------------------------------\n");
    printf("Total distinct states: %d\n", count);

    return 0;
}

