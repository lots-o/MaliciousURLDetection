wget --no-check-certificate https://www.isi.csic.es/dataset/normalTrafficTraining.rar
wget --no-check-certificate https://www.isi.csic.es/dataset/normalTrafficTest.rar
wget --no-check-certificate https://www.isi.csic.es/dataset/anomalousTrafficTest.rar


unrar e normalTrafficTraining.rar 
unrar e normalTrafficTest.rar 
unrar e anomalousTrafficTest.rar 

mkdir data/

mv normalTrafficTraining.txt ./data
mv normalTrafficTest.txt ./data
mv anomalousTrafficTest.txt ./data 

rm normalTrafficTraining.rar
rm normalTrafficTest.rar
rm anomalousTrafficTest.rar 

