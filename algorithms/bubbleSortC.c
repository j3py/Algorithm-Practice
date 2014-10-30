#include <stdio.h>

int main(void) {
	int d[] = {1, 31, 432, 12, 543, 3};
	int size = 6;
	int i, j;
	int bin;

	for (i = 0; i < size; i++) {
		for (j = 0; j < (size-1); j++) {
			if (d[j] < d[j+1]) {
				bin = d[j];
				d[j] = d[j+1];
				d[j+1] = bin;
			}
		}
	}

	for (i = 0; i < size; i++) {
		printf("%d\n", d[i]);
	}

	return 0;

}