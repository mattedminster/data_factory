#! /bin/bash
mfccdir=mfcc  
x=data/train  
steps/make_mfcc.sh --cmd "run.pl" --nj ${params.num_of_jobs} $x exp/make_mfcc/$x $mfccdir  
steps/compute_cmvn_stats.sh $x exp/make_mfcc/$x $mfccdir