


import sys
import re
from scapy.all import *
from memory_profiler import profile

@profile
def get_url_from_payload(payload):
    http_header_regex = r"(?P<name>.*?): (?P<value>.*?)\r\n"
    start = payload.index(b"GET ") +4
    end = payload.index(b" HTTP/1.1")
    url_path = payload[start:end].decode("utf8")
    http_header_raw = payload[:payload.index(b"\r\n\r\n") + 2 ]
    http_header_parsed = dict(re.findall(http_header_regex, http_header_raw.decode("utf8")))
    url = http_header_parsed["Host"] + url_path + "\n"
    return url

@profile
def parse_pcap(pcap_path, urls_file):
    urls_output = open(urls_file,'wb')
    for packet in PcapReader(pcap_path):
        try:
            if packet[TCP].dport == 80:
                if packet[IP].src == "147.182.172.189":
                    print((packet[IP].src))
                    payload = bytes(packet[TCP].payload)
                    url = get_url_from_payload(payload)
                    urls_output.write(url.encode("utf8"))
        except:
            pass
        # if packet[TCP].dport == 80:
        #     payload = bytes(packet[TCP].payload)
        #     url = get_url_from_payload(payload)
        #     urls_output.write(url.encode())
         
      # payload = bytes(packet[TCP])
        # try:
        #     #print(payload.decode())
        #     url = get_url_from_payload(payload)
        #     urls_output.write(url.encode("utf8"))
        # except Exception as e:
        #     print(e)
        #     pass
        # if packet[IP].src == "147.182.172.189" or packet[IP].dst == "147.182.172.189":
        #     payload = bytes(packet[TCP].payload)
        #     url = get_url_from_payload(payload)
        #     print(url)
            #  if packet[TCP].dport == 80:
            #     payload = bytes(packet[TCP].payload)
            #     url = get_url_from_payload(payload)
            #     urls_output.write(url.encode())

    #    set((p[IP].src, p[IP].dst) for p in PcapReader('file.pcap') if IP in p)
# + bytes(packet[TCP].sport) + bytes(packet[TCP].dport) + bytes(packet[TCP].seq) + bytes(packet[TCP].ack) + bytes(packet[TCP].flags) + bytes(packet[TCP].window) + bytes(packet[TCP].urgptr) + bytes(packet[TCP].payload)
        # ipSrc = bytes((packet[IP].src),encoding='utf8').decode()
        # ipDest = bytes((packet[IP].dst),encoding='utf8').decode()

        # if "147.182.172.189" in ipSrc or "147.182.172.189" in ipDest:
        #     # print(ipSrc + " - " + ipDest)
        #     payload = bytes(packet[TCP].payload)
        #     url = get_url_from_payload(payload)
        #     print(url)

#        print(payload.decode())
        # print(packet)
        # payload = bytes(packet[TCP].payload)
        # url = get_url_from_payload(payload)
        # urls_output.write(payload)
        #urls_output.write(url.encode())
         
    # urls_output.close()


def main(arguments):
    # if len(arguments) == 5:
    #     if arguments[1] == "--pcap" and arguments[3] == "--output":
    #         parse_pcap("capture.pcap", "payload3.txt")
    parse_pcap("capture.pcap", "payload3.txt")


if __name__ == "__main__":
    main(("capture.pcap", "payload3.txt"))