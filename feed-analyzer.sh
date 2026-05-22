#!/bin/bash

awk '/^[0-9]/ {printf("\n%s",$0)} {printf(" %s", $0)}' "$1" | cut -d',' -f2 | tail -n +2 | sort | uniq -c | sort -rn | head -5 |awk '{print($2)}'
