import ipaddress
import sys
from rich import print
from tqdm.rich import tqdm 
cidr_file = open(sys.argv[1], "r")
ips_file = open(str(sys.argv[1])+".out", "w")
cidr_count = open(sys.argv[1], "r")
lines = cidr_count.readlines()
#count = 0
def ip_from_cidr(cidr_file, lines):
  """
  Expand a cidr into its constituent IPs including broadcast and network addresses
  """
  global count
  count = 0
  with tqdm(total = len(lines)) as pbar:
    for ip_cidr in cidr_file:
      pbar.update(1)
      ip_cidr = ip_cidr.rstrip()
      for ip in ipaddress.ip_network(ip_cidr):
        count += 1 
        print ('%s' % ip)
        print ('%s' % ip, file = ips_file)
      

print(ip_from_cidr(cidr_file, lines))
print(f"[red] {str(count)} [/]IPs saved to: >>> [red]{ips_file.name}[/]")