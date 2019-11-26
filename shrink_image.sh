cd ./calligraphy/
for f in `ls -1 *.jpg`
do
    if [ -f "../shrink_calligraphy/$f" ]; then 
	echo "file ../shrink_calligraphy/$f exists"
    else
	echo "convert -resize 10%  $f ../shrink_calligraphy/$f"
	convert -resize 10%  $f ../shrink_calligraphy/$f
    fi
done
