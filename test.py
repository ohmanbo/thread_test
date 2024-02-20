import socket

# 서버 주소 및 포트 설정
server_B4 = ('37.10.127.126', 57555) # Gernamy
server_B5 = ('37.10.127.126', 57557) # Gernamy
server_B6 = ('37.10.127.126', 57559) # Gernamy
server_B7 = ('37.10.127.126', 57561) # Gernamy



def query_server(ip, port):
    # Build the request for A2S_INFO, a Steam Query Protocol command
    request = b'\xFF\xFF\xFF\xFFTSource Engine Query\x00'
    address = server_B7

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(request, address)
        response, _ = sock.recvfrom(4096)
    return response

# Example usage
ip_address = '37.10.127.126'
port_number = 57561  # Default ARK server port; change if your server uses a different one
response = query_server(ip_address, port_number)
print(response)