# Author: Melissa Melaugh
# Date Created: 11 August 2016
# Date Updated: 11 August 2016
# Description: This class opens a server, and displays the VM orders on a web page
# File: server
# Status: Complete

# Imports
import http.server  # https://docs.python.org/3/library/http.server.html
                    # https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer
import webbrowser  # https://docs.python.org/3/library/webbrowser.html?highlight=webbrowser#module-webbrowser

web_message = "This is the default message"


class Display(http.server.BaseHTTPRequestHandler):
    # This class creates the display page on the server.
    def do_GET(self):
        # This fixes the str variable to a working html

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # update message for display
        message = web_message.replace("\t", "&nbsp;&nbsp;&nbsp;").split("\n")  # makes the \t readable
        # Write content as utf-8 data and display
        for i in range(0, len(message)):
            self.wfile.write(bytes(message[i] + "<br />", "utf8"))  # inputs the \n and writes to the html page
        return
    # end do_GET
# end Display Class


def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    # Runs the server
    print("Server Starting...")
    server_address = ('127.0.0.1', 9191)
    httpd = server_class(server_address, Display)
    print("Server running, opening web application...")
    webbrowser.open_new("http://localhost:9191/")

    httpd.handle_request()
    httpd.server_close()
    # Server started on local port 9191, opens the web browser with the message created in Display, handles the request
    # and then closes down immediately.
# end run
