#!/usr/bin/env bash

mul_re='mul\(([0-9]{1,3}),([0-9]{1,3})\)$'
do_re='do\(\)'
dont_re="don't\(\)"
s="$(< /dev/stdin)"
s=${s//\)/\)$'\n'}

activated=true

declare -i sum
while read -r line; do
  if [[ $line =~ $do_re ]]; then
    activated=true
  elif [[ $line =~ $dont_re ]]; then
    activated=false
  fi

  if [[ $line =~ $mul_re ]] && $activated; then
    sum+=$((BASH_REMATCH[1] * BASH_REMATCH[2]))
  fi
done <<< "$s"

echo "Part one: ${sum}"
