#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Part one: 218

enum ReportState { SAFE, UNSAFE };
enum NumbersDirection { UNDECIDED = -1, NEGATIVE, POSITIVE };

void calculateDistances(int* numbers, int* distances, size_t amountNumbers) {
	for (int i=0; i < amountNumbers - 1; i++) {
		*distances = *numbers - *(numbers + 1);
		distances++;
		numbers++;
	}
}

enum ReportState validateStateWithDampener(int* numbers, size_t amountNumbers) {
	enum NumbersDirection direction = UNDECIDED;
	int strike = 0;

	for (int i=0; i < amountNumbers - 1; i++) {
		int distanceToNext = *numbers - *(numbers + 1);
		if (distanceToNext > 0 && distanceToNext <= 3 && (direction == UNDECIDED || direction == POSITIVE)) {
			direction = POSITIVE;
		} else if (distanceToNext < 0 && distanceToNext >= -3 && (direction == UNDECIDED || direction == NEGATIVE)) {
			direction = NEGATIVE;
		} else {
			if (strike == 0) {
				strike++;
				distanceToNext = *numbers - *(numbers + 2);
				if (distanceToNext > 0 && distanceToNext <= 3 && (direction == UNDECIDED || direction == POSITIVE)) {
					direction = POSITIVE;
				} else if (distanceToNext < 0 && distanceToNext >= -3 && (direction == UNDECIDED || direction == NEGATIVE)) {
					direction = NEGATIVE;
				}
				strike = 1;
				numbers++;
				continue;
			}

			return UNSAFE;
		}

		numbers++;
	}

	return SAFE;
}

enum ReportState validateState(int* numbers, size_t amountNumbers) {
	// -1 because the last number does not have any distance to another number
	int* distances = malloc((amountNumbers - 1) * sizeof(int));
	if (distances == NULL) {
		perror("Could not allocate memory for distances");
		return -1;
	}

	calculateDistances(numbers, distances, amountNumbers);
	int* pDistances = distances;
	enum NumbersDirection direction = UNDECIDED;

	for (int i=0; i < amountNumbers - 1; i++) {
		if (*pDistances > 0 && *pDistances <= 3 && (direction == UNDECIDED || direction == POSITIVE)) {
			direction = POSITIVE;
		} else if (*pDistances < 0 && *pDistances >= -3 && (direction == UNDECIDED || direction == NEGATIVE)) {
			direction = NEGATIVE;
		} else {
			free(distances);
			return UNSAFE;
		}

		pDistances++;
	}

	return SAFE;
}

int main() {
	FILE* puzzle;
	int amountSafePartOne = 0;
	int amountSafePartTwo = 0;

	puzzle = fopen("puzzle_input.txt", "r");
	if (puzzle == NULL) {
		perror("Could not open puzzle");
		return 1;
	}

	char* buf = NULL;
	size_t read_len = 0;
	size_t buf_len = 0;

	char* bufPosition;
	char* numberStr;
	while ((buf_len = getline(&buf, &read_len, puzzle)) != -1) {
		int amountNumbers = 0;

    char* bufCopy = strdup(buf);
    if (bufCopy == NULL) {
      perror("Could not allocate memory for buffer copy");
      free(buf);
      fclose(puzzle);
      return 1;
    }

    bufPosition = bufCopy;
    while ((numberStr = strsep(&bufPosition, " ")) != NULL) {
      if (*numberStr != '\0')
        amountNumbers++;
    }

		int* numbers = malloc(amountNumbers * sizeof(int));
		if (numbers == NULL) {
			perror("Could not allocate memory for numbers");
			return 1;
		}

		int* pNumbers = numbers;
		bufPosition = buf;
		while ((numberStr = strsep(&bufPosition, " ")) != NULL) {
			if (*numberStr != '\0') {
				*pNumbers = atoi(numberStr);
				pNumbers++;
			}
		}

		enum ReportState state = validateState(numbers, amountNumbers);
		switch (state) {
			case SAFE:
				amountSafePartOne++;
				break;
			case UNSAFE:
				break;
		}

		state = validateStateWithDampener(numbers, amountNumbers);
		switch (state) {
			case SAFE:
				amountSafePartTwo++;
				break;
			case UNSAFE:
				break;
		}

		free(numbers);
	}

	free(buf);

	printf("Part One - %d report(s) are safe\n", amountSafePartOne);
	printf("Part Two - %d report(s) are safe\n", amountSafePartTwo);

	return 0;
}
