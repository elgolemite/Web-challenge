<<<<<<< HEAD
# AturKreatif26
Share questions heree
=======
# Ping Me Maybe

## Category
Web Exploitation

## Difficulty
Easy

## Flag Format
`3108{...}`

## Challenge Description
The company's internal IT department has deployed **NetPulse Diagnostic Suite v1.2.4**, a high-fidelity web utility designed for real-time network latency monitoring and host reachability testing.

While the interface looks state-of-the-art and professional, the underlying execution logic might be less sophisticated than the design suggests. 

The IT team claims the system is "fully isolated and secure." Prove them wrong and exfiltrate the administrative flag.

## Run Locally

```bash
docker compose up --build
```

Open:

```text
http://localhost:5000
```

## Challenge URL Format

```text
http://<challenge-ip>:<port>/
```

## Hints

### Hint 1
The application sends your input to a system command.

### Hint 2
A ping command does not always have to run alone.

### Hint 3
Try listing the files in the current directory.

## Flag

```text
3108{p1ng_t00l_g0_brrr}
```
>>>>>>> 859892e (Add Ping Me Maybe command injection challenge)
