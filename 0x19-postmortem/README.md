Postmortem: Outage Incident on Web Stack
Issue Summary
Duration:
May 10th, 2024, 10:00 PM GMT to May 11th, 2024, 2:00 AM GMT
Impact:
Complete service disruption of our primary web application, affecting approximately 80% of users with access issues.
Timeline
10:00 PM GMT: Automated monitoring alerts detected increased server response times.
10:15 PM GMT: Engineering team initiated investigation, suspecting database overload.
11:00 PM GMT: Focus on optimizing database queries and resource scaling.
11:45 PM GMT: Continued service degradation led to network infrastructure analysis.
12:30 AM GMT: DDoS attack suspected due to unusual traffic patterns.
1:00 AM GMT: Escalation to network operations team for in-depth analysis.
2:00 AM GMT: Misconfiguration in load balancer settings identified as root cause.
2:30 AM GMT: Correction of load balancer settings, service restored.
Root Cause and Resolution
Root Cause:
Misconfiguration in load balancer settings, causing traffic bottlenecks.
Resolution:
Load balancer configuration corrected to distribute requests evenly across servers.
Corrective and Preventative Measures
Improvements/Fixes:
Implement automated checks for load balancer configurations.
Enhance monitoring for network traffic and load balancing.
Tasks:
Review load balancer configurations for potential misconfigurations.
Establish a maintenance schedule for load balancer infrastructure.
