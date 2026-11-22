#!/usr/bin/env python3
"""Run sequential checks from an explicit local target manifest."""
import argparse
import json
import math
import sys
from check import check

def evaluate(targets):
    if not isinstance(targets,list) or not 1 <= len(targets) <= 100:
        raise ValueError('supply between 1 and 100 target objects')
    normalized = []
    for target in targets:
        host,port = target['host'],int(target['port'])
        timeout = float(target.get('timeout',2))
        if not isinstance(host,str) or not host or not 1 <= port <= 65535 or not math.isfinite(timeout) or timeout<=0:
            raise ValueError('each target needs a host, port 1-65535 and positive finite timeout')
        normalized.append((host,port,timeout))
    return [check(host,port,timeout) for host,port,timeout in normalized]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    args = parser.parse_args()
    try:
        with open(args.manifest) as source:
            results = evaluate(json.load(source))
    except (OSError,ValueError,TypeError,KeyError) as error:
        print('Input error: '+str(error),file=sys.stderr)
        return 2
    print(json.dumps({'checks':results,'all_ok':all(r['ok'] for r in results)}))
    return 0 if all(r['ok'] for r in results) else 1

if __name__=='__main__':
    raise SystemExit(main())
