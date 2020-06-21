#! /bin/bash
mfccdir=mfcc  
x=data/train  
steps/make_mfcc.sh --cmd "$train_cmd" --nj 16 $x exp/make_mfcc/$x $mfccdir  
steps/compute_cmvn_stats.sh $x exp/make_mfcc/$x $mfccdir