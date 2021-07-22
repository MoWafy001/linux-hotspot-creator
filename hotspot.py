from subprocess import getoutput, call

IFNAME = getoutput("iw dev").split("Interface ")[1].split("\n")[0]

command_0 = ""

CON_NAME = "MyHS" # default
PASS = 12345678 # default

def start_hs(title, password):
    IFNAME = getoutput("iw dev").split("Interface ")[1].split("\n")[0]

    try:
        global CON_NAME
        CON_NAME = title
        if len(CON_NAME) < 1:
            print("you typed nothing -->> defaulting to MyHS")
            CON_NAME = "MyHS"
    except Exception:
        pass

    try:
        global PASS
        PASS = password
        if len(PASS) < 8:
            print("too short -->> defaulting to 12345678")
            PASS = 12345678
    except Exception:
        pass

    try:
        global command_0
        command_0 = f"nmcli con delete '{CON_NAME}'"
        command_1 = f"nmcli con add type wifi ifname {IFNAME} con-name '{CON_NAME}' autoconnect yes ssid '{CON_NAME}'"
        command_2 = f"nmcli con modify '{CON_NAME}' 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared"
        command_3 = f"nmcli con modify '{CON_NAME}' wifi-sec.key-mgmt wpa-psk"
        command_4 = f'nmcli con modify "{CON_NAME}" wifi-sec.psk "{PASS}"'
        command_5 = f"nmcli con modify '{CON_NAME}' ipv4.addresses '192.168.125.1/24,192.168.125.1'"
        command_6 = f"nmcli con up '{CON_NAME}'"

        removing_hs = getoutput(command_0)
        if "Error" not in removing_hs:
            print(removing_hs)

        call(f"{command_1};{command_2};{command_3};{command_4};{command_5};{command_6};", shell=True)
        print("OK\n")
        print(f"==================\nName: {CON_NAME}\nPass: {PASS}\nGateway: 192.168.125.1\n==================\n")
    except KeyboardInterrupt:
        close_hs()

def close_hs():
    print("deactivatating the hotspot...")
    call(f"nmcli con down {CON_NAME}", shell=True)
    print("removing the hotspot...")
    call(command_0, shell=True)
    print("done.")