import argparse
import jinja2

parser = argparse.ArgumentParser(description='List of IP addresses.')
parser.add_argument('ips', metavar='N', type=str, nargs='+',
                    help='ip addresses')

args = parser.parse_args()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "hosts.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(ip_list=args.ips)

with open("hosts", "w") as fh:
    fh.write(outputText)