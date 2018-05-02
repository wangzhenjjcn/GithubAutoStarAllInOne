#!bin/bash
sed -i 's/^NAME.*$/NAME='\"${NAME:-"1"}\"'/g' /GitHubStar/settings.py
sed -i 's/^PASSWORD.*$/PASSWORD='\"${PASSWORD:-"1"}\"'/g' /GitHubStar/settings.py
sed -i 's/^GITNAME.*$/GITNAME='\"${GITNAME:-"1"}\"'/g' /GitHubStar/settings.py
sed -i 's/^GITPASSWORD.*$/GITPASSWORD='\"${GITPASSWORD:-"1"}\"'/g' /GitHubStar/settings.py

python -u main.py