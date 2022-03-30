
procHigh = "●"
procMedium = "●"
procMedium = "●"


toolStatus = [

    ["has IPv6", 1, procMedium, " < 15s", "ipv6", ["not found", "has IPv6"]],


    ["Server Error", 0, procMedium, " < 30s", "asp.netmisconf", [
        "unable to resolve host address", "Connection timed out"]],


    ["wp-login", 0, procMedium, " < 30s", "wpcheck",
     ["unable to resolve host address", "Connection timed out"]],


    ["drupal", 0, procMedium, " < 30s", "drupalcheck", [
        "unable to resolve host address", "Connection timed out"]],


    ["joomla", 0, procMedium, " < 30s", "joomlacheck", [
        "unable to resolve host address", "Connection timed out"]],


    ["[+]", 0, procMedium, " < 40s", "robotscheck",
     ["Use of uninitialized value in unpack at"]],


    ["No WAF", 0, procMedium, " < 45s",
     "wafcheck", ["appears to be down"]],


    ["tcp open", 0, procMedium, " <  2m",
     "nmapopen", ["Failed to resolve"]],


    ["No emails found", 1, procMedium, " <  3m",
     "harvester", ["No hosts found", "No emails found"]],


    ["[+] Zone Transfer was successful!!", 0, procMedium,
     " < 20s", "dnsreconzt", ["Could not resolve domain"]],





    ["0 errors", 0, procMedium, " < 35s", "dnswalkzt",
     ["!!!0 failures, 0 warnings, 3 errors."]],


    ["Admin Email:", 0, procMedium, " < 25s",
     "whois", ["No match for domain"]],


    ["XSS filter is disabled", 0, procMedium,
     " < 20s", "nmapxssh", ["Failed to resolve"]],


    ["VULNERABLE", 0, procHigh, " < 45m",
     "nmapdos", ["Failed to resolve"]],


    ["Server is vulnerable to Heartbleed", 0, procMedium,
     " < 40s", "sslyzehb", ["Could not resolve hostname"]],


    ["VULNERABLE", 0, procMedium, " < 30s",
     "nmap1", ["Failed to resolve"]],


    ["VULNERABLE", 0, procMedium, " < 35s",
     "nmap2", ["Failed to resolve"]],


    ["VULNERABLE", 0, procMedium, " < 35s",
     "nmap3", ["Failed to resolve"]],


    ["VULNERABLE", 0, procMedium, " < 30s",
     "nmap4", ["Failed to resolve"]],


    ["VULNERABLE", 0, procMedium, " < 35s",
     "nmap5", ["Failed to resolve"]],


    ["ERROR - OCSP response status is not successful", 0, procMedium,
     " < 25s", "sslyze1", ["Could not resolve hostname"]],


    ["VULNERABLE", 0, procMedium, " < 30s",
     "sslyze2", ["Could not resolve hostname"]],


    ["VULNERABLE", 0, procMedium, " < 25s",
     "sslyze3", ["Could not resolve hostname"]],


    ["VULNERABLE", 0, procMedium, " < 30s",
     "sslyze4", ["Could not resolve hostname"]],


    ["does NOT use Load-balancing", 0, procMedium,
     " <  4m", "lbd", ["NOT FOUND"]],


    ["No vulnerabilities found", 1, procMedium, " < 45s", "golism1", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["No vulnerabilities found", 1, procMedium, " < 40s", "golism2", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["No vulnerabilities found", 1, procMedium, " < 45s", "golism3", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["No vulnerabilities found", 1, procMedium, " < 40s", "golism4", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["No vulnerabilities found", 1, procMedium, " < 45s", "golism5", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["FOUND: 0", 1, procHigh, " < 35m", "dirb",
     ["COULDNT RESOLVE HOST", "FOUND: 0"]],


    ["Could not find any vulnerability!", 1, procMedium, " <  4m", "xsser", [
        "XSSer is not working propertly!", "Could not find any vulnerability!"]],


    ["Occurrence ID", 0, procMedium, " < 45s",
     "golism6", ["Cannot resolve domain name"]],


    ["DNS zone transfer successful", 0, procMedium,
     " < 30s", "golism7", ["Cannot resolve domain name"]],


    ["Nikto found 0 vulnerabilities", 1, procMedium, " <  4m", "golism8", [
        "Cannot resolve domain name", "Nikto found 0 vulnerabilities"]],


    ["Possible subdomain leak", 0, procHigh, " < 30m",
     "golism9", ["Cannot resolve domain name"]],


    ["AXFR record query failed:", 1, procMedium, " < 45s", "dnsenumzt", [
        "NS record query failed:", "AXFR record query failed", "no NS record for"]],


    ["Found 0 entries", 1, procHigh, " < 75m",
     "fierce2", ["Found 0 entries", "is gimp"]],


    ["Found 0 E-Mail(s)", 1, procMedium, " < 30s", "dmitry1",
     ["Unable to locate Host IP addr", "Found 0 E-Mail(s)"]],


    ["Found 0 possible subdomain(s)", 1, procMedium, " < 35s", "dmitry2", [
        "Unable to locate Host IP addr", "Found 0 possible subdomain(s)"]],


    ["open", 0, procMedium, " < 15s",
     "nmaptelnet", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 15s", "nmapftp", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 20s",
     "nmapstux", ["Failed to resolve"]],


    ["SUCCEED", 0, procMedium, " < 30s", "webdav",
     ["is not DAV enabled or not accessible."]],


    ["No vulnerabilities found", 1, procMedium, " < 15s", "golism10", [
        "Cannot resolve domain name", "No vulnerabilities found"]],


    ["[+]", 0, procMedium, " <  2m", "uniscan2",
     ["Use of uninitialized value in unpack at"]],


    ["[+]", 0, procMedium, " <  5m", "uniscan3",
     ["Use of uninitialized value in unpack at"]],


    ["[+]", 0, procMedium, " <  9m", "uniscan4",
     ["Use of uninitialized value in unpack at"]],


    ["[+]", 0, procMedium, " <  8m", "uniscan5",
     ["Use of uninitialized value in unpack at"]],


    ["[+]", 0, procMedium, " <  9m", "uniscan6",
     ["Use of uninitialized value in unpack at"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto1", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto2", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto3", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto4", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto5", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto6", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto7", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto8", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto9", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto10", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto11", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto12", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto13", [
        "ERROR: Cannot resolve hostname", "0 item(s) reported", "No web server found", "0 host(s) tested"]],


    ["0 item(s) reported", 1, procMedium, " < 35s", "nikto14",
     "ERROR: Cannot resolve hostname , 0 item(s) reported"],


    ["#1", 0, procHigh, " < 30m", "dnsmap_brute", [
        "[+] 0 (sub)domains and 0 IP address(es) found"]],


    ["open", 0, procMedium, " < 15s",
     "nmapmssql", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 15s",
     "nmapmysql", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 15s",
     "nmaporacle", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 15s",
     "nmapudprdp", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 15s",
     "nmaptcprdp", ["Failed to resolve"]],


    ["open", 0, procHigh, " > 50m",
     "nmapfulltcp", ["Failed to resolve"]],


    ["open", 0, procHigh, " > 75m",
     "nmapfulludp", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 30s",
     "nmapsnmp", ["Failed to resolve"]],


    ["Microsoft SQL Server Error Log", 0, procMedium, " < 30s", "elmahxd", [
        "unable to resolve host address", "Connection timed out"]],


    ["open", 0, procMedium, " < 20s",
     "nmaptcpsmb", ["Failed to resolve"]],


    ["open", 0, procMedium, " < 20s",
     "nmapudpsmb", ["Failed to resolve"]],


    ["Host:", 0, procMedium, " < 5m", "wapiti", ["none"]],


    ["WebDAV is ENABLED", 0, procMedium, " < 40s",
     "nmapwebdaviis", ["Failed to resolve"]],


    ["X-XSS-Protection[1", 1, procMedium, " < 3m", "whatweb",
     ["Timed out", "Socket error", "X-XSS-Protection[1"]],


    ["No names were discovered", 1, procMedium, " < 15m", "amass",
     ["The system was unable to build the pool of resolvers"]]



]
