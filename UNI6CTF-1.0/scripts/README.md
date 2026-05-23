## Custom Script

To process the Base16384 encoded payload, I wrote a small Python decoding utility using the `pybase16384` library.

The script:
- converted the Unicode glyph stream into UTF-16BE bytes,
- decoded the Base16384 payload,
- attempted UTF-8 interpretation,
- and saved binary output when plaintext decoding failed.

### Script Location

```text
scripts/base16384_decoder.py
```