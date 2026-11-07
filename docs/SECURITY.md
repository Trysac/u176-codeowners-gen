# Security notes

## Threat model

`trysac-codeowners-gen` is a pure Python library without network I/O or subprocess calls. The primary threats are:

- **Resource Exhaustion**: The tool parses potentially large git log files. This is defended by an enforced `max_bytes` limit of 10,000,000 bytes in `parse_log`, which prevents memory exhaustion.
- **Input Sanitization**: Callers may pass malicious strings. This is defended by validating inputs (e.g., regex checks on handles) and raising explicit `CodeownersError` exceptions with error codes, rather than attempting to process potentially dangerous data.
- **Error Feedback**: Error messages truncate at 200 characters to prevent log injection or memory issues when reporting malformed input.

This tool does not defend against compromised dependencies or unauthorized access to the environment where the input logs are generated.

To report a vulnerability, see [SECURITY.md](../SECURITY.md).
