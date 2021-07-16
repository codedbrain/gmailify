# gmailify
This tool validates if gmail addresses and corporate emails with google mail servers are valid without being authenticated. The default thread is 10 to avoid being rate limited.

## Check a single gmail address
```
python gmailify.py -e example@gmail.com
```
## Input from file
```
python gmailify.py -f emails.txt
```
## Pass through proxy
```
python gmailify.py -p http://127.0.0.1:8080 -f emails.txt
```
## Output to a file
```
python gmailify.py -f emails.txt -o output.txt
```
