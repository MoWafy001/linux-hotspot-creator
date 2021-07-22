from subprocess import getoutput, call

IFNAME = getoutput("iw dev").split("Interface ")[1].split("\n")[0]

CON_NAME = "MyHS" # default
try:
    CON_NAME = input("Hotspot name: ")
except Exception:
    pass

PASS = 12345678 # default
try:
    PASS = input("Password: ")
except Exception:
    pass

try:
    command_0 = f"nmcli con delete '{CON_NAME}'"
    command_1 = f"nmcli con add type wifi ifname {IFNAME} con-name '{CON_NAME}' autoconnect yes ssid '{CON_NAME}'"
    command_2 = f"nmcli con modify '{CON_NAME}' 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared"
    command_4 = f'nmcli con modify "{CON_NAME}" wifi-sec.psk "{PASS}"'
    command_3 = f"nmcli con modify '{CON_NAME}' wifi-sec.key-mgmt wpa-psk"
    command_5 = f"nmcli con up '{CON_NAME}'"

    removing_hs = getoutput(command_0)
    if "Error" not in removing_hs:
        print(removing_hs)

    call(f"{command_1};{command_2};{command_3};{command_4};{command_5};", shell=True)
    print("OK\n")
    print(f"==================\nName: {CON_NAME}\nPass: {PASS}\n==================\n")
    print("press Enter to stop...")
    input()
except KeyboardInterrupt:
    pass

print("deactivatating the hotspot...")
call(f"nmcli con down {CON_NAME}", shell=True)
print("removing the hotspot...")
call(command_0, shell=True)
print("done.")