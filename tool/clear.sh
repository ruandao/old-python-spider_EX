rm spider.log
rm spider.sqlite
rm *.pyc
cp debugfile.log backup/debug-`date +"%m-%d-%H-%M"`.log
rm debugfile.log
