# !/bin/bash

cd ~ 
currentDay=$(date +"%m_%d_%Y")
files=`find . -type f -mtime -1 -not -wholename "./backup*"`
fname="./backup/${currentDay}_backup.tar.gz"
if [ -f $fname ]
then
 gunzip $fname 
 out=`tar -uvf ${fname%%.gz} $files `
 gzip ${fname%%.gz}
else
 out=`tar -cvzf $fname $files `
fi

echo >> ~/backup/change.log
echo "------------- $(date) -------------" >> ~/backup/change.log
echo >> ~/backup/change.log
 
result=`echo $out | tr ' ' '\n'`
echo "$result" >> ~/backup/change.log
