# Inspect IP address properties: implementation

## What the example does

ipaddress parses IPv4 and IPv6 without DNS lookup. Private-range classifications depend on the Python version; address syntax and loopback checks are deterministic.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"127.0.0.1"
```

Expected result:

```json
{
  "version": 4,
  "compressed": "127.0.0.1",
  "loopback": true
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
