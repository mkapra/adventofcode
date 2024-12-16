#!/usr/bin/env bash

mul_re='mul\(([0-9]{1,3}),([0-9]{1,3})\)'
s="$(< /dev/stdin)"

declare -i sum
while [[ $s =~ $mul_re ]]; do
  sum+=$((BASH_REMATCH[1] * BASH_REMATCH[2]))
  s=${s/"${BASH_REMATCH[0]}"/}
done

echo "Part one: ${sum}"
