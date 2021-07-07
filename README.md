# gmailifiy
This tool validates if gmail addresses and corporate emails with google mail servers are valid without being authenticated. The default thread is 10 to avoid being rate limited.

## Check a single gmail address
```
echo "example@gmail.com" | python3 gmailify.py -
```
## Input from file
```
python3 gmailify.py email.txt
```
## Pass through proxy
```
python3 gmailify.py -p http://127.0.0.1:8080 email.txt
```
## Output to a file
```
python3 gmailify.py -o output.txt email.txt
```
