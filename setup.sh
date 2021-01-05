# python3 sollte schon installiert sein.
# pip3 muss noch installiert werden
sudo apt install -y python3-pip git
# Klonen des git repo des scriptes
git clone https://github.com/sonnix-de/computerspende.git
# das Script benötigt einige requirements

cd computerspende 

pip3 install -U -r requirements.txt

python3 main.py

cd ..

rm -rf computerspende