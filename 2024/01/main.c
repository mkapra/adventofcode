#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <data_structures/linked_list.h>

int countOccurences(struct Node* head, int data) {
  struct Node* cur = searchNode(head, data);
  if (cur == NULL)
    return 0;

  int count = 0;
  while (cur != NULL && (cur = searchNode(cur, data)) != NULL) {
    count++;
    if (cur->data > data)
      return count;
    cur = cur->next;
  }

  return count;
}

int main() {
  FILE* puzzle;
  int err;

  struct Node* lHead = NULL;
  struct Node* rHead = NULL;

  puzzle = fopen("puzzle.txt", "r");
  if (puzzle == NULL) {
    perror("Could not open puzzle");
    return 1;
  }

  char buf[32];
  while (fgets(buf, sizeof(buf), puzzle) != NULL) {
    char* lSpace = strchr(buf, ' ');
    size_t firstNumberLen = (lSpace - buf + 1);

    char* leftNumberStr = malloc(firstNumberLen + 1);
    strlcpy(leftNumberStr, buf, firstNumberLen);

    int l = atoi(leftNumberStr);
    addNode(&lHead, l);
    free(leftNumberStr);

    int r = atoi(&buf[firstNumberLen] + 2);
    addNode(&rHead, r);
  }

  fclose(puzzle);

  int sumPartOne = 0;
  int sumPartTwo = 0;
  struct Node* l = lHead;
  struct Node* r = rHead;
  while (l != NULL || r != NULL) {
    sumPartOne += abs(l->data - r->data);
    sumPartTwo += l->data * countOccurences(rHead, l->data);

    l = l->next;
    r = r->next;
  }

  printf("Part one: %d\n", sumPartOne);
  printf("Part two: %d\n", sumPartTwo);

  // Cleanup
  freeList(&lHead);
  freeList(&rHead);

  return 0;
}
