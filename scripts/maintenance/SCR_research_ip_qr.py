import socket
import qrcode
import os

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def test_qr():
    ip = get_local_ip()
    url = f"http://{ip}:8000"
    print(f"Server URL: {url}")
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="navy", back_color="white")
    img.save("scratch/test_classroom_qr.png")
    print("QR Code saved to scratch/test_classroom_qr.png")

if __name__ == "__main__":
    test_qr()
