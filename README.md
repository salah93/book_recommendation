# nytimes recommended book
get a random(ish?) book recommended by nytimes staff

## steps
+ make sure to have python and pip installed

```
git clone https://github.com/salah93/book_recommendation.git
cd book_recommendation
pip install -U virtualenv; pip install -U virtualenvwrapper
mkvirtualenv book_rec
pip install -r requirements.txt
python run.py
cat <<EOF >> .bash_profile
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
source /usr/local/bin/virtualenvwrapper.sh
EOF
source .bash_profile
```
