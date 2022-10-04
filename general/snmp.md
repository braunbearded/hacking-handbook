# bruteforce community string

```bash
onesixtyone -c /usr/share/metasploit-framework/data/wordlists/snmp_default_pass.txt $rhost
hydra -P /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt $rhost snmp
```

# read all values from snmp

```bash
snmpwalk -v 1|2c|3 -c [COMM_STRING] $rhost
snmpwalk -v 1|2c|3 -c public $rhost
snmpwalk -v 2c -c public $rhost NET-SNMP-EXTEND-MIB::nsExtendObjects
snmpwalk -v 2c -c public $rhost NET-SNMP-EXTEND-MIB::nsExtendOutputFull
snmp-check -w "$rhost"
snmpwalk -v 2c -c public -m all $rhost

```

# read specific value from snmp

```bash
snmpwalk -v 1|2c|3 -c public $rhost OID
```

# full export until OID 99999

```bash
snmpwalk -v 2c -c public $rhost -I r -C E 99999
```

# full export until OID 99999 (values only)

```bash
snmpwalk -v 2c -c public $rhost -I r -C E 99999 -v
```
