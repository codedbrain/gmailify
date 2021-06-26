import requests
import argparse
import sys

valid_emails = []

def argsParser():
    parser = argparse.ArgumentParser(description="Validate google emails without being authenticated")
    parser.add_argument("file", type=argparse.FileType('r'), help="File containing an email per line")
    parser.add_argument("-o", "--output", help="Output valid emails in a file", type=argparse.FileType('w'))
    parser.add_argument("-n", "--nossl", help="Disable SSL",action="store_false")
    parser.add_argument("-p", "--proxy", help="Proxy server to pass requests through -p http://127.0.0.1:8080")
    return parser.parse_args()

def check(email,proxies,ssl):
    try:
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(f'https://mail.google.com/mail/gxlu', params={'email': email},proxies=proxies,verify=ssl)
        for cookie in resp.cookies:
            if cookie.name == "COMPASS":
                return True
    except requests.exceptions.SSLError as e:
        print("SSL Error. Consider using -n flag to disable SSL errors")


def main():
    args = argsParser()
    proxies={}
    if args.proxy is not None:
        proxies = {"http":args.proxy,"https":args.proxy}

    with args.file as emails:
        for email in emails:
            email = email.rstrip("\n")
            if check(email,proxies,args.nossl):
                valid_emails.append(email)
                print(email) 

    if args.output is not None:
         for i in valid_emails:
            args.output.write(i + "\n")
            args.output.flush()

if __name__ == "__main__":
	main() 
