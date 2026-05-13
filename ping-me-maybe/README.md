# Ping Me Maybe

# Author

Chop chicken

## Category
Web 

## Difficulty
Easy

## Flag Format

```text
AK26{...}
```

## Challenge Description

My loneliness is killing me, and i, i must confess i still believe, still believe, when i'm not with you i lose my mind, give me a sign!!!

## Objective

Exploit the vulnerable ping diagnostic feature and recover the hidden admin recovery token.

## Provided URL

```text
http://<challenge-host>:5000/
```

For local testing:

```text
http://127.0.0.1:5000/
```

## Run Locally

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:5000/
```

## Files

Recommended challenge structure:

```text
ping-me-maybe/
├── README.md
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── index.html
```

## Important Routes

| Route | Description |
|---|---|
| `/` | Main NetPulse ping utility |
| `/health` | Simple health check endpoint |

## Default Flag

```text
AK26{p1ng_m3_b4by_0n3_m0r3_t1m3}
```

The flag is stored inside the container as an internal recovery token.

## Player Hints

### Hint 1
The application passes your input into a system command.

### Hint 2
A ping command does not always have to run alone.

### Hint 3
Start by listing files and checking nearby directories.

## Intended Solution Summary

1. Open the NetPulse ping utility.
2. Submit a normal host such as `127.0.0.1` to understand the output.
3. Notice that the application returns raw command output.
4. Test command chaining through the host input.
5. Enumerate the current directory and nearby files.
6. Follow the note pointing to the backup diagnostic log.
7. Read the internal recovery token file and recover the flag.

## Vulnerability

The backend builds a shell command using unsanitized user input:

```python
cmd = f"ping -c 1 {host}"
```

Because the command is executed with `shell=True`, command separators can be used to run additional commands.

## Organizer Notes

This challenge is designed for beginners learning command injection. The UI is intentionally realistic and modern, but the backend logic is simple.

The Docker image installs `iputils-ping`, creates a low-privileged `ctf` user, and stores the flag in an internal-looking file path to encourage basic Linux enumeration after exploitation.

Do not expose this challenge outside an isolated CTF/lab environment.
