#!/usr/bin/env python3
"""
A simple API using Python's http.server module
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Root endpoint - simple text
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # JSON data endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Status check endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            # Info endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # Handle unknown endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            error = "Endpoint not found"
            self.wfile.write(error.encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8000)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()
