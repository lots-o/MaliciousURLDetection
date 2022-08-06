wget --no-check-certificate https://www.isi.csic.es/dataset/normalTrafficTraining.rar
wget --no-check-certificate https://www.isi.csic.es/dataset/normalTrafficTest.rar
wget --no-check-certificate https://www.isi.csic.es/dataset/anomalousTrafficTest.rar


unrar e normalTrafficTraining.rar 
unrar e normalTrafficTest.rar 
unrar e anomalousTrafficTest.rar 

mkdir data/raw

mv normalTrafficTraining.txt ./data/raw
mv normalTrafficTest.txt ./data/raw
mv anomalousTrafficTest.txt ./data/raw

rm normalTrafficTraining.rar
rm normalTrafficTest.rar
rm anomalousTrafficTest.rar 

