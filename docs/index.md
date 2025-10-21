# Transpiler Mate

A small and light yet poweful API + CLI to extract [Schema.org/SoftwareApplication](https://schema.org/SoftwareApplication) Metadata from an annotated [CWL](https://www.commonwl.org/) document and publish it as a Record on [Zenodo](https://zenodo.org/).

## Pre-requisites

You must own an authentication Token to pusblish on Zenodo, see how to create a [new Token](https://zenodo.org/account/settings/applications/tokens/new/).

## Installation

```
pip install transpiler-mate
```

## CLI Usage

```
$ transpiler-mate --help
Usage: transpiler-mate [OPTIONS] SOURCE

Options:
  --dry-run          Picks the Zenodo sandbox server
  --auth-token TEXT  The Zenodo Access token, see https://(sandbox.)zenodo.org
                     /account/settings/applications/tokens  [required]
  --help             Show this message and exit.
  ```

i.e.

```
$ transpiler-mate --dry-run --auth-token=<ZENODO_TOKEN> ./docs/pattern-1.cwl

2025-10-09 16:24:35.965 | INFO     | transpiler_mate.cli:main:55 - Started at: 2025-10-09T16:24:35.965
2025-10-09 16:24:35.965 | DEBUG    | transpiler_mate.metadata:__init__:55 - Loading raw document from ./docs/pattern-1.cwl...
2025-10-09 16:24:35.971 | DEBUG    | transpiler_mate.metadata:__init__:62 - Reading the input dictionary and extracting Schema.org metadata in JSON-LD format...
2025-10-09 16:24:35.972 | DEBUG    | transpiler_mate.metadata:__init__:72 - Schema.org metadata successfully extracted in in JSON-LD format!
2025-10-09 16:24:35.973 | DEBUG    | transpiler_mate.metadata:update:89 - JSON-LD format compacted metadata ready to be merged to the original raw CWL document...
2025-10-09 16:24:35.974 | DEBUG    | transpiler_mate.metadata:update:100 - JSON-LD format compacted metadata merged to the original document
2025-10-09 16:24:35.977 | INFO     | transpiler_mate.metadata:update:104 - JSON-LD format compacted metadata merged to the original './docs/pattern-1.cwl' document
2025-10-09 16:24:35.977 | INFO     | transpiler_mate.cli:main:64 - Interacting with Invenio server at https://sandbox.zenodo.org)
2025-10-09 16:24:35.977 | DEBUG    | transpiler_mate.invenio:__init__:102 - Setting up the HTTP logger...
2025-10-09 16:24:36.014 | DEBUG    | transpiler_mate.invenio:__init__:104 - HTTP logger correctly setup
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate.invenio:create_or_update_process:214 - 'identifier' key not found in source document, reserving a DOI...
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/json
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 2
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:36.014 | WARNING  | transpiler_mate:wrapper:52 - {}
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:70 - < 201 Created
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:36 GMT
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 2241
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: "4"
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 999
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 60
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < set-cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ; Expires=Thu, 16 Oct 2025 14:24:36 GMT; Max-Age=604800; Secure; Path=/; SameSite=Lax, 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; path=/; HttpOnly; Secure; SameSite=None
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: f07b95af77de4f24df04031afd4770b9
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:36.482267+00:00", "modified": "2025-10-09T14:24:36.595373+00:00", "id": 346365, "conceptrecid": "346364", "metadata": {"access_right": "open", "relations": {"version": [{"index": 0, "is_last": false, "parent": {"pid_type": "recid", "pid_value": "346364"}}]}}, "title": "", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft", "self_html": "https://sandbox.zenodo.org/uploads/346365", "preview_html": "https://sandbox.zenodo.org/records/346365?preview=1", "reserve_doi": "https://sandbox.zenodo.org/api/records/346365/draft/pids/doi", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/draft:346365/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/draft:346365/sequence/default", "files": "https://sandbox.zenodo.org/api/records/346365/draft/files", "media_files": "https://sandbox.zenodo.org/api/records/346365/draft/media-files", "archive": "https://sandbox.zenodo.org/api/records/346365/draft/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/346365/draft/media-files-archive", "versions": "https://sandbox.zenodo.org/api/records/346365/versions", "record": "https://sandbox.zenodo.org/api/records/346365", "record_html": "https://sandbox.zenodo.org/records/346365", "publish": "https://sandbox.zenodo.org/api/records/346365/draft/actions/publish", "review": "https://sandbox.zenodo.org/api/records/346365/draft/review", "access_links": "https://sandbox.zenodo.org/api/records/346365/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/346365/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/346365/access/users", "access_request": "https://sandbox.zenodo.org/api/records/346365/access/request", "access": "https://sandbox.zenodo.org/api/records/346365/access", "communities": "https://sandbox.zenodo.org/api/records/346365/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/346365/communities-suggestions", "requests": "https://sandbox.zenodo.org/api/records/346365/requests"}, "updated": "2025-10-09T14:24:36.595373+00:00", "recid": "346365", "revision": 4, "files": [], "owners": [{"id": "48746"}], "status": "draft", "state": "unsubmitted", "submitted": false}
2025-10-09 16:24:36.745 | SUCCESS  | transpiler_mate.invenio:create_or_update_process:223 - Successfully reserved a draft record with ID: 346365
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/346365/draft/pids/doi
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:36.745 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:36.746 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:36.746 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:70 - < 201 Created
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:36 GMT
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 2509
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: "6"
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 998
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 60
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 220dca2bd474f2a3aafc7a2db7dcac60
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:37.011 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:36.482267+00:00", "modified": "2025-10-09T14:24:36.848061+00:00", "id": 346365, "conceptrecid": "346364", "doi": "10.5072/zenodo.346365", "doi_url": "https://handle.test.datacite.org/10.5072/zenodo.346365", "metadata": {"doi": "10.5072/zenodo.346365", "access_right": "open", "relations": {"version": [{"index": 0, "is_last": false, "parent": {"pid_type": "recid", "pid_value": "346364"}}]}}, "title": "", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft", "self_html": "https://sandbox.zenodo.org/uploads/346365", "preview_html": "https://sandbox.zenodo.org/records/346365?preview=1", "doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "self_doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "reserve_doi": "https://sandbox.zenodo.org/api/records/346365/draft/pids/doi", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/draft:346365/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/draft:346365/sequence/default", "files": "https://sandbox.zenodo.org/api/records/346365/draft/files", "media_files": "https://sandbox.zenodo.org/api/records/346365/draft/media-files", "archive": "https://sandbox.zenodo.org/api/records/346365/draft/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/346365/draft/media-files-archive", "versions": "https://sandbox.zenodo.org/api/records/346365/versions", "record": "https://sandbox.zenodo.org/api/records/346365", "record_html": "https://sandbox.zenodo.org/records/346365", "publish": "https://sandbox.zenodo.org/api/records/346365/draft/actions/publish", "review": "https://sandbox.zenodo.org/api/records/346365/draft/review", "access_links": "https://sandbox.zenodo.org/api/records/346365/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/346365/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/346365/access/users", "access_request": "https://sandbox.zenodo.org/api/records/346365/access/request", "access": "https://sandbox.zenodo.org/api/records/346365/access", "communities": "https://sandbox.zenodo.org/api/records/346365/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/346365/communities-suggestions", "requests": "https://sandbox.zenodo.org/api/records/346365/requests"}, "updated": "2025-10-09T14:24:36.848061+00:00", "recid": "346365", "revision": 6, "files": [], "owners": [{"id": "48746"}], "status": "draft", "state": "unsubmitted", "submitted": false}
2025-10-09 16:24:37.012 | SUCCESS  | transpiler_mate.invenio:create_or_update_process:233 - Successfully reserved a DOI with ID 10.5072/zenodo.346365 (URL: https://handle.test.datacite.org/10.5072/zenodo.346365)
2025-10-09 16:24:37.013 | DEBUG    | transpiler_mate.metadata:update:89 - JSON-LD format compacted metadata ready to be merged to the original raw CWL document...
2025-10-09 16:24:37.013 | DEBUG    | transpiler_mate.metadata:update:100 - JSON-LD format compacted metadata merged to the original document
2025-10-09 16:24:37.017 | INFO     | transpiler_mate.metadata:update:104 - JSON-LD format compacted metadata merged to the original './docs/pattern-1.cwl' document
2025-10-09 16:24:37.018 | INFO     | transpiler_mate.invenio:_finalize:135 - Drafting file upload [pattern-1_v1.0.0.cwl, codemeta.json] to Record '346365'...
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/346365/draft/files
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/json
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 180
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:37.019 | WARNING  | transpiler_mate:wrapper:52 - [{"key":"pattern-1_v1.0.0.cwl","size":3738,"checksum":"md5:7e479156b3545479cefae3e95c42ddbf"},{"key":"codemeta.json","size":2026,"checksum":"md5:f586238a27856ecdb6e9cb24da286f36"}]
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:70 - < 201 Created
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:37 GMT
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1378
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 997
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 420a68484d9e01efff0a2ece492770d1
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate:wrapper:79 - {"enabled": true, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files", "archive": "https://sandbox.zenodo.org/api/records/346365/draft/files-archive"}, "entries": [{"created": "2025-10-09T14:24:37.086655+00:00", "updated": "2025-10-09T14:24:37.091875+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/commit"}, "key": "pattern-1_v1.0.0.cwl", "checksum": "md5:7e479156b3545479cefae3e95c42ddbf", "size": 3738, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-09T14:24:37.097350+00:00", "updated": "2025-10-09T14:24:37.101298+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/commit"}, "key": "codemeta.json", "checksum": "md5:f586238a27856ecdb6e9cb24da286f36", "size": 2026, "transfer": {"type": "L"}, "status": "pending"}], "default_preview": null, "order": []}
2025-10-09 16:24:37.215 | SUCCESS  | transpiler_mate.invenio:_finalize:147 - File upload pattern-1_v1.0.0.cwl, codemeta.json drafted to Record '346365'
2025-10-09 16:24:37.215 | INFO     | transpiler_mate.invenio:_finalize:150 - Uploading file content 'pattern-1_v1.0.0.cwl)' to Record '346365'...
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/content
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 3738
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:37.216 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-09 16:24:37.418 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:37 GMT
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 587
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 996
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 82105e23a551d3ca844930c8f81e8a93
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:37.086655+00:00", "updated": "2025-10-09T14:24:37.091875+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/commit"}, "key": "pattern-1_v1.0.0.cwl", "checksum": "md5:7e479156b3545479cefae3e95c42ddbf", "size": 3738, "transfer": {"type": "L"}, "status": "pending"}
2025-10-09 16:24:37.419 | SUCCESS  | transpiler_mate.invenio:_finalize:164 - File content pattern-1_v1.0.0.cwl uploaded to Record 346365
2025-10-09 16:24:37.419 | INFO     | transpiler_mate.invenio:_finalize:166 - Completing file upload pattern-1_v1.0.0.cwl] to Record '346365'...
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/commit
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:37.419 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:37 GMT
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 995
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 096a4b5336a7403eb430a7c0a2cfb362
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:37.086655+00:00", "updated": "2025-10-09T14:24:37.493573+00:00", "mimetype": "application/octet-stream", "version_id": "e1299a5d-d77f-4914-9c2f-073e7590c2dc", "file_id": "dc2ddb5c-e9ba-4991-8b56-f21248aff7ad", "bucket_id": "c37308d8-5e70-4ca9-84ec-115562fb8d57", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/commit"}, "key": "pattern-1_v1.0.0.cwl", "checksum": "md5:7e479156b3545479cefae3e95c42ddbf", "size": 3738, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-09 16:24:37.625 | SUCCESS  | transpiler_mate.invenio:_finalize:174 - File upload pattern-1_v1.0.0.cwl to Record '346365' completed
2025-10-09 16:24:37.625 | INFO     | transpiler_mate.invenio:_finalize:150 - Uploading file content 'codemeta.json)' to Record '346365'...
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/content
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 2026
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:37.626 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:37 GMT
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 559
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 994
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: a085b9d1c75538ecfe538881a459b5dd
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:37.097350+00:00", "updated": "2025-10-09T14:24:37.101298+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/commit"}, "key": "codemeta.json", "checksum": "md5:f586238a27856ecdb6e9cb24da286f36", "size": 2026, "transfer": {"type": "L"}, "status": "pending"}
2025-10-09 16:24:37.828 | SUCCESS  | transpiler_mate.invenio:_finalize:164 - File content codemeta.json uploaded to Record 346365
2025-10-09 16:24:37.828 | INFO     | transpiler_mate.invenio:_finalize:166 - Completing file upload codemeta.json] to Record '346365'...
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/commit
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:37.828 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:37.829 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:38.016 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:37 GMT
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 993
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: fcd025ca80e87858e41c7551db5a8b13
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:37.097350+00:00", "updated": "2025-10-09T14:24:37.904762+00:00", "mimetype": "application/json", "version_id": "d32b8b7c-6e26-4787-87a9-7cf41e3609c1", "file_id": "a2d5f1bf-0b50-4f79-b6c8-6bbd643c3dc6", "bucket_id": "c37308d8-5e70-4ca9-84ec-115562fb8d57", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json", "content": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/content", "commit": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/commit"}, "key": "codemeta.json", "checksum": "md5:f586238a27856ecdb6e9cb24da286f36", "size": 2026, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-09 16:24:38.017 | SUCCESS  | transpiler_mate.invenio:_finalize:174 - File upload codemeta.json to Record '346365' completed
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/346365/draft
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/json
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 693
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:38.018 | WARNING  | transpiler_mate:wrapper:52 - {"access":{"record":"public","files":"public"},"files":{"enabled":true},"metadata":{"resource_type":{"id":"workflow"},"title":"Water bodies detection based on NDWI and the otsu threshold","publication_date":"2025-10-09","creators":[{"person_or_org":{"type":"personal","given_name":"Fabrice","family_name":"Brito","name":"Brito, Fabrice"},"affiliations":[{"name":"Terradue Srl"}]},{"person_or_org":{"type":"personal","given_name":"Simone","family_name":"Tripodi","name":"Tripodi, Simone"},"affiliations":[{"name":"Terradue Srl"}]}],"publisher":"Terradue Srl","description":"Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition","version":"1.0.0"}}
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:38 GMT
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: W/"8"
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 992
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: fc73cf0548c9db3da3bec1a779a2a028
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:38.294 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:36.482267+00:00", "modified": "2025-10-09T14:24:38.164560+00:00", "id": 346365, "conceptrecid": "346364", "doi": "10.5072/zenodo.346365", "doi_url": "https://handle.test.datacite.org/10.5072/zenodo.346365", "metadata": {"title": "Water bodies detection based on NDWI and the otsu threshold", "doi": "10.5072/zenodo.346365", "publication_date": "2025-10-09", "description": "Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition", "access_right": "open", "creators": [{"name": "Brito, Fabrice", "affiliation": "Terradue Srl"}, {"name": "Tripodi, Simone", "affiliation": "Terradue Srl"}], "version": "1.0.0", "resource_type": {"title": "Workflow", "type": "workflow"}, "relations": {"version": [{"index": 0, "is_last": false, "parent": {"pid_type": "recid", "pid_value": "346364"}}]}}, "title": "Water bodies detection based on NDWI and the otsu threshold", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft", "self_html": "https://sandbox.zenodo.org/uploads/346365", "preview_html": "https://sandbox.zenodo.org/records/346365?preview=1", "doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "self_doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "reserve_doi": "https://sandbox.zenodo.org/api/records/346365/draft/pids/doi", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/draft:346365/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/draft:346365/sequence/default", "files": "https://sandbox.zenodo.org/api/records/346365/draft/files", "media_files": "https://sandbox.zenodo.org/api/records/346365/draft/media-files", "archive": "https://sandbox.zenodo.org/api/records/346365/draft/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/346365/draft/media-files-archive", "versions": "https://sandbox.zenodo.org/api/records/346365/versions", "record": "https://sandbox.zenodo.org/api/records/346365", "record_html": "https://sandbox.zenodo.org/records/346365", "publish": "https://sandbox.zenodo.org/api/records/346365/draft/actions/publish", "review": "https://sandbox.zenodo.org/api/records/346365/draft/review", "access_links": "https://sandbox.zenodo.org/api/records/346365/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/346365/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/346365/access/users", "access_request": "https://sandbox.zenodo.org/api/records/346365/access/request", "access": "https://sandbox.zenodo.org/api/records/346365/access", "communities": "https://sandbox.zenodo.org/api/records/346365/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/346365/communities-suggestions", "requests": "https://sandbox.zenodo.org/api/records/346365/requests"}, "updated": "2025-10-09T14:24:38.164560+00:00", "recid": "346365", "revision": 8, "files": [{"id": "dc2ddb5c-e9ba-4991-8b56-f21248aff7ad", "key": "pattern-1_v1.0.0.cwl", "size": 3738, "checksum": "md5:7e479156b3545479cefae3e95c42ddbf", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/pattern-1_v1.0.0.cwl/content"}}, {"id": "a2d5f1bf-0b50-4f79-b6c8-6bbd643c3dc6", "key": "codemeta.json", "size": 2026, "checksum": "md5:f586238a27856ecdb6e9cb24da286f36", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/draft/files/codemeta.json/content"}}], "owners": [{"id": "48746"}], "status": "draft", "state": "unsubmitted", "submitted": false}
2025-10-09 16:24:38.295 | SUCCESS  | transpiler_mate.invenio:_finalize:191 - Draft Record '346365' metadata updated!
2025-10-09 16:24:38.295 | INFO     | transpiler_mate.invenio:_finalize:193 - Publishing the Draft Record '346365'...
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/346365/draft/actions/publish
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <ZENODO_TOKEN>
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: 04f20c86f07421a9ec0f9d5ba4be544f=e56600676a18df06a91f0e841bff5b8f; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MDAxOTg3NiwiZXhwIjoxNzYwMTA2Mjc2fQ.Imsxc2ZIdFF1dGtjOHp6MHNyRDhGZFJ5SzJUQktIY2MzIg.EIEYCkeYNe6Rp_xdHtynIpGTa8AvZkMdGik21rfZV9N52EbeW-MPSu5RpCaTcdrjQTR9d5d8hZLwtRhsfP1IFQ
2025-10-09 16:24:38.295 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:70 - < 202 Accepted
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Thu, 09 Oct 2025 14:24:39 GMT
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 4043
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: "4"
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 991
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1760019937
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-09T14:24:38.442546+00:00", "modified": "2025-10-09T14:24:38.826080+00:00", "id": 346365, "conceptrecid": "346364", "doi": "10.5072/zenodo.346365", "conceptdoi": "10.5072/zenodo.346364", "doi_url": "https://handle.test.datacite.org/10.5072/zenodo.346365", "metadata": {"title": "Water bodies detection based on NDWI and the otsu threshold", "doi": "10.5072/zenodo.346365", "publication_date": "2025-10-09", "description": "Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition", "access_right": "open", "creators": [{"name": "Brito, Fabrice", "affiliation": "Terradue Srl"}, {"name": "Tripodi, Simone", "affiliation": "Terradue Srl"}], "version": "1.0.0", "resource_type": {"title": "Workflow", "type": "workflow"}, "relations": {"version": [{"index": 0, "is_last": true, "parent": {"pid_type": "recid", "pid_value": "346364"}}]}}, "title": "Water bodies detection based on NDWI and the otsu threshold", "links": {"self": "https://sandbox.zenodo.org/api/records/346365", "self_html": "https://sandbox.zenodo.org/records/346365", "preview_html": "https://sandbox.zenodo.org/records/346365?preview=1", "doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "self_doi": "https://handle.test.datacite.org/10.5072/zenodo.346365", "self_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.346365", "reserve_doi": "https://sandbox.zenodo.org/api/records/346365/draft/pids/doi", "parent": "https://sandbox.zenodo.org/api/records/346364", "parent_html": "https://sandbox.zenodo.org/records/346364", "parent_doi": "https://handle.test.datacite.org/10.5072/zenodo.346364", "parent_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.346364", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/record:346365/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/record:346365/sequence/default", "files": "https://sandbox.zenodo.org/api/records/346365/files", "media_files": "https://sandbox.zenodo.org/api/records/346365/media-files", "archive": "https://sandbox.zenodo.org/api/records/346365/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/346365/media-files-archive", "latest": "https://sandbox.zenodo.org/api/records/346365/versions/latest", "latest_html": "https://sandbox.zenodo.org/records/346365/latest", "versions": "https://sandbox.zenodo.org/api/records/346365/versions", "draft": "https://sandbox.zenodo.org/api/records/346365/draft", "access_links": "https://sandbox.zenodo.org/api/records/346365/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/346365/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/346365/access/users", "access_request": "https://sandbox.zenodo.org/api/records/346365/access/request", "access": "https://sandbox.zenodo.org/api/records/346365/access", "communities": "https://sandbox.zenodo.org/api/records/346365/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/346365/communities-suggestions", "request_deletion": "https://sandbox.zenodo.org/api/records/346365/request-deletion", "requests": "https://sandbox.zenodo.org/api/records/346365/requests"}, "updated": "2025-10-09T14:24:38.826080+00:00", "recid": "346365", "revision": 4, "files": [{"id": "dc2ddb5c-e9ba-4991-8b56-f21248aff7ad", "key": "pattern-1_v1.0.0.cwl", "size": 3738, "checksum": "md5:7e479156b3545479cefae3e95c42ddbf", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/files/pattern-1_v1.0.0.cwl/content"}}, {"id": "a2d5f1bf-0b50-4f79-b6c8-6bbd643c3dc6", "key": "codemeta.json", "size": 2026, "checksum": "md5:f586238a27856ecdb6e9cb24da286f36", "links": {"self": "https://sandbox.zenodo.org/api/records/346365/files/codemeta.json/content"}}], "swh": {}, "owners": [{"id": "48746"}], "status": "published", "stats": {"downloads": 0, "unique_downloads": 0, "views": 0, "unique_views": 0, "version_downloads": 0, "version_unique_downloads": 0, "version_unique_views": 0, "version_views": 0}, "state": "done", "submitted": true}
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate.invenio:_finalize:200 - Draft Record '346365' metadata updated!
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate.cli:main:76 - Record available on 'https://sandbox.zenodo.org/records/346365'
2025-10-09 16:24:39.366 | INFO     | transpiler_mate.cli:main:78 - ------------------------------------------------------------------------
2025-10-09 16:24:39.366 | SUCCESS  | transpiler_mate.cli:main:79 - BUILD SUCCESS
2025-10-09 16:24:39.366 | INFO     | transpiler_mate.cli:main:80 - ------------------------------------------------------------------------
2025-10-09 16:24:39.366 | INFO     | transpiler_mate.cli:main:82 - Total time: 3.4016 seconds
2025-10-09 16:24:39.366 | INFO     | transpiler_mate.cli:main:83 - Finished at: 2025-10-09T16:24:39.366
```
