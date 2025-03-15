import socket
import os
HOST = '0.0.0.0'
PORT = 9999

def html_type():
  files = os.listdir(os.getcwd())
  list_files = ""
  for file in files:
    if file == "main.py":
      continue
    list_files += f"<a href='/{file}'><li>{file}</li></a>"
  return f"""
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web Server</title>
</head>
<body>
  <h1>
    Welcome to Web Server
    
  </h1>
  <p>Here are the files you can download from the server :) </p>
  <ul>
    {list_files}
  </ul>
</body>
</html>
  """

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 and tcp
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

soc.bind((HOST,PORT))

soc.listen(10)
print(f"[*] Listening as {HOST}:{PORT}")



# print(c_soc,c_addr)
while True:
  c_soc , c_addr = soc.accept()
  request = c_soc.recv(1024).decode()
  print(request)
  headers = request.split("\n")
  temp = headers[0].split()
  method = temp[0]
  path = temp[1]
  print(path)
  if method != "GET":
    print("Method not allowed")
    response = "HTTP/1.1 400 Bad Request\n"
    c_soc.send(response.encode())
    c_soc.close()
    continue 

  if path == "/":
    content = html_type()
    response = "HTTP/1.1 200 OK\n\n" + content
    c_soc.sendall(response.encode())
    c_soc.close()
    continue
  else:
    try:
      with open(path[1:], "rb") as file:
        content = file.read()
        file_name = os.path.basename(path[1:])
        headers = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: application/octet-stream\r\n"
                    f"Content-Disposition: attachment; filename=\"{file_name}\"\r\n"
                    f"Content-Length: {len(content)}\r\n"
                    "\r\n"
                )
        response = headers + content.decode()
        c_soc.sendall(response.encode())
        c_soc.close()
    except FileNotFoundError:
      response = "HTTP/1.1 404 Not Found\n"
      c_soc.sendall(response.encode())
      c_soc.close()
      continue
# html_type()