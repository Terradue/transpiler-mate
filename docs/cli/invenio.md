# Publish a CWL Workflow on an Invenio instance

```
$ transpiler-mate invenio-publish --help
Usage: transpiler-mate invenio-publish [OPTIONS] SOURCE

  Publishes the input CWL to an Invenio instance.

Options:
  --base-url TEXT    The Invenio server base URL  [required]
  --auth-token TEXT  The Invenio Access token  [required]
  --attach PATH
  --help
```

> [!NOTE]  
> The `--auth-token` option can be omitted if the `INVENIO_AUTH_TOKEN` environment variable is set, i.e.

```
export INVENIO_AUTH_TOKEN=<INVENIO_AUTH_TOKEN>
```

Invocation will look alike:

```
$ transpiler-mate invenio-publish \
  --base-url=https://sandbox.zenodo.org/ \
  --auth-token=<INVENIO_AUTH_TOKEN> \
  --attach=./codemeta.json \
  --attach=./record.json \
  --attach=/path/to/state.png \
  --attach=/path/to/sequence.png \
  --attach=/path/to/class.png 
  --attach=/path/to/component.png 
  --attach=/path/to/activity.png \
  /path/to/pattern-1.cwl

2025-10-29 15:42:57.902 | INFO     | transpiler_mate.cli:wrapper:32 - Started at: 2025-10-29T15:42:57.902
2025-10-29 15:42:57.903 | DEBUG    | transpiler_mate.metadata:__init__:51 - Loading raw document from /path/to/pattern-1.cwl...
2025-10-29 15:42:58.521 | INFO     | transpiler_mate.cli:invenio_publish:101 - Interacting with Invenio server at https://sandbox.zenodo.org/)
2025-10-29 15:42:58.603 | DEBUG    | transpiler_mate.invenio:__init__:120 - Setting up the HTTP logger...
2025-10-29 15:42:58.636 | DEBUG    | transpiler_mate.invenio:__init__:122 - HTTP logger correctly setup
2025-10-29 15:42:58.636 | INFO     | transpiler_mate.invenio:create_or_update_process:276 - Identifier 10.5072/zenodo.393402 already assigned to /path/to/pattern-1.cwl
2025-10-29 15:42:58.636 | INFO     | transpiler_mate.invenio:create_or_update_process:280 - Creating a new version for already existing Record 393402
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393402/versions
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:42:58.636 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:70 - < 201 Created
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:42:59 GMT
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 3031
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: "5"
2025-10-29 15:42:59.261 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 999
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 60
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < set-cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; Expires=Wed, 05 Nov 2025 14:42:59 GMT; Max-Age=604800; Secure; Path=/; SameSite=Lax, 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83; path=/; HttpOnly; Secure; SameSite=None
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 4b2e7823032a853f5017cdc85dc0dc59
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:42:59.262 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.079123+00:00", "modified": "2025-10-29T14:42:59.172467+00:00", "id": 393433, "conceptrecid": "393401", "conceptdoi": "10.5072/zenodo.393401", "metadata": {"title": "Water bodies detection based on NDWI and the otsu threshold", "description": "Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition", "access_right": "open", "creators": [{"name": "Brito, Fabrice", "affiliation": "Terradue (Italy)", "orcid": "0009-0000-1342-9736"}, {"name": "Re, Alice", "affiliation": "Terradue (Italy)", "orcid": "0000-0001-7068-5533"}, {"name": "Tripodi, Simone", "affiliation": "Terradue (Italy)", "orcid": "0009-0006-2063-618X"}], "resource_type": {"title": "Workflow", "type": "workflow"}, "relations": {"version": [{"index": 3, "is_last": false, "parent": {"pid_type": "recid", "pid_value": "393401"}}]}}, "title": "Water bodies detection based on NDWI and the otsu threshold", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft", "self_html": "https://sandbox.zenodo.org/uploads/393433", "preview_html": "https://sandbox.zenodo.org/records/393433?preview=1", "reserve_doi": "https://sandbox.zenodo.org/api/records/393433/draft/pids/doi", "parent_doi": "https://handle.test.datacite.org/10.5072/zenodo.393401", "parent_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.393401", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/draft:393433/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/draft:393433/sequence/default", "files": "https://sandbox.zenodo.org/api/records/393433/draft/files", "media_files": "https://sandbox.zenodo.org/api/records/393433/draft/media-files", "archive": "https://sandbox.zenodo.org/api/records/393433/draft/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/393433/draft/media-files-archive", "versions": "https://sandbox.zenodo.org/api/records/393433/versions", "record": "https://sandbox.zenodo.org/api/records/393433", "record_html": "https://sandbox.zenodo.org/records/393433", "publish": "https://sandbox.zenodo.org/api/records/393433/draft/actions/publish", "review": "https://sandbox.zenodo.org/api/records/393433/draft/review", "access_links": "https://sandbox.zenodo.org/api/records/393433/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/393433/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/393433/access/users", "access_request": "https://sandbox.zenodo.org/api/records/393433/access/request", "access": "https://sandbox.zenodo.org/api/records/393433/access", "communities": "https://sandbox.zenodo.org/api/records/393433/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/393433/communities-suggestions", "requests": "https://sandbox.zenodo.org/api/records/393433/requests"}, "updated": "2025-10-29T14:42:59.172467+00:00", "recid": "393433", "revision": 5, "files": [], "owners": [{"id": "48746"}], "status": "draft", "state": "unsubmitted", "submitted": false}
2025-10-29 15:42:59.262 | INFO     | transpiler_mate.invenio:create_or_update_process:289 - New version 393433 for already existing Record 393402 created!
2025-10-29 15:42:59.270 | INFO     | transpiler_mate.invenio:_finalize:170 - Drafting file upload [pattern-1.cwl, codemeta.json, record.json, state.png, sequence.png, class.png, component.png, activity.png] to Record '393433'...
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/json
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 808
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:42:59.272 | WARNING  | transpiler_mate:wrapper:52 - [{"key":"pattern-1_v4.0.0.cwl","size":4792,"checksum":"md5:12beba8d3612216a01021c5f0031b4aa"},{"key":"pattern-1_codemeta_v4.0.0.json","size":3334,"checksum":"md5:7a924cad592dba87a1015440448c0792"},{"key":"pattern-1_record_v4.0.0.json","size":2095,"checksum":"md5:fbe6af0ed8c4ca8a09d407178734ba85"},{"key":"pattern-1_state_v4.0.0.png","size":19445,"checksum":"md5:2064702ca8651a3185872e15565530b9"},{"key":"pattern-1_sequence_v4.0.0.png","size":42021,"checksum":"md5:4c47b8ece5f4426b437177cb32d2372f"},{"key":"pattern-1_class_v4.0.0.png","size":58961,"checksum":"md5:489df77f1594d1782d1b2120428a1dba"},{"key":"pattern-1_component_v4.0.0.png","size":24170,"checksum":"md5:ee26069537a8fd04972d83fb7ec7faaf"},{"key":"pattern-1_activity_v4.0.0.png","size":11299,"checksum":"md5:0ed15555fc828446c30d264dcf7433a1"}]
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:70 - < 201 Created
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:42:59 GMT
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 7267
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 998
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 60
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:42:59.568 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: fa555af2614ea25c48a3a39bc871bf4c
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate:wrapper:79 - {"enabled": true, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files", "archive": "https://sandbox.zenodo.org/api/records/393433/draft/files-archive"}, "entries": [{"created": "2025-10-29T14:42:59.549808+00:00", "updated": "2025-10-29T14:42:59.552786+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/commit"}, "key": "pattern-1_v4.0.0.cwl", "checksum": "md5:12beba8d3612216a01021c5f0031b4aa", "size": 4792, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.556417+00:00", "updated": "2025-10-29T14:42:59.558630+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/commit"}, "key": "pattern-1_codemeta_v4.0.0.json", "checksum": "md5:7a924cad592dba87a1015440448c0792", "size": 3334, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.562247+00:00", "updated": "2025-10-29T14:42:59.564576+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/commit"}, "key": "pattern-1_record_v4.0.0.json", "checksum": "md5:fbe6af0ed8c4ca8a09d407178734ba85", "size": 2095, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.568423+00:00", "updated": "2025-10-29T14:42:59.570809+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_state_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_state_v4.0.0.png", "checksum": "md5:2064702ca8651a3185872e15565530b9", "size": 19445, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.574305+00:00", "updated": "2025-10-29T14:42:59.576594+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_sequence_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_sequence_v4.0.0.png", "checksum": "md5:4c47b8ece5f4426b437177cb32d2372f", "size": 42021, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.580342+00:00", "updated": "2025-10-29T14:42:59.582630+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_class_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_class_v4.0.0.png", "checksum": "md5:489df77f1594d1782d1b2120428a1dba", "size": 58961, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.586016+00:00", "updated": "2025-10-29T14:42:59.588176+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_component_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_component_v4.0.0.png", "checksum": "md5:ee26069537a8fd04972d83fb7ec7faaf", "size": 24170, "transfer": {"type": "L"}, "status": "pending"}, {"created": "2025-10-29T14:42:59.591574+00:00", "updated": "2025-10-29T14:42:59.593731+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_activity_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_activity_v4.0.0.png", "checksum": "md5:0ed15555fc828446c30d264dcf7433a1", "size": 11299, "transfer": {"type": "L"}, "status": "pending"}], "default_preview": null, "order": []}
2025-10-29 15:42:59.569 | SUCCESS  | transpiler_mate.invenio:_finalize:182 - File upload pattern-1.cwl, codemeta.json, record.json, state.png, sequence.png, class.png, component.png, activity.png drafted to Record '393433'
2025-10-29 15:42:59.569 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'pattern-1.cwl)' to Record '393433'...
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/content
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 4792
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:42:59.569 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:42:59.740 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:42:59 GMT
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 587
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 997
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 60
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: a7d71d243c7455c0e8910849025c37d9
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.549808+00:00", "updated": "2025-10-29T14:42:59.552786+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/commit"}, "key": "pattern-1_v4.0.0.cwl", "checksum": "md5:12beba8d3612216a01021c5f0031b4aa", "size": 4792, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:42:59.741 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content pattern-1.cwl uploaded to Record 393433
2025-10-29 15:42:59.741 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload pattern-1.cwl] to Record '393433'...
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/commit
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:42:59.741 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:00 GMT
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 996
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 1e05a720ef17c9ceb70d22ec41bee762
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.549808+00:00", "updated": "2025-10-29T14:42:59.994354+00:00", "mimetype": "application/octet-stream", "version_id": "154d65e6-ecdb-4aa3-983b-bbaba4c09fc3", "file_id": "9c1e174b-16a4-43e1-bda5-39f6d3d6c000", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/commit"}, "key": "pattern-1_v4.0.0.cwl", "checksum": "md5:12beba8d3612216a01021c5f0031b4aa", "size": 4792, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:42:59.865 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload pattern-1.cwl to Record '393433' completed
2025-10-29 15:42:59.865 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'codemeta.json)' to Record '393433'...
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/content
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 3334
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:42:59.866 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:00 GMT
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 627
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 995
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:00.027 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: f1469de19f22e0396abeb78dbd3ea9cb
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.556417+00:00", "updated": "2025-10-29T14:42:59.558630+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/commit"}, "key": "pattern-1_codemeta_v4.0.0.json", "checksum": "md5:7a924cad592dba87a1015440448c0792", "size": 3334, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:00.028 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content codemeta.json uploaded to Record 393433
2025-10-29 15:43:00.028 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload codemeta.json] to Record '393433'...
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/commit
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:00.028 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:00 GMT
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 994
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 4345e64a4880abd5620b020ad3a5276c
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.556417+00:00", "updated": "2025-10-29T14:43:00.285249+00:00", "mimetype": "application/json", "version_id": "6fa9c540-69a7-40ff-ac2a-69fe87f3d6ac", "file_id": "747064b7-133c-4f02-8ef4-3bd1d75e0f71", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/commit"}, "key": "pattern-1_codemeta_v4.0.0.json", "checksum": "md5:7a924cad592dba87a1015440448c0792", "size": 3334, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:00.148 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload codemeta.json to Record '393433' completed
2025-10-29 15:43:00.148 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'record.json)' to Record '393433'...
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/content
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 2095
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:00.149 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:00.459 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:00 GMT
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 619
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 993
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 1f6d215202229021eba7ea27f893f5e1
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.562247+00:00", "updated": "2025-10-29T14:42:59.564576+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/commit"}, "key": "pattern-1_record_v4.0.0.json", "checksum": "md5:fbe6af0ed8c4ca8a09d407178734ba85", "size": 2095, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:00.460 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content record.json uploaded to Record 393433
2025-10-29 15:43:00.460 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload record.json] to Record '393433'...
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/commit
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:00.460 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:00 GMT
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 992
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 59
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: cfd652b3ff0dfacb0ede2fe1082b117f
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.562247+00:00", "updated": "2025-10-29T14:43:00.728824+00:00", "mimetype": "application/json", "version_id": "5e3bc159-291a-4e76-a5f6-612a5111f16f", "file_id": "9eb17ca1-1bf9-44b8-bcbe-e553b988bef1", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/commit"}, "key": "pattern-1_record_v4.0.0.json", "checksum": "md5:fbe6af0ed8c4ca8a09d407178734ba85", "size": 2095, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:00.738 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload record.json to Record '393433' completed
2025-10-29 15:43:00.738 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'state.png)' to Record '393433'...
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/content
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 19445
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:00.738 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:00.888 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1022
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 991
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: eea3303e2de95efb8a7217dd5480c7c8
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.568423+00:00", "updated": "2025-10-29T14:42:59.570809+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_state_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_state_v4.0.0.png", "checksum": "md5:2064702ca8651a3185872e15565530b9", "size": 19445, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:00.889 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content state.png uploaded to Record 393433
2025-10-29 15:43:00.889 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload state.png] to Record '393433'...
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/commit
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:00.889 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.015 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.015 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 990
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: afcbf56d1884a3e8ba0872d24d940d6a
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.568423+00:00", "updated": "2025-10-29T14:43:01.145822+00:00", "mimetype": "image/png", "version_id": "08495845-c6d5-4f9c-a89b-44813aa5cf71", "file_id": "550005d3-b264-4eaa-bd1c-b13f831c162d", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_state_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_state_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_state_v4.0.0.png", "checksum": "md5:2064702ca8651a3185872e15565530b9", "size": 19445, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:01.016 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload state.png to Record '393433' completed
2025-10-29 15:43:01.016 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'sequence.png)' to Record '393433'...
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/content
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 42021
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.016 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1046
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 989
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: a0fca63bed6ab58dfa28a7eeff02daee
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.574305+00:00", "updated": "2025-10-29T14:42:59.576594+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_sequence_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_sequence_v4.0.0.png", "checksum": "md5:4c47b8ece5f4426b437177cb32d2372f", "size": 42021, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:01.162 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content sequence.png uploaded to Record 393433
2025-10-29 15:43:01.162 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload sequence.png] to Record '393433'...
2025-10-29 15:43:01.162 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/commit
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.163 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 988
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 9383e126b1901906a7c961a6f68e4eae
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.574305+00:00", "updated": "2025-10-29T14:43:01.418819+00:00", "mimetype": "image/png", "version_id": "f3086333-3c2d-4fef-9a8d-0d115e7ea0dd", "file_id": "93c1a0d4-eea8-4f72-ba39-28c734b86d63", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_sequence_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_sequence_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_sequence_v4.0.0.png", "checksum": "md5:4c47b8ece5f4426b437177cb32d2372f", "size": 42021, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:01.352 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload sequence.png to Record '393433' completed
2025-10-29 15:43:01.352 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'class.png)' to Record '393433'...
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/content
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 58961
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.353 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1022
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 987
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.522 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: a5e1ccd1b4815d7a8b47e763106099c9
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.580342+00:00", "updated": "2025-10-29T14:42:59.582630+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_class_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_class_v4.0.0.png", "checksum": "md5:489df77f1594d1782d1b2120428a1dba", "size": 58961, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:01.523 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content class.png uploaded to Record 393433
2025-10-29 15:43:01.523 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload class.png] to Record '393433'...
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/commit
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.523 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:01 GMT
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:01.671 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 986
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 58
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 7ab4ebb034e5b1cfbd9ae9d6e234e1e5
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.580342+00:00", "updated": "2025-10-29T14:43:01.776671+00:00", "mimetype": "image/png", "version_id": "49516147-24ca-45f9-aa25-6c1515aba2cf", "file_id": "879cee3e-2c42-46ce-94be-d55987b52025", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_class_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_class_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_class_v4.0.0.png", "checksum": "md5:489df77f1594d1782d1b2120428a1dba", "size": 58961, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:01.672 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload class.png to Record '393433' completed
2025-10-29 15:43:01.672 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'component.png)' to Record '393433'...
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/content
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 24170
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:01.672 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:01.967 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:01.967 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:01.967 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:02 GMT
2025-10-29 15:43:01.967 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1054
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 985
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: b5f8d4dc4c0b7970e92081ac18fbd9c1
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.586016+00:00", "updated": "2025-10-29T14:42:59.588176+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_component_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_component_v4.0.0.png", "checksum": "md5:ee26069537a8fd04972d83fb7ec7faaf", "size": 24170, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:01.968 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content component.png uploaded to Record 393433
2025-10-29 15:43:01.968 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload component.png] to Record '393433'...
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/commit
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:01.968 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:02 GMT
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 984
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: bfc62d85c1034bb5b2f84931a673f8f1
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.586016+00:00", "updated": "2025-10-29T14:43:02.236957+00:00", "mimetype": "image/png", "version_id": "56506c74-e4e9-41ca-a823-94233e4a3c97", "file_id": "c484928c-7d9f-4b75-8ee8-3c36c868de13", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_component_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_component_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_component_v4.0.0.png", "checksum": "md5:ee26069537a8fd04972d83fb7ec7faaf", "size": 24170, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:02.112 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload component.png to Record '393433' completed
2025-10-29 15:43:02.112 | INFO     | transpiler_mate.invenio:_finalize:185 - Uploading file content 'activity.png)' to Record '393433'...
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/content
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/octet-stream
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 11299
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:02.113 | WARNING  | transpiler_mate:wrapper:54 - [REQUEST BUILT FROM STREAM, OMISSING]
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:02 GMT
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 1046
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 983
2025-10-29 15:43:02.255 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: b3574130a169325874f60c2e7741d122
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.591574+00:00", "updated": "2025-10-29T14:42:59.593731+00:00", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_activity_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_activity_v4.0.0.png", "checksum": "md5:0ed15555fc828446c30d264dcf7433a1", "size": 11299, "transfer": {"type": "L"}, "status": "pending"}
2025-10-29 15:43:02.256 | SUCCESS  | transpiler_mate.invenio:_finalize:199 - File content activity.png uploaded to Record 393433
2025-10-29 15:43:02.256 | INFO     | transpiler_mate.invenio:_finalize:201 - Completing file upload activity.png] to Record '393433'...
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/commit
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:02.256 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:02.398 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:02.398 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:02.398 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:02 GMT
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 982
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 1ffbf1f50eb7945e429e4c2b151e0588
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.591574+00:00", "updated": "2025-10-29T14:43:02.511724+00:00", "mimetype": "image/png", "version_id": "9552467e-cd57-42e6-a9bd-9be9ae7f27a1", "file_id": "3b8872fa-7ebf-4ea2-8b6b-62a5427b12a6", "bucket_id": "2ec34898-4467-4d36-9e1e-1de137da6e89", "metadata": null, "access": {"hidden": false}, "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png", "content": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/content", "commit": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/commit", "iiif_canvas": "https://sandbox.zenodo.org/api/iiif/draft:393433/canvas/pattern-1_activity_v4.0.0.png", "iiif_base": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png", "iiif_info": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/info.json", "iiif_api": "https://sandbox.zenodo.org/api/iiif/draft:393433:pattern-1_activity_v4.0.0.png/full/full/0/default.png"}, "key": "pattern-1_activity_v4.0.0.png", "checksum": "md5:0ed15555fc828446c30d264dcf7433a1", "size": 11299, "transfer": {"type": "L"}, "status": "completed", "storage_class": "L"}
2025-10-29 15:43:02.399 | SUCCESS  | transpiler_mate.invenio:_finalize:209 - File upload activity.png to Record '393433' completed
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:43 - PUT https://sandbox.zenodo.org/api/records/393433/draft
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Content-Type: application/json
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 1080
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:02.399 | WARNING  | transpiler_mate:wrapper:52 - {"access":{"record":"public","files":"public"},"files":{"enabled":true},"metadata":{"resource_type":{"id":"workflow"},"title":"Water bodies detection based on NDWI and the otsu threshold","publication_date":"2025-10-29","creators":[{"person_or_org":{"type":"personal","given_name":"Fabrice","family_name":"Brito","name":"Brito, Fabrice","identifiers":[{"scheme":"orcid","identifier":"0009-0000-1342-9736"}]},"affiliations":[{"id":"0069cx113","name":"Terradue"}]},{"person_or_org":{"type":"personal","given_name":"Alice","family_name":"Re","name":"Re, Alice","identifiers":[{"scheme":"orcid","identifier":"0000-0001-7068-5533"}]},"affiliations":[{"id":"0069cx113","name":"Terradue"}]},{"person_or_org":{"type":"personal","given_name":"Simone","family_name":"Tripodi","name":"Tripodi, Simone","identifiers":[{"scheme":"orcid","identifier":"0009-0006-2063-618X"}]},"affiliations":[{"id":"0069cx113","name":"Terradue"}]}],"publisher":"Terradue Srl","description":"Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition","version":"4.0.0"}}
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:70 - < 200 OK
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:02 GMT
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < transfer-encoding: chunked
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < vary: Accept-Encoding
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: W/"7"
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 981
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 57
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains, max-age=15768000
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < x-request-id: 91454d81e9fd8437765a551ea5a0d6d0
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:74 - < content-encoding: gzip
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:02.785 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:42:59.079123+00:00", "modified": "2025-10-29T14:43:02.737984+00:00", "id": 393433, "conceptrecid": "393401", "conceptdoi": "10.5072/zenodo.393401", "metadata": {"title": "Water bodies detection based on NDWI and the otsu threshold", "publication_date": "2025-10-29", "description": "Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition", "access_right": "open", "creators": [{"name": "Brito, Fabrice", "affiliation": "Terradue (Italy)", "orcid": "0009-0000-1342-9736"}, {"name": "Re, Alice", "affiliation": "Terradue (Italy)", "orcid": "0000-0001-7068-5533"}, {"name": "Tripodi, Simone", "affiliation": "Terradue (Italy)", "orcid": "0009-0006-2063-618X"}], "version": "4.0.0", "resource_type": {"title": "Workflow", "type": "workflow"}, "relations": {"version": [{"index": 3, "is_last": false, "parent": {"pid_type": "recid", "pid_value": "393401"}}]}}, "title": "Water bodies detection based on NDWI and the otsu threshold", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft", "self_html": "https://sandbox.zenodo.org/uploads/393433", "preview_html": "https://sandbox.zenodo.org/records/393433?preview=1", "reserve_doi": "https://sandbox.zenodo.org/api/records/393433/draft/pids/doi", "parent_doi": "https://handle.test.datacite.org/10.5072/zenodo.393401", "parent_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.393401", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/draft:393433/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/draft:393433/sequence/default", "files": "https://sandbox.zenodo.org/api/records/393433/draft/files", "media_files": "https://sandbox.zenodo.org/api/records/393433/draft/media-files", "thumbnails": {"10": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E10,/0/default.jpg", "50": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E50,/0/default.jpg", "100": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E100,/0/default.jpg", "250": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E250,/0/default.jpg", "750": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E750,/0/default.jpg", "1200": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E1200,/0/default.jpg"}, "archive": "https://sandbox.zenodo.org/api/records/393433/draft/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/393433/draft/media-files-archive", "versions": "https://sandbox.zenodo.org/api/records/393433/versions", "record": "https://sandbox.zenodo.org/api/records/393433", "record_html": "https://sandbox.zenodo.org/records/393433", "publish": "https://sandbox.zenodo.org/api/records/393433/draft/actions/publish", "review": "https://sandbox.zenodo.org/api/records/393433/draft/review", "access_links": "https://sandbox.zenodo.org/api/records/393433/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/393433/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/393433/access/users", "access_request": "https://sandbox.zenodo.org/api/records/393433/access/request", "access": "https://sandbox.zenodo.org/api/records/393433/access", "communities": "https://sandbox.zenodo.org/api/records/393433/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/393433/communities-suggestions", "requests": "https://sandbox.zenodo.org/api/records/393433/requests"}, "updated": "2025-10-29T14:43:02.737984+00:00", "recid": "393433", "revision": 7, "files": [{"id": "747064b7-133c-4f02-8ef4-3bd1d75e0f71", "key": "pattern-1_codemeta_v4.0.0.json", "size": 3334, "checksum": "md5:7a924cad592dba87a1015440448c0792", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_codemeta_v4.0.0.json/content"}}, {"id": "9eb17ca1-1bf9-44b8-bcbe-e553b988bef1", "key": "pattern-1_record_v4.0.0.json", "size": 2095, "checksum": "md5:fbe6af0ed8c4ca8a09d407178734ba85", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_record_v4.0.0.json/content"}}, {"id": "550005d3-b264-4eaa-bd1c-b13f831c162d", "key": "pattern-1_state_v4.0.0.png", "size": 19445, "checksum": "md5:2064702ca8651a3185872e15565530b9", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_state_v4.0.0.png/content"}}, {"id": "93c1a0d4-eea8-4f72-ba39-28c734b86d63", "key": "pattern-1_sequence_v4.0.0.png", "size": 42021, "checksum": "md5:4c47b8ece5f4426b437177cb32d2372f", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_sequence_v4.0.0.png/content"}}, {"id": "879cee3e-2c42-46ce-94be-d55987b52025", "key": "pattern-1_class_v4.0.0.png", "size": 58961, "checksum": "md5:489df77f1594d1782d1b2120428a1dba", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_class_v4.0.0.png/content"}}, {"id": "c484928c-7d9f-4b75-8ee8-3c36c868de13", "key": "pattern-1_component_v4.0.0.png", "size": 24170, "checksum": "md5:ee26069537a8fd04972d83fb7ec7faaf", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_component_v4.0.0.png/content"}}, {"id": "9c1e174b-16a4-43e1-bda5-39f6d3d6c000", "key": "pattern-1_v4.0.0.cwl", "size": 4792, "checksum": "md5:12beba8d3612216a01021c5f0031b4aa", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_v4.0.0.cwl/content"}}, {"id": "3b8872fa-7ebf-4ea2-8b6b-62a5427b12a6", "key": "pattern-1_activity_v4.0.0.png", "size": 11299, "checksum": "md5:0ed15555fc828446c30d264dcf7433a1", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/draft/files/pattern-1_activity_v4.0.0.png/content"}}], "owners": [{"id": "48746"}], "status": "draft", "state": "unsubmitted", "submitted": false}
2025-10-29 15:43:02.786 | SUCCESS  | transpiler_mate.invenio:_finalize:226 - Draft Record '393433' metadata updated!
2025-10-29 15:43:02.786 | INFO     | transpiler_mate.invenio:_finalize:228 - Publishing the Draft Record '393433'...
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:43 - POST https://sandbox.zenodo.org/api/records/393433/draft/actions/publish
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Host: sandbox.zenodo.org
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Content-Length: 0
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Accept: */*
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Accept-Encoding: gzip, deflate
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Connection: keep-alive
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > User-Agent: python-httpx/0.28.1
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Authorization: Bearer <INVENIO_AUTH_TOKEN>
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:47 - > Cookie: csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTc2MTc0ODk3OSwiZXhwIjoxNzYxODM1Mzc5fQ.ImZjQzFSSXlXcE5RdDhTcXFVSUFCS3Q2Q1FkYldRYm05Ig.rYNIWPOC9OcXgymaAcX4CYs_jAYU3UGZViXIQppdrdByjVWzHVkeI0EJY5epF9lyLfbm2lmIaraiiiZ_5WQleA; 04f20c86f07421a9ec0f9d5ba4be544f=55542f39350aac4f858e1c881c1f2e83
2025-10-29 15:43:02.786 | WARNING  | transpiler_mate:wrapper:49 - >
2025-10-29 15:43:04.116 | SUCCESS  | transpiler_mate:wrapper:70 - < 202 Accepted
2025-10-29 15:43:04.116 | SUCCESS  | transpiler_mate:wrapper:74 - < server: nginx
2025-10-29 15:43:04.116 | SUCCESS  | transpiler_mate:wrapper:74 - < date: Wed, 29 Oct 2025 14:43:04 GMT
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < content-type: application/json
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < content-length: 6614
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < etag: "4"
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-limit: 1000
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-remaining: 980
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-ratelimit-reset: 1761749040
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < retry-after: 55
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < permissions-policy: interest-cohort=()
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-frame-options: sameorigin
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-xss-protection: 1; mode=block
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < x-content-type-options: nosniff
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < content-security-policy: default-src 'self' fonts.googleapis.com *.gstatic.com data: 'unsafe-inline' 'unsafe-eval' blob: zenodo-broker.web.cern.ch zenodo-broker-qa.web.cern.ch maxcdn.bootstrapcdn.com cdnjs.cloudflare.com ajax.googleapis.com webanalytics.web.cern.ch
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < strict-transport-security: max-age=31556926; includeSubDomains
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < referrer-policy: strict-origin-when-cross-origin
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-allow-origin: *
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:74 - < access-control-expose-headers: Content-Type, ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:76 - 
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate:wrapper:79 - {"created": "2025-10-29T14:43:03.111230+00:00", "modified": "2025-10-29T14:43:03.728825+00:00", "id": 393433, "conceptrecid": "393401", "doi": "10.5072/zenodo.393433", "conceptdoi": "10.5072/zenodo.393401", "doi_url": "https://handle.test.datacite.org/10.5072/zenodo.393433", "metadata": {"title": "Water bodies detection based on NDWI and the otsu threshold", "doi": "10.5072/zenodo.393433", "publication_date": "2025-10-29", "description": "Water bodies detection based on NDWI and otsu threshold applied to a single Landsat-8/9 acquisition", "access_right": "open", "creators": [{"name": "Brito, Fabrice", "affiliation": "Terradue (Italy)", "orcid": "0009-0000-1342-9736"}, {"name": "Re, Alice", "affiliation": "Terradue (Italy)", "orcid": "0000-0001-7068-5533"}, {"name": "Tripodi, Simone", "affiliation": "Terradue (Italy)", "orcid": "0009-0006-2063-618X"}], "version": "4.0.0", "resource_type": {"title": "Workflow", "type": "workflow"}, "relations": {"version": [{"index": 3, "is_last": true, "parent": {"pid_type": "recid", "pid_value": "393401"}}]}}, "title": "Water bodies detection based on NDWI and the otsu threshold", "links": {"self": "https://sandbox.zenodo.org/api/records/393433", "self_html": "https://sandbox.zenodo.org/records/393433", "preview_html": "https://sandbox.zenodo.org/records/393433?preview=1", "doi": "https://handle.test.datacite.org/10.5072/zenodo.393433", "self_doi": "https://handle.test.datacite.org/10.5072/zenodo.393433", "self_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.393433", "reserve_doi": "https://sandbox.zenodo.org/api/records/393433/draft/pids/doi", "parent": "https://sandbox.zenodo.org/api/records/393401", "parent_html": "https://sandbox.zenodo.org/records/393401", "parent_doi": "https://handle.test.datacite.org/10.5072/zenodo.393401", "parent_doi_html": "https://sandbox.zenodo.org/doi/10.5072/zenodo.393401", "self_iiif_manifest": "https://sandbox.zenodo.org/api/iiif/record:393433/manifest", "self_iiif_sequence": "https://sandbox.zenodo.org/api/iiif/record:393433/sequence/default", "files": "https://sandbox.zenodo.org/api/records/393433/files", "media_files": "https://sandbox.zenodo.org/api/records/393433/media-files", "thumbnails": {"10": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E10,/0/default.jpg", "50": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E50,/0/default.jpg", "100": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E100,/0/default.jpg", "250": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E250,/0/default.jpg", "750": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E750,/0/default.jpg", "1200": "https://sandbox.zenodo.org/api/iiif/record:393433:pattern-1_state_v4.0.0.png/full/%5E1200,/0/default.jpg"}, "archive": "https://sandbox.zenodo.org/api/records/393433/files-archive", "archive_media": "https://sandbox.zenodo.org/api/records/393433/media-files-archive", "latest": "https://sandbox.zenodo.org/api/records/393433/versions/latest", "latest_html": "https://sandbox.zenodo.org/records/393433/latest", "versions": "https://sandbox.zenodo.org/api/records/393433/versions", "draft": "https://sandbox.zenodo.org/api/records/393433/draft", "access_links": "https://sandbox.zenodo.org/api/records/393433/access/links", "access_grants": "https://sandbox.zenodo.org/api/records/393433/access/grants", "access_users": "https://sandbox.zenodo.org/api/records/393433/access/users", "access_request": "https://sandbox.zenodo.org/api/records/393433/access/request", "access": "https://sandbox.zenodo.org/api/records/393433/access", "communities": "https://sandbox.zenodo.org/api/records/393433/communities", "communities-suggestions": "https://sandbox.zenodo.org/api/records/393433/communities-suggestions", "request_deletion": "https://sandbox.zenodo.org/api/records/393433/request-deletion", "file_modification": "https://sandbox.zenodo.org/api/records/393433/file-modification", "requests": "https://sandbox.zenodo.org/api/records/393433/requests"}, "updated": "2025-10-29T14:43:03.728825+00:00", "recid": "393433", "revision": 4, "files": [{"id": "747064b7-133c-4f02-8ef4-3bd1d75e0f71", "key": "pattern-1_codemeta_v4.0.0.json", "size": 3334, "checksum": "md5:7a924cad592dba87a1015440448c0792", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_codemeta_v4.0.0.json/content"}}, {"id": "9eb17ca1-1bf9-44b8-bcbe-e553b988bef1", "key": "pattern-1_record_v4.0.0.json", "size": 2095, "checksum": "md5:fbe6af0ed8c4ca8a09d407178734ba85", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_record_v4.0.0.json/content"}}, {"id": "550005d3-b264-4eaa-bd1c-b13f831c162d", "key": "pattern-1_state_v4.0.0.png", "size": 19445, "checksum": "md5:2064702ca8651a3185872e15565530b9", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_state_v4.0.0.png/content"}}, {"id": "93c1a0d4-eea8-4f72-ba39-28c734b86d63", "key": "pattern-1_sequence_v4.0.0.png", "size": 42021, "checksum": "md5:4c47b8ece5f4426b437177cb32d2372f", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_sequence_v4.0.0.png/content"}}, {"id": "879cee3e-2c42-46ce-94be-d55987b52025", "key": "pattern-1_class_v4.0.0.png", "size": 58961, "checksum": "md5:489df77f1594d1782d1b2120428a1dba", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_class_v4.0.0.png/content"}}, {"id": "c484928c-7d9f-4b75-8ee8-3c36c868de13", "key": "pattern-1_component_v4.0.0.png", "size": 24170, "checksum": "md5:ee26069537a8fd04972d83fb7ec7faaf", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_component_v4.0.0.png/content"}}, {"id": "9c1e174b-16a4-43e1-bda5-39f6d3d6c000", "key": "pattern-1_v4.0.0.cwl", "size": 4792, "checksum": "md5:12beba8d3612216a01021c5f0031b4aa", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_v4.0.0.cwl/content"}}, {"id": "3b8872fa-7ebf-4ea2-8b6b-62a5427b12a6", "key": "pattern-1_activity_v4.0.0.png", "size": 11299, "checksum": "md5:0ed15555fc828446c30d264dcf7433a1", "links": {"self": "https://sandbox.zenodo.org/api/records/393433/files/pattern-1_activity_v4.0.0.png/content"}}], "swh": {}, "owners": [{"id": "48746"}], "status": "published", "stats": {"downloads": 0, "unique_downloads": 0, "views": 0, "unique_views": 0, "version_downloads": 0, "version_unique_downloads": 0, "version_unique_views": 0, "version_views": 0}, "state": "done", "submitted": true}
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate.invenio:_finalize:235 - Draft Record '393433' metadata updated!
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate.cli:invenio_publish:115 - Record available on 'https://sandbox.zenodo.org//records/393433'
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate.cli:wrapper:37 - ------------------------------------------------------------------------
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate.cli:wrapper:38 - SUCCESS
2025-10-29 15:43:04.117 | SUCCESS  | transpiler_mate.cli:wrapper:39 - ------------------------------------------------------------------------
2025-10-29 15:43:04.117 | INFO     | transpiler_mate.cli:wrapper:48 - Total time: 6.2148 seconds
2025-10-29 15:43:04.117 | INFO     | transpiler_mate.cli:wrapper:49 - Finished at: 2025-10-29T15:43:04.117
```
