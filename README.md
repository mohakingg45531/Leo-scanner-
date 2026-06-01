🚀 Leo Scanner - Fast Proxy Checker

A high-speed, multi-threaded proxy scanner and checker built with Python. `Leo Scanner` automatically filters and verifies proxies, testing their response time (Ping) and protocols, then saving the live, ultra-fast ones for you.

---

 ✨ Features
* **Multi-Threaded Performance:** Powered by `ThreadPoolExecutor` to check dozens of proxies concurrently in seconds.
* **Dual Protocol Testing:** Automatically tests both **HTTP/S** and **SOCKS5** protocols for each proxy.
* **Smart Filtering:** Automatically excludes dead, unresponsive, or slow proxies (with a ping higher than 2000ms).
* **Automatic Saving:** Saves all working and verified fast proxies neatly into a file named `proxiesW.txt`.
* **Beautiful UI:** Styled with dynamic blue ANSI color codes and a custom developer banner.

---

🛠️ Prerequisites & Installation

Before running the script, make sure you have Python installed and the required `requests` library.

1. Install Dependencies
Run the following command in your terminal or Termux to install the required package:
```bash
pip install requests

```
2. Clone the Repository
Clone this project directly to your local machine or Termux using:
```bash
git clone [https://github.com/mohakingg45531/Leo-scanner-.git](https://github.com/mohakingg45531/Leo-scanner-.git)
cd Leo-scanner-

```
 🚀 How to Use
 1. Open the leoscanner.py file using any text editor (like nano in Termux).
 2. Find the PROXIES list near the top of the script and add your proxy IPs and ports inside the quotation marks:
   ```python
   PROXIES = [
       "167.71.222.42:8080",
       "45.77.54.12:1080",
   ]
   
   ```
 3. Save the file and run the scanner using Python:
   ```bash
   python leoscanner.py
   
   ```
 📂 Output File
Once the scan finishes, the tool creates a file called **proxiesW.txt** in the same folder.
It saves the live proxies formatted like this:
```text
167.71.222.42:8080 | Type: HTTP/S | Ping: 120ms
45.77.54.12:1080 | Type: SOCKS5 | Ping: 450ms

```
👤 Developer mohakingg45531(Leo)
 
