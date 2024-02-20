import a2s
import time

# 서버 주소 및 포트 설정
server_list = [
 {'_cellName': 'A1', '_serverInfo': {'IP': '37.10.127.123', 'Port': 57555}},
 {'_cellName': 'A2', '_serverInfo': {'IP': '37.10.127.123', 'Port': 57557}},
 {'_cellName': 'A3', '_serverInfo': {'IP': '37.10.127.123', 'Port': 57559}},
 {'_cellName': 'A4', '_serverInfo': {'IP': '37.10.127.123', 'Port': 57561}},
 {'_cellName': 'A5', '_serverInfo': {'IP': '37.10.127.124', 'Port': 57555}},
 {'_cellName': 'A6', '_serverInfo': {'IP': '37.10.127.124', 'Port': 57557}},
 {'_cellName': 'A7', '_serverInfo': {'IP': '37.10.127.124', 'Port': 57559}},
 {'_cellName': 'A8', '_serverInfo': {'IP': '37.10.127.124', 'Port': 57561}},
 {'_cellName': 'A9', '_serverInfo': {'IP': '37.10.127.125', 'Port': 57555}},
 {'_cellName': 'B1', '_serverInfo': {'IP': '37.10.127.125', 'Port': 57557}},
 {'_cellName': 'B2', '_serverInfo': {'IP': '37.10.127.125', 'Port': 57559}},
 {'_cellName': 'B3', '_serverInfo': {'IP': '37.10.127.125', 'Port': 57561}},
 {'_cellName': 'B4', '_serverInfo': {'IP': '37.10.127.126', 'Port': 57555}},
 {'_cellName': 'B5', '_serverInfo': {'IP': '37.10.127.126', 'Port': 57557}},
 {'_cellName': 'B6', '_serverInfo': {'IP': '37.10.127.126', 'Port': 57559}},
 {'_cellName': 'B7', '_serverInfo': {'IP': '37.10.127.126', 'Port': 57561}},
 {'_cellName': 'B8', '_serverInfo': {'IP': '37.10.127.127', 'Port': 57555}},
 {'_cellName': 'B9', '_serverInfo': {'IP': '37.10.127.127', 'Port': 57557}},
 {'_cellName': 'C1', '_serverInfo': {'IP': '37.10.127.127', 'Port': 57559}},
 {'_cellName': 'C2', '_serverInfo': {'IP': '37.10.127.127', 'Port': 57561}},
 {'_cellName': 'C3', '_serverInfo': {'IP': '37.10.127.128', 'Port': 57555}},
 {'_cellName': 'C4', '_serverInfo': {'IP': '37.10.127.128', 'Port': 57557}},
 {'_cellName': 'C5', '_serverInfo': {'IP': '37.10.127.128', 'Port': 57559}},
 {'_cellName': 'C6', '_serverInfo': {'IP': '37.10.127.128', 'Port': 57561}},
 {'_cellName': 'C7', '_serverInfo': {'IP': '37.10.127.129', 'Port': 57555}},
 {'_cellName': 'C8', '_serverInfo': {'IP': '37.10.127.129', 'Port': 57557}},
 {'_cellName': 'C9', '_serverInfo': {'IP': '37.10.127.129', 'Port': 57559}},
 {'_cellName': 'D1', '_serverInfo': {'IP': '37.10.127.129', 'Port': 57561}},
 {'_cellName': 'D2', '_serverInfo': {'IP': '37.10.127.130', 'Port': 57555}},
 {'_cellName': 'D3', '_serverInfo': {'IP': '37.10.127.130', 'Port': 57557}},
 {'_cellName': 'D4', '_serverInfo': {'IP': '37.10.127.130', 'Port': 57559}},
 {'_cellName': 'D5', '_serverInfo': {'IP': '37.10.127.130', 'Port': 57561}},
 {'_cellName': 'D6', '_serverInfo': {'IP': '37.10.127.131', 'Port': 57555}},
 {'_cellName': 'D7', '_serverInfo': {'IP': '37.10.127.131', 'Port': 57557}},
 {'_cellName': 'D8', '_serverInfo': {'IP': '37.10.127.131', 'Port': 57559}},
 {'_cellName': 'D9', '_serverInfo': {'IP': '37.10.127.131', 'Port': 57561}},
 {'_cellName': 'E1', '_serverInfo': {'IP': '37.10.127.132', 'Port': 57555}},
 {'_cellName': 'E2', '_serverInfo': {'IP': '37.10.127.132', 'Port': 57557}},
 {'_cellName': 'E3', '_serverInfo': {'IP': '37.10.127.132', 'Port': 57559}},
 {'_cellName': 'E4', '_serverInfo': {'IP': '37.10.127.132', 'Port': 57561}},
 {'_cellName': 'E5', '_serverInfo': {'IP': '37.10.127.133', 'Port': 57555}},
 {'_cellName': 'E6', '_serverInfo': {'IP': '37.10.127.133', 'Port': 57557}},
 {'_cellName': 'E7', '_serverInfo': {'IP': '37.10.127.133', 'Port': 57559}},
 {'_cellName': 'E8', '_serverInfo': {'IP': '37.10.127.133', 'Port': 57561}},
 {'_cellName': 'E9', '_serverInfo': {'IP': '37.10.127.134', 'Port': 57555}},
 {'_cellName': 'F1', '_serverInfo': {'IP': '37.10.127.134', 'Port': 57557}},
 {'_cellName': 'F2', '_serverInfo': {'IP': '37.10.127.134', 'Port': 57559}},
 {'_cellName': 'F3', '_serverInfo': {'IP': '37.10.127.134', 'Port': 57561}},
 {'_cellName': 'F4', '_serverInfo': {'IP': '37.10.127.135', 'Port': 57555}},
 {'_cellName': 'F5', '_serverInfo': {'IP': '37.10.127.135', 'Port': 57557}},
 {'_cellName': 'F6', '_serverInfo': {'IP': '37.10.127.135', 'Port': 57559}},
 {'_cellName': 'F7', '_serverInfo': {'IP': '37.10.127.135', 'Port': 57561}},
 {'_cellName': 'F8', '_serverInfo': {'IP': '37.10.127.136', 'Port': 57555}},
 {'_cellName': 'F9', '_serverInfo': {'IP': '37.10.127.136', 'Port': 57557}},
 {'_cellName': 'G1', '_serverInfo': {'IP': '37.10.127.136', 'Port': 57559}},
 {'_cellName': 'G2', '_serverInfo': {'IP': '37.10.127.136', 'Port': 57561}},
 {'_cellName': 'G3', '_serverInfo': {'IP': '37.10.127.137', 'Port': 57555}},
 {'_cellName': 'G4', '_serverInfo': {'IP': '37.10.127.137', 'Port': 57557}},
 {'_cellName': 'G5', '_serverInfo': {'IP': '37.10.127.137', 'Port': 57559}},
 {'_cellName': 'G6', '_serverInfo': {'IP': '37.10.127.137', 'Port': 57561}},
 {'_cellName': 'G7', '_serverInfo': {'IP': '37.10.127.138', 'Port': 57555}},
 {'_cellName': 'G8', '_serverInfo': {'IP': '37.10.127.138', 'Port': 57557}},
 {'_cellName': 'G9', '_serverInfo': {'IP': '37.10.127.138', 'Port': 57559}},
 {'_cellName': 'H1', '_serverInfo': {'IP': '37.10.127.138', 'Port': 57561}},
 {'_cellName': 'H2', '_serverInfo': {'IP': '37.10.127.139', 'Port': 57555}},
 {'_cellName': 'H3', '_serverInfo': {'IP': '37.10.127.139', 'Port': 57557}},
 {'_cellName': 'H4', '_serverInfo': {'IP': '37.10.127.139', 'Port': 57559}},
 {'_cellName': 'H5', '_serverInfo': {'IP': '37.10.127.139', 'Port': 57561}},
 {'_cellName': 'H6', '_serverInfo': {'IP': '37.10.127.140', 'Port': 57555}},
 {'_cellName': 'H7', '_serverInfo': {'IP': '37.10.127.140', 'Port': 57557}},
 {'_cellName': 'H8', '_serverInfo': {'IP': '37.10.127.140', 'Port': 57559}},
 {'_cellName': 'H9', '_serverInfo': {'IP': '37.10.127.140', 'Port': 57561}},
 {'_cellName': 'I1', '_serverInfo': {'IP': '37.10.127.141', 'Port': 57555}},
 {'_cellName': 'I2', '_serverInfo': {'IP': '37.10.127.141', 'Port': 57557}},
 {'_cellName': 'I3', '_serverInfo': {'IP': '37.10.127.141', 'Port': 57559}},
 {'_cellName': 'I4', '_serverInfo': {'IP': '37.10.127.141', 'Port': 57561}},
 {'_cellName': 'I5', '_serverInfo': {'IP': '37.10.127.142', 'Port': 57555}},
 {'_cellName': 'I6', '_serverInfo': {'IP': '37.10.127.142', 'Port': 57557}},
 {'_cellName': 'I7', '_serverInfo': {'IP': '37.10.127.142', 'Port': 57559}},
 {'_cellName': 'I8', '_serverInfo': {'IP': '37.10.127.142', 'Port': 57561}},
 {'_cellName': 'I9', '_serverInfo': {'IP': '37.10.127.143', 'Port': 57555}}]

start_time = time.time()


for server in server_list:
    iteration_start = time.time()
    
    server_ip = server['_serverInfo']['IP']
    server_port = server['_serverInfo']['Port']
    try:
        server_info = a2s.rules((server_ip, server_port))
    except Exception as e:
            print(f"Error fetching server info: {e}")
            continue  # 에러가 발생하면 다음 서버로 넘어감
        
       
    #server_name = server_info.server_name
    day_time = server_info['DayTime_s']
    player_number = 150 - int(server_info['NUMOPENPUBCONN'])
    
    iteration_end = time.time()  # 현재 반복 종료 시간
    
    
    print(f"{server['_cellName']} day_time: {day_time}, player_number: {player_number}, duration: {iteration_end - iteration_start}\n")

end_time = time.time()  # 전체 반복문 종료 시간
print(f"전체 반복문 수행 시간: {end_time - start_time}초")

#result = a2s.players(server)
#print(result)

#result = a2s.rules(server)
#print(result)