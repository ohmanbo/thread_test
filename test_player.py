import socket

# https://www.steambrowser.com/server/kfgameinfo_survival/37.10.127.126:57561
# 서버 주소 및 포트 설정
server_B4 = ('37.10.127.126', 57555) # Gernamy
server_B5 = ('37.10.127.126', 57557) # Gernamy
server_B6 = ('37.10.127.126', 57559) # Gernamy
server_B7 = ('37.10.127.126', 57561) # Gernamy


server_address = server_B7
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 챌린지 넘버 요청
message = b'\xFF\xFF\xFF\xFF\x55\xFF\xFF\xFF\xFF'
sock.sendto(message, server_address)

# 챌린지 넘버 응답 받기
response, _ = sock.recvfrom(4096)
challenge_number = response[5:]  # 챌린지 넘버 추출
print(challenge_number)

# A2S_PLAYER 쿼리 보내기
player_query = b'\xFF\xFF\xFF\xFF\x55' + challenge_number
print(player_query)
#sock.sendto(player_query, server_address)

# 플레이어 정보 응답 받기
#player_info, _ = sock.recvfrom(4096)
#print(player_info)

sock.close()