#! /bin/bash
utils/prepare_lang.sh data/local/lang 'OOV' data/local/ data/lang
                    
# where the underlying argument structure is:
utils/prepare_lang.sh <dict-src-dir> <oov-dict-entry> <tmp-dir> <lang-dir>