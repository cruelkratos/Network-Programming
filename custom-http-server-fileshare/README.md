# Simple HTTP File Server

A lightweight HTTP server implementation that allows you to browse and download files from the directory where the server is running.

## Features

- **Directory Listing**: Displays all files in the current directory as clickable links
- **File Downloads**: Enables downloading of any file from the server
- **Clean Interface**: Simple HTML interface for browsing available files
- **TCP/IP Based**: Built on Python's socket library using TCP connections

## How It Works

This server implements a basic subset of the HTTP protocol:

1. **Server Initialization**: Binds to all network interfaces (0.0.0.0) on port 9999
2. **Request Handling**: Processes incoming GET requests
3. **Response Types**:
   - Directory listing (when accessing the root URL "/")
   - File downloads (when requesting a specific file)
   - Error responses (404 for file not found, 400 for non-GET methods)

## Usage

1. Place the script in the directory containing files you wish to share
2. Run the server:

```bash
python main.py
```

3. Access the server through a web browser at:

```
http://localhost:9999
```

4. Browse the file list and click any file to download it

## Technical Details

- **Protocol**: HTTP/1.1
- **Supported Methods**: GET only
- **Content Types**: 
  - HTML for directory listing
  - application/octet-stream for file downloads
- **Socket Configuration**: TCP with address reuse enabled
- **Connection Handling**: One connection at a time, with a listen backlog of 10

## Limitations

- Only supports GET requests
- No authentication or access control
- Limited error handling
- No support for concurrent connections (processes one request at a time)
- Binary files may not download correctly due to encoding issues

## Security Considerations

This server has minimal security features and should only be used in trusted environments:
- No input validation or path traversal protection
- All files in the directory become publicly accessible
- No encryption (HTTP, not HTTPS)

## Requirements

- Python 3.x
- Standard library only (socket, os)

## Example Directory Listing

When accessing the root URL, you'll see a page similar to:

```
Welcome to Web Server

Here are the files you can download from the server :)

• file1.txt
• image.jpg
• document.pdf
```

Each file name is a clickable link that will download the corresponding file.
