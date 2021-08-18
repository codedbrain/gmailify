# gmailify
This tool validates if gmail addresses and corporate emails with google mail servers are valid without being authenticated. The default thread is 10 to avoid being rate limited.

# Installation
```
python -m pip install gmailify
```

## Check a single gmail address
```
python -m gmailify -e example@gmail.com
```
## Input from file
```
python -m gmailify -f emails.txt
```
## Pass through proxy
```
python -m gmailify -p http://127.0.0.1:8080 -f emails.txt
```
## Output to a file
```
python -m gmailify -f emails.txt -o output.txt
```
