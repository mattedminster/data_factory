#! /bin/bash
cut -d ' ' -f 2- lexicon.txt |  sed 's/ /\n/g' | sort -u > nonsilence_phones.txt