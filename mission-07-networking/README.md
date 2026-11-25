# Mission 7 — How computers communicate

## Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A Local Area Network connects devices within a small, single location like a home, classroom, or office. | All laptops and phones connected to my home Wi-Fi router. |
| **MAN** | A Metropolitan Area Network spans across a whole city or a large university/corporate campus. | A city-wide public Wi-Fi network or interconnected buildings across a large university campus. |
| **WAN** | A Wide Area Network connects multiple smaller networks across huge geographic distances, countries, or continents. | The global Internet connecting computers in India to servers around the world. |
| **DNS** | The Domain Name System acts like the internet's phonebook, translating human-readable website names into numeric IP addresses. | Translating `example.com` into its numeric IP address (`93.184.216.34`) so a browser can locate the server. |
| **Router** | A networking device that connects different networks together and directs data packets along the best path to their destination. | A home Wi-Fi router forwarding web requests from my laptop to my Internet Service Provider (ISP). |
| **Protocol** | A shared set of rules and formats that computers follow so they can reliably send, receive, and understand data. | `HTTPS` for secure web browsing or `TCP/IP` for reliable internet data transmission. |
| **Packet switching** | Breaking large messages or files into small chunks (packets) that travel independently across the network and get reassembled at the destination. | Streaming a video where small data packets take different routes across the internet and reassemble smoothly on screen. |
| **Client-server** | A communication model where a user's device (the client) requests data or a service, and a central computer (the server) processes and sends back the response. | My web browser (client) requesting a webpage from GitHub's web server (server). |

---

## Task 7.2 — Observe network information

### Commands Used
```bash
ping -c 4 example.com
nslookup example.com
```
*(Note: Personal IP addresses and local DNS server details have been omitted/redacted for privacy.)*

### Observations & Explanations
* **What a connectivity test (`ping`) helps you check:**
  A connectivity test checks whether my computer can successfully reach a target website or server over the network, how long it takes for data packets to make a round trip (latency in milliseconds), and whether any packets were lost along the way.
* **What information a DNS lookup (`nslookup`) displays:**
  A DNS lookup displays the domain name queried (`example.com`) and the public IPv4/IPv6 network address(es) associated with that domain so devices know where to send traffic.
* **Role of DNS when you enter a website name in a browser:**
  Because computers communicate using numeric IP addresses rather than words, DNS automatically translates the domain name typed into the browser into the destination server's exact IP address before the connection is made.

---

## Task 7.3 — What happens when you open a website?

1. **User enters the URL:** I type a website address (such as `https://example.com`) into my web browser, which acts as the **client**.
2. **DNS lookup:** The browser checks its cache and queries a **DNS** server to translate the human-readable domain name into the destination server's numeric IP address.
3. **Request travels through the network:** My computer packages the request into small data packets using standard networking **protocols** (such as TCP/IP and HTTPS) and sends them through my local **router** and ISP across the internet.
4. **Connection and HTTP/HTTPS request:** Once the packets reach the destination web **server**, the client and server establish a connection and the client sends a formal HTTP/HTTPS request asking for the webpage files.
5. **Server processes the request:** The **server** locates or generates the requested HTML, CSS, and image files and breaks them into data packets to send back to my IP address.
6. **Browser renders the response:** The packets travel back through the **router** to my **client** device, where the browser reassembles them and displays the complete webpage on my screen.

---

## Reflection & Challenges Faced
* **Summary:** Reviewed core networking concepts (LAN/MAN/WAN, DNS, routers, protocols, packet switching, client-server), tested live network connectivity and DNS resolution in Terminal, and traced the step-by-step lifecycle of loading a webpage.
* **Challenges:** Making sure to redact local network details and IP addresses from terminal output while clearly explaining how DNS, routers, and protocols work together.
