from os import system; from json import loads as loadJson; from json import dumps as dumpJson; from json.decoder import JSONDecodeError; from sys import version_info, stdout

if version_info < (3, 0):
    stdout.write("This script is for Python 3.0 <=")

try:
    from mitmproxy import http
except ModuleNotFoundError:
    system("pip3 install mitmproxy")
try:
	import pyperclip
except ModuleNotFoundError:
    system("pip3 install pyperclip")

bypassJson = {
	"result" : "success"
}

def response(flow : http.HTTPFlow) -> None:
    request, response = flow.request, flow.response
    if request.host == "api.auth.gg":
        try:
            data = loadJson(response.content)
            if len(data) != 0:
                dataPresent = True
            elif len(data) == 0:
                dataPresent = False
        except JSONDecodeError:
            dataPresent = False
        if dataPresent:
            response.content = dumpJson(bypassJson).encode()
        else:
            response.content = dumpJson(bypassJson).encode()


def main():
	print("[+] Usage: mitmproxy -s '{0}'".format(__file__)); pyperclip.copy("mitmproxy -s '{0}'".format(__file__)); print("[+] Copied to clipboard"); print("If mitmproxy doesnt work, use the command but with 'mitmweb' instead")

if __name__ == "__main__":
	main()
