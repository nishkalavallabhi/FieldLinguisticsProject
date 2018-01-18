for file in `ls $1`;
do
  echo $1$file
  mpg123 -w $1$file".wav" $1$file
done


