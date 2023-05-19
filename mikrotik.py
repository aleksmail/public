import netmiko
from netmiko import ConnectHandler

def main():
    mikrot_cred = {
        'device_type': 'mikrotik_routeros',
        'host': '192.168.100.59',
        'username': 'admin',
        'password': '',
        'port': '22'
    }

    sshCli = ConnectHandler(**mikrot_cred)
    print(sshCli.find_prompt())
    sendcmd = sshCli.send_command('/interface ethernet print')
    print(sendcmd)

    commands = ['/ip address add address=172.16.16.1/32 interface=bridge disable=no',
                '/ipv6 address add address=2001:db8:acad:1::1/64 advertise=no interface=bridge disable=no']

    #sendcmdlist = sshCli.send_config_set(commands, cmd_verify=True)
    #print(sendcmdlist)

    bkp = sshCli.send_command('/export')
    print(bkp)

    sshCli.disconnect()

    file = open("backup.txt", "w")
    file.write(bkp)
    file.close()

if __name__ == '__main__':
    main()