#! /bin/bash
 cut -d ' ' -f 2- text | sed 's/ /\n/g' | sort -u > words.txt