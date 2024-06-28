#include <stdio.h>
#include <stdlib.h>

#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))
#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define CLAMP(V, MIN_V, MAX_V) MIN(MAX(V, MIN_V), MAX_V)

int compare(const void *a, const void *b) {
    double *a_row = (double *)a;
    double *b_row = (double *)b;

    return b_row[3] - a_row[3];
}

double evaluate_quadratic(double x, double *row) {
    return x * x * row[0] + x * row[1] + row[2];
}

int main() {
    int n, i, j;
    double values[100000][4], r;

    scanf("%d",&n);

    for (i = 0; i < n; i++) {
        scanf("%lf %lf %lf %lf", values[i], values[i] + 1, values[i] + 2, values[i] + 3);
    }

    qsort(values, n, 4 * sizeof(double), compare);

    for (i = 1; i < n; i++) {
        for (j = 0; j < 3; j++) {
            values[i][j] += values[i - 1][j];
        }
    }

    r = 0;
    for (i = 0; i < n; i++) {
        r = MAX(
            r,
            MAX(
                values[i][2],
                MAX(
                    evaluate_quadratic(CLAMP(-values[i][1]/(2*values[i][0]+0.001), 0, values[i][3]), values[i]),
                    evaluate_quadratic(values[i][3], values[i])
                )
            )
        );
    }

    printf("%lf\n", r);

    return 0;
}