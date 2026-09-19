import requests as r
import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from genusername import gen

robloxApi = "https://auth.roblox.com/v1/usernames/validate"

# shared state
session = r.Session()
_xcsrf_token = None
_token_time = 0
TOKEN_TTL = 60 * 20
last_request_time = 0
REQUEST_DELAY = 0.25

lock = threading.Lock()

def _post_with_token(headers, payload):
    global _xcsrf_token, _token_time

    res = session.post(robloxApi, json=payload, headers=headers)

    if res.status_code == 403:
        new_token = res.headers.get("x-csrf-token")
        if new_token:
            with lock:
                _xcsrf_token = new_token
                _token_time = time.time()

            headers["X-CSRF-TOKEN"] = new_token
            return session.post(robloxApi, json=payload, headers=headers)

    return res

def _rate_limited():
    global last_request_time

    with lock:
        now = time.time()
        wait = REQUEST_DELAY - (now - last_request_time)

        if wait > 0:
            time.sleep(wait)

        last_request_time = time.time()

def _check_username(username):
    global _xcsrf_token, _token_time

    _rate_limited()

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json;charset=UTF-8",
    }

    with lock:
        if _xcsrf_token and (time.time() - _token_time < TOKEN_TTL):
            headers["X-CSRF-TOKEN"] = _xcsrf_token

    payload = {
        "birthday": "2003-11-08T17:00:00.000Z",
        "context": "Signup",
        "username": username
    }

    try:
        res = _post_with_token(headers, payload)
        res.raise_for_status()
        data = res.json()

        return data.get("code") == 0 and data.get("message") == "Username is valid"

    except r.exceptions.RequestException:
        return False


def trySniping(username=None):
    if username is None:
        username = gen()

    time.sleep(random.uniform(0.2, 0.5))  # polite delay
    return _check_username(username)


def run_workers(count=10, max_workers=5):
    found = False

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(trySniping) for _ in range(count)]

        for future in as_completed(futures):
            result = future.result()
            print(result)

            if result:
                found = True

    return found
    
def snipeLoop(loop, option, length, max_workers=5):
    if not loop or not option:
        return []

    option_map = {
        1: "four",
        2: "five",
	3: "words",
        4: "random",
        5: "lnb",
	6: "numbers"
    }

    gen_type = option_map.get(option)
    if not gen_type:
        return []

    usernames = set()
    while len(usernames) < loop:
        username = gen(gen_type, length or None)
        if username not in usernames:
            print(f"\033[38;2;217;217;0m    Queued `{username}`")
            usernames.add(username)

    usernames = list(usernames)

    gotUsernames = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(trySniping, u): u for u in usernames}

        for future in as_completed(futures):
            username = futures[future]
            try:
                result = future.result()

                if result:
                    gotUsernames.append(username)
                    print(f"\033[38;2;0;217;105m    `{username}` is AVAILABLE")
                else:
                    print(f"\033[38;2;217;0;83m    `{username}` is taken")

            except Exception as e:
                print(f"Error with {username}: {e}")

    return gotUsernames