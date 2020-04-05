
import sys
import robin_stocks as r

if len(sys.argv) != 3:
    print('Usage: python3 Main.py <username> <password>')
    sys.exit(0)

r.login(sys.argv[1], sys.argv[2])

print(r.load_account_profile())

r.logout()

