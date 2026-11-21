# Adapted from the TCP port scanning example in Python Penetration
# Testing Essentials, Packt Publishing, January 2015.
# ISBN: 978-1-78439-858-3.
#python version 3 
import socket

hosts_input = input(
    "Enter the IPv4 addresses separated by commas: "
).split(",")

hostlist = []

# Validate each IPv4 address.
for item in hosts_input:
    host = item.strip()
    ip_parts = host.split(".")
    valid_ip = True

    if len(ip_parts) != 4:
        valid_ip = False

    else:
        for part in ip_parts:
            if not part.isdecimal() or not (0 <= int(part) <= 255):
                valid_ip = False
                break

    # This validation belongs inside the hosts loop.
    if not valid_ip:
        print(f"Invalid IPv4 address: {host}.")
    else:
        hostlist.append(host)

if not hostlist:
    print("No valid IPv4 addresses to scan.")

else:
    ports_input = input(
        "Insert the ports or ranges separated by commas: "
    ).split(",")

    portlist = []

    for item in ports_input:
        p = item.strip()

        if "-" in p:
            limits = p.split("-")

            if len(limits) != 2:
                print(f"Ignored invalid range: {p}")
                continue

            start = limits[0].strip()
            end = limits[1].strip()

            if start.isdecimal() and end.isdecimal():
                start = int(start)
                end = int(end)

                if 1 <= start <= end <= 65535:
                    for port in range(start, end + 1):
                        portlist.append(port)
                else:
                    print(f"Ignored invalid range: {p}")
            else:
                print(f"Ignored invalid range: {p}")

        elif p.isdecimal() and 1 <= int(p) <= 65535:
            portlist.append(int(p))

        else:
            print(f"Ignored invalid port: {p}")

    if not portlist:
        print("No valid ports to scan.")

    else:
        # Scan all selected ports on each valid machine.
        for host in hostlist:
            print(f"\nScanning machine: {host}")

            for port in portlist:
                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                try:
                    sock.settimeout(3)
                    result = sock.connect_ex((host, port))

                    if result == 0:
                        print(
                            "Connection accepted for port", port,
                            "- code:", result
                        )

                    elif result == 11:
                        print(
                            "Connection not completed within timeout"
                            " for port", port,
                            "- code:", result
                        )

                    elif result == 111:
                        print(
                            "Connection refused for port", port,
                            "- code:", result
                        )

                    else:
                        print(
                            "Connection failed for port", port,
                            "- code:", result
                        )

                except socket.timeout:
                    print("Connection timed out for port", port)

                except socket.error as error:
                    print("Connection error for port", port, "-", error)

                finally:
                    sock.close()
