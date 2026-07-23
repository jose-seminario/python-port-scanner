from scanner import scan_port_range
from ui import show_banner, show_menu
from input_handler import get_user_option, get_ip, get_port_range

show_banner()
show_menu()

option = get_user_option()

if option == 1:
    ip = get_ip()
    start_port, end_port = get_port_range()
    scan_port_range(ip, start_port, end_port)

elif option == 2:
    ip = get_ip()
    scan_port_range(ip, 1, 65535)