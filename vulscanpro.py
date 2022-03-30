#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Name__ = "VulScanPro"
__Discription__ = "Automatic Web Vulnerability Scanner."
__Version__ = "1.0.0"
__Author__ = "Md. Nur Habib"

# Importing the libraries
import sys
import argparse
import subprocess
import os
import time
import random
import threading
import re
import random
from urllib.parse import urlsplit
from core.toolcmd import *
from core.toolfix import *
from core.toolnames import *
from core.toolprecheck import *
from core.toolresp import *
from core.toolstatus import *
from plugins.banner import BannerFunction
from plugins.colors import *


# Scan Time Elapser
intervalsVariable = (
    ("h", 3600),
    ("m", 60),
    ("s", 1),
)


def displayTimeFunction(secoundVariable, granularity=3):
    resultVariable = []
    secoundVariable = secoundVariable + 1
    for name, count in intervalsVariable:
        valueVariable = secoundVariable // count
        if valueVariable:
            secoundVariable -= valueVariable * count
            resultVariable.append("{}{}".format(valueVariable, name))
    return " ".join(resultVariable[:granularity])


def terminalSizeFunction():
    try:
        rows, columns = subprocess.check_output(["stty", "size"]).split()
        return int(columns)
    except subprocess.CalledProcessError as e:
        return int(20)



def urlMarkerFunction(url):
    if not re.match(r'http(s?)\:', url):
        url = 'http://' + url
    parsed = urlsplit(url)
    host = parsed.netloc
    if host.startswith('www.'):
        host = host[4:]
    return host


def checkInternetConnectionFunction():
    os.system("ping -c1 github.com > rs_net 2>&1")
    if "0% packet loss" in open("rs_net").read():
        val = 1
    else:
        val = 0
    os.system("rm rs_net > /dev/null 2>&1")
    return val


# Classifies the Vulnerability"s Severity
def vulnerablitryInformation(val):
    resultVariable = ""
    if val == "c":
        resultVariable = bold + red + " critical : " + reset
    elif val == "h":
        resultVariable = bold + orange + " high : " + reset
    elif val == "m":
        resultVariable = bold + purple + " medium : " + reset
    elif val == "l":
        resultVariable = bold + blue + " low : " + reset
    else:
        resultVariable = bold + lightgrey + " info : " + reset
    return resultVariable


procHigh = red + "●" + reset
pprocMedium = orange + "●" + reset
procLow = green + "●" + reset


def vulnerabilityRemedInformationFunction(v1, v2, v3):
    print(bold+"Vulnerability Threat Level"+reset)
    print("\t"+vulnerablitryInformation(v2)+" "+orange +
          str(toolResponse[v1][0])+reset)
    print(bold+"Vulnerability Definition"+reset)
    print("\t"+red+str(toolFix[v3-1][1])+reset)
    print(bold+"Vulnerability Remediation"+reset)
    print("\t"+green+str(toolFix[v3-1][2])+reset)


# Help Menu
def helper():
    print(f"{bold}{blue}Usage : \n")
    print(f"{orange}>> python vulscanpro example.com\n")
    print(f"{blue}-h, --help           : Help Menu")
    print("-s, --skip           : Skip some tools and scan faster.")
    print("-u, --update         : Update VulScanPro.")
    print(f"-n, --nospinner      : Disable the IDLE spinner.{reset}")


def clearFunction():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


class Spinner:
    busy = False
    delay = 0.005

    @staticmethod
    def spinningCorsorFunction():
        while 1:

            for cursor in " ":
                yield cursor

    def __init__(self, delay=None):
        self.spinningGenerator = self.spinningCorsorFunction()
        if delay and float(delay):
            self.delay = delay
        self.disabled = False

    def spinningTaskFunction(self):
        inc = 0
        try:
            while self.busy:
                if not self.disabled:
                    x = + \
                        next(self.spinningGenerator)
                    inc = inc + 1
                    print(x, end="")
                    if inc > random.uniform(0, terminalSizeFunction()):
                        print(end="\r") + \
                            str(round(random.uniform(40, 47)))+"m"
                        inc = 0
                    sys.stdout.flush()
                time.sleep(self.delay)
                if not self.disabled:
                    sys.stdout.flush()

        except (KeyboardInterrupt, SystemExit):
            print("\n\tQuitting...")
            sys.exit(1)

    def startFunction(self):
        self.busy = True
        try:
            threading.Thread(target=self.spinningTaskFunction).startFunction()
        except Exception as e:
            print("\n")

    def stop(self):
        try:
            self.busy = False
            time.sleep(self.delay)
        except (KeyboardInterrupt, SystemExit):
            print("\n\tQuitting...")
            sys.exit(1)


spinner = Spinner()

# Tool Names
toolNames

# Tool CMD
toolCMD
# Tool Response
toolResponse

# Tool Status
toolStatus

# Tool Fix
toolFix

# Tool precheck
toolsPreCheck


def getParserFunction():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="store_true",
                        help="Show help message and exit.")
    parser.add_argument("-u", "--update", action="store_true",
                        help="Update VulScanPro.")
    parser.add_argument("-s", "--skip", action="append", default=[],
                        help="Skip some tools", choices=[t[0] for t in toolsPreCheck])
    parser.add_argument("-n", "--nospinner", action="store_true",
                        help="Disable the idle loader/spinner.")
    parser.add_argument("target", nargs="?", metavar="URL",
                        help="URL to scan.", default="", type=str)
    return parser


getParserFunction()


scanShuffleVariabe = list(zip(toolNames, toolCMD, toolResponse, toolStatus))
random.shuffle(scanShuffleVariabe)
toolNames, toolCMD, toolResponse, toolStatus = zip(*scanShuffleVariabe)
toolChecksVariable = (len(toolNames) + len(toolResponse) + len(toolStatus)) / 3
toolChecksVariable = round(toolChecksVariable)

# Variables And List
tool = 0
runTest = 1
argumentOne = 0
argumentTwo = 1
argumentThree = 2
argumentFour = 3
argumentFive = 4
argumentSix = 5

scanVulnerablitryList = list()
scanVulneriblityNumber = 0
scanVulnerariblity = 0

scanTotalElapsed = 0
scanAvailTools = 0
scanSkippedTools = 0

if len(sys.argv) == 1:
    BannerFunction()
    helper()
    sys.exit(1)

argumentNameSpace = getParserFunction().parse_args()

if argumentNameSpace.nospinner:
    spinner.disabled = True

if argumentNameSpace.help or (not argumentNameSpace.update
                              and not argumentNameSpace.target):
    BannerFunction()
    helper()

elif argumentNameSpace.update:
    BannerFunction()
    print(f"{bold}{cyan}VulScanPro is Updating, Please Wait.{reset}\n")
    spinner.startFunction()
    rs_internet_availability = checkInternetConnectionFunction()
    if rs_internet_availability == 0:
        print(f"\t{bold}{red}Found Connecting Error.Try Again.{reset}")
        spinner.stop()
        sys.exit(1)
    cmd = "sha1sum vulscanpro | grep .... | cut -c 1-40"
    oldVersionofHash = subprocess.check_output(cmd, shell=True)
    oldVersionofHash = oldVersionofHash.strip()
    os.system("wget -N https://raw.githubusercontent.com/thenurhabib/vulscanpro/master/vulscanpro -O vulscanpro > /dev/null 2>&1")
    newVersionofHash = subprocess.check_output(cmd, shell=True)
    newVersionofHash = newVersionofHash.strip()
    if oldVersionofHash == newVersionofHash:
        clearFunction()
        print(f"\t{bold}You already have the latest version of VulScanPro.{reset}")
    else:
        clearFunction()
        print(f"{bold}\tVulScanPro successfully updated to the latest version.{reset}")
    spinner.stop()
    sys.exit(1)

elif argumentNameSpace.target:
    target = urlMarkerFunction(argumentNameSpace.target)
    os.system("rm /tmp/te* > /dev/null 2>&1")
    os.system("clear")
    os.system("setterm -cursor off")
    BannerFunction()
    print(f"{bold}{blue}Checking Available Security Scanning Tools Phase... Initiated.{reset}\n")

    unavalableToolNames = list()

    while (scanAvailTools < len(toolsPreCheck)):
        preComandLine = str(toolsPreCheck[scanAvailTools][argumentOne])
        try:
            p = subprocess.Popen([preComandLine], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            val = output + err
        except:
            print(f"\t{bold}{blue}VulScanPro was terminated abruptly.{reset}")
            sys.exit(1)

        if b"Not Found" in val or toolsPreCheck[scanAvailTools][argumentOne] in argumentNameSpace.skip:
            if b"not found" in val:
                print(
                    f"\t{blue}{toolsPreCheck[scanAvailTools][argumentOne]}{reset}{red}...unavailable.{reset}")

            elif toolsPreCheck[scanAvailTools][argumentOne] in argumentNameSpace.skip:
                print(
                    f"\t{blue}{toolsPreCheck[scanAvailTools][argumentOne]}{reset}{red}...skipped.{reset}")

            for scanner_index, scanner_val in enumerate(toolNames):
                if scanner_val[2] == toolsPreCheck[scanAvailTools][argumentOne]:

                    scanner_val[3] = 0
                    unavalableToolNames.append(
                        toolsPreCheck[scanAvailTools][argumentOne])

        else:
            print(
                f"\t{blue}{toolsPreCheck[scanAvailTools][argumentOne]}{reset}{green}...available.{reset}")
        scanAvailTools = scanAvailTools + 1
        clearFunction()
    unavalableToolNames = list(set(unavalableToolNames))
    if len(unavalableToolNames) == 0:
        print(f"\t{green}All Scanning Tools are available.{reset}")
    else:
        print(f"\t{orange}Some of these tools {red}" + str(unavalableToolNames) + f"{reset}{orange}are unavailable.{reset}")
    print(f"{bold}{blue}\nChecking Available Security Scanning Tools Phase... Completed.{reset}")
    print("\n")
    print(f"Preliminary Scan Phase Initiated... Loaded"+str(toolChecksVariable)+" vulnerability checks.")

    while(tool < len(toolNames)):
        print("["+toolStatus[tool][argumentThree]+toolStatus[tool][argumentFour]+"] Deploying "+str(tool+1) +"/"+str(toolChecksVariable)+" | "+blue+toolNames[tool][argumentTwo]+reset,)
        if toolNames[tool][argumentFour] == 0:
            print(f"{orange}\nScanning Tool Unavailable. Skipping Test...\n{reset}")
            scanSkippedTools = scanSkippedTools + 1
            tool = tool + 1
            continue
        try:
            spinner.startFunction()
        except Exception as e:
            print("\n")
        scanStartVariable = time.time()
        temporarryFilesVariable = f"/tmp/VulScanPro_temp_{toolNames[tool][argumentOne]}"
        cmd = toolCMD[tool][argumentOne]+target + \
            toolCMD[tool][argumentTwo]+" > "+temporarryFilesVariable+" 2>&1"

        try:
            subprocess.check_output(cmd, shell=True)
        except KeyboardInterrupt:
            runTest = 0
        except:
            runTest = 1

        if runTest == 1:
            spinner.stop()
            scanStopVariable = time.time()
            elapsed = scanStopVariable - scanStartVariable
            scanTotalElapsed = scanTotalElapsed + elapsed
            print(blue+"Scan Completed in " + displayTimeFunction(int(elapsed))+reset, end="\r", flush=True)
            print("\n")
            scanToolOutputFileVariable = open(temporarryFilesVariable).read()
            if toolStatus[tool][argumentTwo] == 0:
                if toolStatus[tool][argumentOne].lower() in scanToolOutputFileVariable.lower():
                    vulnerabilityRemedInformationFunction(
                        tool, toolResponse[tool][argumentTwo], toolResponse[tool][argumentThree])
                    scanVulnerablitryList.append(
                        toolNames[tool][argumentOne]+"*"+toolNames[tool][argumentTwo])
            else:
                if any(i in scanToolOutputFileVariable for i in toolStatus[tool][argumentSix]):
                    m = 1  
                else:
                    vulnerabilityRemedInformationFunction(
                        tool, toolResponse[tool][argumentTwo], toolResponse[tool][argumentThree])
                    scanVulnerablitryList.append(
                        toolNames[tool][argumentOne]+"*"+toolNames[tool][argumentTwo])
        else:
            runTest = 1
            spinner.stop()
            scanStopVariable = time.time()
            elapsed = scanStopVariable - scanStartVariable
            scanTotalElapsed = scanTotalElapsed + elapsed

            print(blue+"\nScan Interrupted in " + displayTimeFunction(int(elapsed))+reset, end="\r", flush=True)
            print(f"{orange}\n\tTest Skipped. Performing Next. Press Ctrl+Z to Quit VulScanPro.\n{reset}")
            scanSkippedTools = scanSkippedTools + 1

        tool = tool + 1

    print(f"{bold}{blue}Preliminary Scan Phase Completed.{reset}\n")
    print(f"{bold}{blue}Report Generation Phase Initiated.{reset}")
    if len(scanVulnerablitryList) == 0:
        print(f"\t{green}No Vulnerabilities Detected.{reset}")
    else:
        with open("RS-Vulnerability-Report", "a") as report:
            while(scanVulnerariblity < len(scanVulnerablitryList)):
                vulnerableIformation = scanVulnerablitryList[scanVulnerariblity].split(
                    "*")
                report.write(vulnerableIformation[argumentTwo])
                report.write("\n------------------------\n\n")
                temporaryReport_name = "/tmp/VulScanPro_temp_" + \
                    vulnerableIformation[argumentOne]
                with open(temporaryReport_name, "r") as temporaryReport:
                    data = temporaryReport.read()
                    report.write(data)
                    report.write("\n\n")
                temporaryReport.close()
                scanVulnerariblity = scanVulnerariblity + 1

            print(
                f"\tComplete Vulnerability Report for {blue}{target}{reset}named {green}`RS-Vulnerability-Report`{reset} is available under the same directory VulScanPro resides.")

        report.close()

    for fileIndex, fileName in enumerate(toolNames):
        with open("RS-Debug-ScanLog", "a") as report:
            try:
                with open("/tmp/VulScanPro_temp_"+fileName[argumentOne], "r") as temporaryReport:
                    data = temporaryReport.read()
                    report.write(fileName[argumentTwo])
                    report.write("\n------------------------\n\n")
                    report.write(data)
                    report.write("\n\n")
                temporaryReport.close()
            except:
                break
        report.close()

    print("\tTotal Vulnerability Checks         : " + bold + green+ str(len(toolNames))+reset)
    print("\tTotal Vulnerability Skipped        : " + bold + orange +str(scanSkippedTools)+reset)
    print("\tTotal Vulnerabilities Detected     : " + bold + red +str(len(scanVulnerablitryList))+reset)
    print("\tTotal Time Elapsed for the Scan    : " + bold + blue +displayTimeFunction(int(scanTotalElapsed))+reset)
    os.system("setterm -cursor on")
    os.system("rm /tmp/VulScanPro_te* > /dev/null 2>&1")
