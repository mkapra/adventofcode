#include <iostream>
#include <vector>

int main(int argc, char const* argv[])
{
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("../../numbers.txt", "r");
	if (fp == NULL) {
		perror("Unable to open file!");
		exit(1);
	}

	// Save all numbers in a list
	std::vector<int> numbers;
	while ((read = getline(&line, &len, fp)) != -1) {
		numbers.push_back(atoi(line));
	}

	// Loop over numbers
	for (auto number : numbers) {
		for (auto number2 : numbers) {
			if ((number + number2) == 2020) {
				std::cout << "Result: " << number * number2 << '\n';
				return 0;
			}
		}
	}

	return 0;
}
