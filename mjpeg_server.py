from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class MJPEGHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
        self.end_headers()

        while True:
            try:
                with open('C1.jpg', 'rb') as f:
                    image_data = f.read()

                self.wfile.write(b'--frame\r\n')
                self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
                self.wfile.write(image_data)
                self.wfile.write(b'\r\n')

                time.sleep(0.1)  # Adjust the delay between frames (e.g., 0.1 = 10 FPS)
            except Exception as e:
                print(f"Error: {e}")
                break

def run(server_class=HTTPServer, handler_class=MJPEGHandler, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting MJPEG server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()