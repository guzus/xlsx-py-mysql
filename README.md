# xlsx-py-mysql

Load **.xlsx** data to **MySQL** database conveniently with only a few lines of **Python** code!

## How to run

1. **Install python & dependencies**

Python >=3.8 is recommended.
```
pip3 install -r requirements.txt
```
2. **Configure [.env](.env.example) file**

This enables Python to access into your MySQL.

3. **Configure [settings.py](settings.py)**

This inform Python what data to extract from .xlsx file, what MySQL table to put data.

4. **Run python**

To see rich log, run `python load.py log`.
```
python load.py
```

## Development Rules

1. **Renew [requirements.txt](requirements.txt)**
```
pip3 freeze > requirements.txt
```

2. **Use [Black](https://github.com/psf/black) to format code**
```
black .
```

3. **Regex for Commit Message**

`Initial commit` than `initial commit` is better commit message.
```
[A-Z][\S]*\s[A-Za-z][\s\S]*
```

## Participate!

Please post `Issues` if you have any issues or suggestions.
