./SMILExtract -C config/IS13_ComParE.conf -I $1 -O trial_output_temp
tail -1 trial_output_temp
rm trial_output_temp

