import concurrent.futures
import requests
import time
import os

# ANSI Color Codes for beautiful blue styling
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Place your proxies here inside the list between the quotation marks
PROXIES = ["127.0.0.1:8080",]

TEST_URL = "http://httpbin.org/ip"
MAX_PING = 2000  # Maximum acceptable ping in milliseconds
TIMEOUT = 3.0    # Short timeout to avoid wasting time on dead proxies

def print_banner():
    # Clears the terminal screen before printing the banner
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = f"""
{BLUE}{BOLD}=================================================================
  _                 ____                                      
 | |    ___  ___   / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |   / _ \/ _ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__|  __/ (_) |  ___) | (_| (_| | | | | | | |  __/ |   
 |_____\___|\___/  |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                          
                     DEVELOPED BY: {CYAN}Leo scanner{BLUE}
================================================================={RESET}
    """
    print(banner)

def check_proxy(proxy):
    protocols_to_try = [
        {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"},
        {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    ]
    
    for proxies in protocols_to_try:
        try:
            # Measure start time with high precision
            start_time = time.perf_counter()
            response = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
            # Measure end time immediately upon receiving response
            end_time = time.perf_counter()
            
            if response.status_code == 200:
                # Calculate ping in milliseconds as an integer
                ping_ms = int((end_time - start_time) * 1000)
                proto = "SOCKS5" if "socks5" in proxies["http"] else "HTTP/S"
                
                # Proxy filtering condition (exclude proxies above 2000ms)
                if ping_ms <= MAX_PING:
                    print(f"✅ LIVE ({proto}) -> {proxy} | Ping: {ping_ms}ms")
                    return proxy, proto, ping_ms
                else:
                    print(f"❌ EXCLUDED (Too Slow) -> {proxy} | Ping: {ping_ms}ms")
                    return None
        except:
            continue
            
    print(f"❌ DEAD or Unresponsive: {proxy}")
    return None

def main():
    print_banner()
    
    if not PROXIES:
        print(f"{BLUE}[{CYAN}!{BLUE}]{RESET} Proxy list is empty! Please add proxies inside the code first.")
        return

    print(f"{BLUE}[{CYAN}*{BLUE}]{RESET} Starting check and filtration (Max acceptable ping: {MAX_PING}ms)...")
    print(f"{BLUE}-" * 65 + f"{RESET}")
    
    working_proxies = []
    
    # Using ThreadPoolExecutor for high-speed concurrent checking
    with concurrent.futures.ThreadPoolExecutor(max_workers=60) as executor:
        results = executor.map(check_proxy, PROXIES)
        for result in results:
            if result:
                working_proxies.append(result)
                
    print(f"{BLUE}-" * 65 + f"{RESET}")
    print(f" {BLUE}[{CYAN}✓{BLUE}]{RESET} Check finished! Accepted and fast proxies: {BLUE}{BOLD}{len(working_proxies)}{RESET}")
    
    # Save the results to the requested file: proxiesW.txt
    if working_proxies:
        with open("proxiesW.txt", "w", encoding="utf-8") as f:
            for proxy, proto, ping in working_proxies:
                f.write(f"{proxy} | Type: {proto} | Ping: {ping}ms\n")
        print(f" ✅ Valid proxies successfully saved to: {CYAN}proxiesW.txt{RESET}")
    else:
        print(" ❌ No fast proxies under 2000ms were found to save.")

if __name__ == "__main__":
    main()
