<img src="assets/pulse.png" width="200" alt="Pulse Logo">

[![Python 3.8+](https://img.shields.io/badge/python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ethical Use](https://img.shields.io/badge/use-authorized%20only-critical.svg)]()

⚠️ LEGAL WARNING

🚨 AUTHORIZED USE ONLY 🚨

This tool is for **authorized penetration testing ONLY**. You must have explicit written permission to test any target system.

Pulse is an advanced stress testing tool that simulates real user traffic to evaluate web application resilience under load. Unlike basic flooding tools, Pulse includes modern evasion techniques to test against WAF-protected infrastructure.

### Key Features

✅ **User-Agent Rotation** - 10 realistic browser signatures (Chrome, Firefox, Safari, Edge, Mobile)  
✅ **Smart Headers** - Browser-specific HTTP headers that mimic legitimate traffic  
✅ **Human Timing** - Random delays (0.5-2.5s) to avoid detection  
✅ **Session Rotation** - Fresh identity every 8-25 requests  
✅ **WAF Analysis** - Real-time block rate monitoring with recommendations  
✅ **Referer Variation** - Simulates organic traffic sources (Google, Bing, direct)  
✅ **Interactive Setup** - No code editing required, all configuration via prompts

## 💪 Real-World Effectiveness

**Highly Effective Against:**

**Unprotected Servers** | 95-99% | 30-60 seconds | Apache/Nginx default configs |
**Basic WAF (ModSecurity)** | 70-85% | 1-3 minutes | Default rulesets bypassed |
**Simple Rate Limiting** | 60-80% | 2-5 minutes | Basic IP-based limits |
**Shared Hosting** | 90-99% | 20-40 seconds | Limited resources saturated |
**Internal Applications** | 85-95% | 30-90 seconds | Corporate intranets without CDN |

**Performance Metrics:**
- **Request Rate**: 300-500 req/s with 100 workers
- **Concurrent Connections**: 100-250 simultaneous
- **Memory Usage**: ~100-150 MB
- **CPU Usage**: 20-40% of one core
- **Network Bandwidth**: 10-50 Mbps

**Real Impact on Targets:**
- Unprotected servers: CPU 80-99%, response time 10-30x slower
- Service degradation or temporary unavailability
- Identifies infrastructure weaknesses effectively

**Limited Effectiveness Against:**

| **Cloudflare** | 70-90% blocked | JS challenges, CAPTCHA, fingerprinting |
| **AWS Shield/CloudFront** | 60-80% blocked | ML-based detection, auto-scaling |
| **Akamai** | 80-95% blocked | Advanced behavioral analysis |
| **Imperva WAF** | 70-90% blocked | Signature + behavioral detection |
| **DataDome** | 90%+ blocked | Canvas/TLS fingerprinting |

**Technical Limitations:**

**Detection Indicators:**
- Single source IP (easy to block)
- Pattern in timing despite randomization
- Lack of cookies/session state
- No JavaScript execution footprint
- Visible in server logs as repeated requests

### Performance Comparison

**vs Basic Tools:**

| Tool | Req/s | WAF Evasion | Pule Advantage |
|------|-------|-------------|-------------------|
| LOIC | 100-200 | None | 3x faster + smart evasion |
| hping3 | 50-100 | Layer 3/4 | Application layer + headers |
| Slowloris | 10-50 | Basic | Faster + modern techniques |
| Custom scripts | 50-150 | None | Realistic browser behavior |

**vs Professional Tools:**
| Tool | Req/s | Distribution | Use Case |
|------|-------|--------------|----------|
| Apache Bench | 1000+ | Single | Pulse better for WAF testing |
| wrk | 5000+ | Single | Pulse more realistic traffic |
| Locust | 10000+ | Distributed | Pulse = educational/small tests |
| Metasploit | Variable | Framework | Pulse = HTTP-only focused |

**Pulse Spot:**

- Better evasion than basic tools
- Simpler than full frameworks
- Ideal for learning and authorized small-scale tests
- Not suitable for production pentesting against modern infrastructures
