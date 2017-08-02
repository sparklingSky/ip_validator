import ipaddress
import ipcalc
__author__ = 'sparklingSky'


def ip_validator(input_data):
    """
    :param input_data: string of IP addresses or subnet(s)
    :return: formatted list of all IP addresses
    """
    formatted_input_data = ""
    for symbol in input_data:
        if symbol is not ",":
            formatted_input_data += symbol
    formatted_input_data = formatted_input_data.split()
    for item in formatted_input_data:
        try:
            ipaddress.ip_network(item)
        except:
            try:
                ipaddress.ip_address(input_data)
            except ValueError:
                return 1
    formatted_ip_list = []
    for item in formatted_input_data:
        try:
            lst = []
            for ip in ipcalc.Network(item):
                lst.append(str(ip))
            formatted_ip_list.extend(lst)
        except:
            formatted_ip_list.append(item)
            
    return formatted_ip_list

# ips = "1.2.3.0/28, 4.5.6.20"
# print(ip_validator(ips))
