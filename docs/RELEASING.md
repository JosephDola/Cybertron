# Releasing C.Y.B.E.R.

C.Y.B.E.R. releases are automated with GitHub Actions.

## Simple version

To publish a release, update:

`release-trigger/current.json`

Example:

```json
{
  "version": "v13.0.3",
  "title": "C.Y.B.E.R. V13.0.3 — Hardware Reliability Update",
  "notes_file": "releases/v13.0.3/README.md",
  "prerelease": true
}
```

Pushing that change to `main` starts `.github/workflows/release.yml`.

The workflow automatically:

1. validates the version and release notes,
2. creates a ZIP of the exact source commit,
3. creates SHA-256 checksums,
4. creates the Git tag if needed,
5. creates the GitHub Release,
6. uploads the source ZIP and checksum file,
7. uploads any optional files stored under `release-assets/<version>/`.

## Optional installer files

If a release has extra built files, place them in a folder matching the tag, for example:

`release-assets/v14.0.0/Cybertron-v14.0.0-macOS-x86_64.dmg`

`release-assets/v14.0.0/Cybertron-v14.0.0-Windows.zip`

Those files will be attached automatically when the release is published.

## Release notes

Keep release notes easy to read. Start with:

- what changed,
- why it matters,
- what the user needs to do,
- known limitations.

Technical implementation details can go later in the page.

## Alpha releases

While C.Y.B.E.R. is still alpha software, use:

```json
"prerelease": true
```

When the project is ready for stable public releases, change it to `false`.
