# OSCAR How-To Video Guides

Human-paced, single-task `1920x1080` screen-recording guides covering every major workflow in **OSCAR 3.11.8** ([`ORNL/oscar`](https://github.com/ORNL/oscar)). Each module starts immediately at `00:00` with the workflow action, runs under 2 minutes, includes embedded `mov_text` soft subtitles plus 4-language (`en`, `es`, `fr`, `el`) standalone `.vtt` / `.srt` caption files, and pairs with a 3-to-4-step sequential reference block.

## Encoding & Playback Profile

| Parameter | Specification |
| --- | --- |
| Hardware Encoder | NVIDIA GeForce RTX 5060 Ti `h264_nvenc` (`High@L4.1`, `avc1`) |
| Container & Color | Universal `.mp4` (`+faststart`), `NV12` / `4:2:0` (`yuv420p`), `BT.709` |
| Compression & GOP | `8 s` forced IDR keyframe interval (`GOP 240 @ 30fps`) + NVENC `p7`/`hq` B-frame skip blocks |
| Resolution & FPS | `1920x1080` (`1080p`) constant `30 FPS` (`CFR`) |
| Captions | Embedded MP4 `mov_text` track + 4-language (`en`, `es`, `fr`, `el`) [`captions/`](captions/) `.vtt` & `.srt` (`232` subtitle files) |

- **Interactive HTML5 Player with Closed Captions:** Open [`index.html`](index.html) locally (or via GitHub Pages) to watch every guide with synchronized WebVTT closed captions.
- **Reproducible NVENC Encoding Script:** [`scripts/encode-nvenc-5060ti.sh`](scripts/encode-nvenc-5060ti.sh) and validator [`scripts/verify-guides.py`](scripts/verify-guides.py).

## Module Index

| # | Workflow Guide | Track | Duration | Size | Captions |
| --- | --- | --- | --- | --- | --- |
| 01 | [Initialize OSCAR Deployment, Admin Credentials & TLS](#01-deployment-init-and-credentials) ([MP4](videos/01-deployment-init-and-credentials.mp4)) | Track A | 28.5s | 587.7 KiB | [VTT](captions/01-deployment-init-and-credentials.vtt) · [SRT](captions/01-deployment-init-and-credentials.srt) |
| 02 | [Upgrade OSCAR in a Clean Release Directory](#02-clean-directory-upgrade) ([MP4](videos/02-clean-directory-upgrade.mp4)) | Track A | 29.5s | 519.6 KiB | [VTT](captions/02-clean-directory-upgrade.vtt) · [SRT](captions/02-clean-directory-upgrade.srt) |
| 03 | [Verify Parquet Cold-Tier Archives & Single-Snapshot Backup](#03-archive-and-snapshot-backup) ([MP4](videos/03-archive-and-snapshot-backup.mp4)) | Track A | 28.5s | 545.2 KiB | [VTT](captions/03-archive-and-snapshot-backup.vtt) · [SRT](captions/03-archive-and-snapshot-backup.srt) |
| 04 | [Configure OSCAR Service Retention & Custom Disposition Codes](#04-admin-oscar-service-and-custom-codes) ([MP4](videos/04-admin-oscar-service-and-custom-codes.mp4)) | Track B | 41.5s | 1040.3 KiB | [VTT](captions/04-admin-oscar-service-and-custom-codes.vtt) · [SRT](captions/04-admin-oscar-service-and-custom-codes.srt) |
| 05 | [Sync Multi-Lane Spreadsheet Configuration (config.csv)](#05-admin-lane-spreadsheet-sync) ([MP4](videos/05-admin-lane-spreadsheet-sync.mp4)) | Track B | 30s | 682.8 KiB | [VTT](captions/05-admin-lane-spreadsheet-sync.vtt) · [SRT](captions/05-admin-lane-spreadsheet-sync.srt) |
| 06 | [Configure a Lane System & Georeferenced Site Diagram](#06-admin-manual-lane-and-site-diagram) ([MP4](videos/06-admin-manual-lane-and-site-diagram.mp4)) | Track B | 41s | 1078.5 KiB | [VTT](captions/06-admin-manual-lane-and-site-diagram.vtt) · [SRT](captions/06-admin-manual-lane-and-site-diagram.srt) |
| 07 | [Upload External EML VM-250 Plugin & Enable Per-Lane EML](#07-admin-eml-plugin-setup) ([MP4](videos/07-admin-eml-plugin-setup.mp4)) | Track B | 27s | 1939.6 KiB | [VTT](captions/07-admin-eml-plugin-setup.vtt) · [SRT](captions/07-admin-eml-plugin-setup.srt) |
| 08 | [Sign In to OSCAR Viewer, Switch Language & Manage Nodes](#08-viewer-signin-language-and-nodes) ([MP4](videos/08-viewer-signin-language-and-nodes.mp4)) | Track C | 31.5s | 3838.2 KiB | [VTT](captions/08-viewer-signin-language-and-nodes.vtt) · [SRT](captions/08-viewer-signin-language-and-nodes.srt) |
| 09 | [Monitor Live 50-Lane Dashboard & Inspect Alarm Rows](#09-dashboard-monitoring-and-quick-adjudication) ([MP4](videos/09-dashboard-monitoring-and-quick-adjudication.mp4)) | Track C | 29s | 2439.6 KiB | [VTT](captions/09-dashboard-monitoring-and-quick-adjudication.vtt) · [SRT](captions/09-dashboard-monitoring-and-quick-adjudication.srt) |
| 10 | [Scope Workstation Lanes with Fail-Closed Operational Views](#10-operational-views-scoping) ([MP4](videos/10-operational-views-scoping.mp4)) | Track C | 29s | 1164.3 KiB | [VTT](captions/10-operational-views-scoping.vtt) · [SRT](captions/10-operational-views-scoping.srt) |
| 11 | [Inspect Live Lane Camera Stream & Gamma/Neutron Waveforms](#11-live-lane-video-and-charts) ([MP4](videos/11-live-lane-video-and-charts.mp4)) | Track C | 62s | 3584.1 KiB | [VTT](captions/11-live-lane-video-and-charts.vtt) · [SRT](captions/11-live-lane-video-and-charts.srt) |
| 12 | [Filter Event Log by UpSet Categories, Vehicle ID, Adjudication Code & Event UUID](#12-event-log-filtering-and-adjudication-codes) ([MP4](videos/12-event-log-filtering-and-adjudication-codes.mp4)) | Track C | 56.5s | 4116.8 KiB | [VTT](captions/12-event-log-filtering-and-adjudication-codes.vtt) · [SRT](captions/12-event-log-filtering-and-adjudication-codes.srt) |
| 13 | [Review Retained 5-Frame Media, Daily File Output & Adjudicate](#13-event-details-adjudication-and-daily-file) ([MP4](videos/13-event-details-adjudication-and-daily-file.mp4)) | Track C | 39s | 2159 KiB | [VTT](captions/13-event-details-adjudication-and-daily-file.vtt) · [SRT](captions/13-event-details-adjudication-and-daily-file.srt) |
| 14 | [Export Signed Alarm QR & Verify Offline on Air-Gapped Transfer](#14-airgapped-alarm-qr-transfer) ([MP4](videos/14-airgapped-alarm-qr-transfer.mp4)) | Track C | 27s | 1628.5 KiB | [VTT](captions/14-airgapped-alarm-qr-transfer.vtt) · [SRT](captions/14-airgapped-alarm-qr-transfer.srt) |
| 15 | [Monitor RPM/Camera Status of Health & Georeferenced Site Map](#15-status-of-health-and-site-map) ([MP4](videos/15-status-of-health-and-site-map.mp4)) | Track C | 32.5s | 2886 KiB | [VTT](captions/15-status-of-health-and-site-map.vtt) · [SRT](captions/15-status-of-health-and-site-map.srt) |
| 16 | [Analyze National View Statistics & Generate Multi-Format Reports](#16-national-statistics-and-reports) ([MP4](videos/16-national-statistics-and-reports.mp4)) | Track C | 36s | 842.7 KiB | [VTT](captions/16-national-statistics-and-reports.vtt) · [SRT](captions/16-national-statistics-and-reports.srt) |
| 17 | [Configure Vehicle OCR, Compare Multi-Pass Transits & Adjudicate](#17-vehicle-ocr-and-adjudication) ([MP4](videos/17-vehicle-ocr-and-adjudication.mp4)) | Track C | 48.5s | 2912.5 KiB | [VTT](captions/17-vehicle-ocr-and-adjudication.vtt) · [SRT](captions/17-vehicle-ocr-and-adjudication.srt) |
| 18 | [Use Flight Recorder, Help (?) & Redacted Support Bundles (UI & CLI)](#18-operator-help-and-support-bundle) ([MP4](videos/18-operator-help-and-support-bundle.mp4)) | Track C | 37.5s | 3333.3 KiB | [VTT](captions/18-operator-help-and-support-bundle.vtt) · [SRT](captions/18-operator-help-and-support-bundle.srt) |
| 19 | [Manage Users, Bulk QR Invites, Offline Passkeys & Federation Tokens](#19-viewer-users-passkeys-and-access) ([MP4](videos/19-viewer-users-passkeys-and-access.mp4)) | Track C | 39.5s | 2798.3 KiB | [VTT](captions/19-viewer-users-passkeys-and-access.vtt) · [SRT](captions/19-viewer-users-passkeys-and-access.srt) |
| 20 | [Federate Multi-Site Nodes, Search Vehicles Across Portals & Generate Reports](#20-multi-node-federation-vehicle-search-and-report) ([MP4](videos/20-multi-node-federation-vehicle-search-and-report.mp4)) | Track C | 90s | 4423.5 KiB | [VTT](captions/20-multi-node-federation-vehicle-search-and-report.vtt) · [SRT](captions/20-multi-node-federation-vehicle-search-and-report.srt) |
| 21 | [Onboard Authentik SSO Passkey Users & Revoke Access Across All Layers](#21-federated-sso-passkey-onboarding-and-revocation) ([MP4](videos/21-federated-sso-passkey-onboarding-and-revocation.mp4)) | Track C | 39.5s | 1790.5 KiB | [VTT](captions/21-federated-sso-passkey-onboarding-and-revocation.vtt) · [SRT](captions/21-federated-sso-passkey-onboarding-and-revocation.srt) |
| 22 | [Install, Configure & Run the End-to-End OSCAR Regression Suite](#22-regression-suite-setup-and-certification) ([MP4](videos/22-regression-suite-setup-and-certification.mp4)) | Track D | 42.5s | 1748.3 KiB | [VTT](captions/22-regression-suite-setup-and-certification.vtt) · [SRT](captions/22-regression-suite-setup-and-certification.srt) |
| 23 | [Prepare Windows 11 WSL 2 Hosts & Right-Size 100% Per-Lane OCR](#23-windows-wsl2-host-readiness-and-ocr-scaling) ([MP4](videos/23-windows-wsl2-host-readiness-and-ocr-scaling.mp4)) | Track D | 55s | 13167.7 KiB | [VTT](captions/23-windows-wsl2-host-readiness-and-ocr-scaling.vtt) · [SRT](captions/23-windows-wsl2-host-readiness-and-ocr-scaling.srt) |
| 24 | [Manage Continual & Occasional USB NVMe Backups & Safe Field Eject](#24-continual-and-occasional-usb-backups) ([MP4](videos/24-continual-and-occasional-usb-backups.mp4)) | Track C | 43.5s | 1570.8 KiB | [VTT](captions/24-continual-and-occasional-usb-backups.vtt) · [SRT](captions/24-continual-and-occasional-usb-backups.srt) |
| 25 | [Swap Pluggable OCR Packs & Air-Gapped Regional .pmtiles Basemaps](#25-pluggable-runtime-extensions-and-pmtiles) ([MP4](videos/25-pluggable-runtime-extensions-and-pmtiles.mp4)) | Track C | 48s | 2039.9 KiB | [VTT](captions/25-pluggable-runtime-extensions-and-pmtiles.vtt) · [SRT](captions/25-pluggable-runtime-extensions-and-pmtiles.srt) |
| 26 | [Stage Ubuntu 24.04 Off-Site & Cut Over to Air-Gapped Portal Subnets](#26-ubuntu-hotel-staging-and-airgapped-cutover) ([MP4](videos/26-ubuntu-hotel-staging-and-airgapped-cutover.mp4)) | Track D | 33.5s | 1007.3 KiB | [VTT](captions/26-ubuntu-hotel-staging-and-airgapped-cutover.vtt) · [SRT](captions/26-ubuntu-hotel-staging-and-airgapped-cutover.srt) |
| 27 | [Connect Cargo NII (WCO UFF 2.0 & 3.0.0) SMB Shares & Inspect 16-Bit X-Rays](#27-cargo-uff-smb-and-xray-inspection) ([MP4](videos/27-cargo-uff-smb-and-xray-inspection.mp4)) | Track D | 55s | 3599.7 KiB | [VTT](captions/27-cargo-uff-smb-and-xray-inspection.vtt) · [SRT](captions/27-cargo-uff-smb-and-xray-inspection.srt) |
| 28 | [Practice Safely in the Ephemeral Hands-On Training Sandbox & Guided Academy](#28-hands-on-training-sandbox) ([MP4](videos/28-hands-on-training-sandbox.mp4)) | Track D | 79s | 3193.2 KiB | [VTT](captions/28-hands-on-training-sandbox.vtt) · [SRT](captions/28-hands-on-training-sandbox.srt) |
| 29 | [Configure & Control Per-Lane Physical RPM Lights & Sound (WebRelay-Quad)](#29-lane-webrelay-lights-and-sound) ([MP4](videos/29-lane-webrelay-lights-and-sound.mp4)) | Track C | 44s | 2607.8 KiB | [VTT](captions/29-lane-webrelay-lights-and-sound.vtt) · [SRT](captions/29-lane-webrelay-lights-and-sound.srt) |

## Track A — CLI Deployment, Upgrades & Storage Lifecycle

<a id="01-deployment-init-and-credentials"></a>
### 01. Initialize OSCAR Deployment, Admin Credentials & TLS

Extract a clean OSCAR 3.11.8 release archive, initialize administrator credentials and TLS SAN certificates with oscar init, and verify healthy container startup.

- **Video:** [Watch `01-deployment-init-and-credentials.mp4` (28.5s, 587.7 KiB)](videos/01-deployment-init-and-credentials.mp4) · [WebVTT Captions](captions/01-deployment-init-and-credentials.vtt) · [SRT Captions](captions/01-deployment-init-and-credentials.srt)

1. Extract `oscar-3.11.8.zip` into a clean release directory on Ubuntu Server 24.04 or Windows 11 and change into `oscar-3.11.8/`.
2. Run `sudo bash oscar.sh init` (or `.\oscar.bat init` on Windows 11) and supply the deployment hostname, IANA timezone, and administrator password (`>= 14` characters).
3. Allow `init` to generate deployment-bound PostgreSQL secrets, TLS gateway certificates, and external `oscar_oscar_state` / `oscar_postgres_data` volumes.
4. Run `sudo bash oscar.sh status` (or `.\oscar.bat status`) to confirm `oscar-gateway`, `oscar`, and `oscar-postgis` report `running (healthy)`.

<a id="02-clean-directory-upgrade"></a>
### 02. Upgrade OSCAR in a Clean Release Directory

Verify a pre-upgrade snapshot, copy only .env, secrets/, and tls/ into a newly extracted oscar-3.11.8 folder, and run oscar upgrade while preserving external volumes.

- **Video:** [Watch `02-clean-directory-upgrade.mp4` (29.5s, 519.6 KiB)](videos/02-clean-directory-upgrade.mp4) · [WebVTT Captions](captions/02-clean-directory-upgrade.vtt) · [SRT Captions](captions/02-clean-directory-upgrade.srt)

1. When `single` backup mode is enabled, run `sudo bash oscar.sh backup` and `sudo bash oscar.sh backup-verify` from the active release directory before upgrading.
2. Extract the target `oscar-3.11.8.zip` archive into a separate sibling directory — never unzip over an existing release directory.
3. Copy only `.env`, `secrets/`, and `tls/` (plus `.oscar-volume-adoption` if previously adopted) into the newly extracted directory.
4. Run `sudo bash oscar.sh upgrade` (or `.\oscar.bat upgrade`) and confirm all containers return `healthy` with preserved named volumes and archive roots.

<a id="03-archive-and-snapshot-backup"></a>
### 03. Verify Parquet Cold-Tier Archives & Single-Snapshot Backup

Inspect PARQUET_PRIMARY cold-tier generation status, verify sealed Parquet SHA-256 parity receipts, and run a coordinated single-snapshot backup and verification.

- **Video:** [Watch `03-archive-and-snapshot-backup.mp4` (28.5s, 545.2 KiB)](videos/03-archive-and-snapshot-backup.mp4) · [WebVTT Captions](captions/03-archive-and-snapshot-backup.vtt) · [SRT Captions](captions/03-archive-and-snapshot-backup.srt)

1. Run `sudo bash oscar.sh archive status` (or `.\oscar.bat archive status`) to inspect `PARQUET_PRIMARY` staging windows, sealed generation counts, and parity receipts.
2. Run `sudo bash oscar.sh archive verify` to validate manifest SHA-256 checksums and row-count parity across immutable Parquet files.
3. Ensure `single` backup mode is configured with a non-overlapping absolute backup directory (`--backup-mode single --backup-dir <path>`).
4. Run `sudo bash oscar.sh backup` followed by `sudo bash oscar.sh backup-verify` to create and verify the coordinated PostGIS, state, and archive-generation snapshot.

## Track B — SensorHub Admin Configuration

<a id="04-admin-oscar-service-and-custom-codes"></a>
### 04. Configure OSCAR Service Retention & Custom Disposition Codes

Open Services -> OSCAR Service in SensorHub Admin to review 5-JPEG media retention settings, storage-pressure thresholds, and custom adjudication disposition codes.

- **Video:** [Watch `04-admin-oscar-service-and-custom-codes.mp4` (41.5s, 1040.3 KiB)](videos/04-admin-oscar-service-and-custom-codes.mp4) · [WebVTT Captions](captions/04-admin-oscar-service-and-custom-codes.vtt) · [SRT Captions](captions/04-admin-oscar-service-and-custom-codes.srt)

1. Open `https://oscar.local/sensorhub/admin`, expand **Services**, and select **OSCAR Service**.
2. Review **Video Retention Config** (`Age Before Five-Frame Retention`, `Video Query Period`) and **Storage Pressure Retention Config** (`Trigger Usage (%)`, `Target Usage (%)`, `OCR Crop Retention`).
3. Open **Custom Disposition Codes** and click **`+`** to add or update site-specific adjudication code entries alongside built-in codes.
4. Click **Apply Changes** and **Save** in the top toolbar to persist the updated service configuration.

<a id="05-admin-lane-spreadsheet-sync"></a>
### 05. Sync Multi-Lane Spreadsheet Configuration (config.csv)

Import or download the multi-lane config.csv spreadsheet via Spreadsheet Config Path in OSCAR Service to provision RPM endpoints, RTSP cameras, and OperationalViews assignments in bulk.

- **Video:** [Watch `05-admin-lane-spreadsheet-sync.mp4` (30s, 682.8 KiB)](videos/05-admin-lane-spreadsheet-sync.mp4) · [WebVTT Captions](captions/05-admin-lane-spreadsheet-sync.vtt) · [SRT Captions](captions/05-admin-lane-spreadsheet-sync.srt)

1. Navigate to **Services -> OSCAR Service** in SensorHub Admin (`https://oscar.local/sensorhub/admin`).
2. Locate **Spreadsheet Config Path** and use **Upload** or **Download** under **General** to import or export the site's multi-lane `config.csv` spreadsheet (including `OperationalViews` semicolon-delimited keys such as `east-gate;entrance`).
3. Click **Apply Changes** and **Save** to synchronize all lane definitions.
4. Expand **Sensors** in the left accordion to confirm imported `Lane01`–`Lane50` modules are registered and active.

<a id="06-admin-manual-lane-and-site-diagram"></a>
### 06. Configure a Lane System & Georeferenced Site Diagram

Inspect Lane01 General, Fixed Location, and Lane Options settings under Sensors, populate georeferenced Lower-Left and Upper-Right Site Diagram bounds in OSCAR Service, and save.

- **Video:** [Watch `06-admin-manual-lane-and-site-diagram.mp4` (41s, 1078.5 KiB)](videos/06-admin-manual-lane-and-site-diagram.mp4) · [WebVTT Captions](captions/06-admin-manual-lane-and-site-diagram.vtt) · [SRT Captions](captions/06-admin-manual-lane-and-site-diagram.srt)

1. Open **Sensors** in SensorHub Admin and select **Lane01**.
2. Review **General** (including **Extended Occupancy Threshold (min)** and **Operational View Keys**), **Fixed Location** (latitude/longitude coordinates), and **Lane Options** (RPM driver address and RTSP camera stream parameters).
3. Switch to **Services -> OSCAR Service -> Site Diagram Config**, click **Add**, and enter georeferenced **Site Lower Left Bound** and **Site Upper Right Bound** coordinates.
4. Click **Apply Changes** and **Save** to publish lane coordinates and site map bounds to the Viewer.

<a id="07-admin-eml-plugin-setup"></a>
### 07. Upload External EML VM-250 Plugin & Enable Per-Lane EML

Verify or upload a separately licensed EML VM-250 .jar plugin in OSCAR Service, review Code 9999 documentation in the localized README, and confirm per-lane EML enablement under Lane Options.

- **Video:** [Watch `07-admin-eml-plugin-setup.mp4` (27s, 1939.6 KiB)](videos/07-admin-eml-plugin-setup.mp4) · [WebVTT Captions](captions/07-admin-eml-plugin-setup.vtt) · [SRT Captions](captions/07-admin-eml-plugin-setup.srt)

1. Open **Services -> OSCAR Service** in SensorHub Admin (`https://oscar.local/sensorhub/admin`).
2. Locate **EML Plugin Path** and use **Upload** to install the external licensed EML VM-250 `.jar` runtime into private state storage.
3. Open the **README** tab in OSCAR Service and scroll to the **EML** / `Code 9999: EML Non-Threat` guidance.
4. Open **Sensors -> Lane01 -> Lane Options** to verify **EML Configuration** (`Lane Width (m)`, `Enable EML Analysis`, `Is Collimated`).

## Track C — OSCAR Viewer Console Operations

<a id="08-viewer-signin-language-and-nodes"></a>
### 08. Sign In to OSCAR Viewer, Switch Language & Manage Nodes

Authenticate at the OSCAR TLS gateway login page (with Keep me signed in until I log out and offline Passkey support), switch console UI localization live across 4 languages, open the Operator Quick Guide (?), and configure federated OSCAR nodes.

- **Video:** [Watch `08-viewer-signin-language-and-nodes.mp4` (31.5s, 3838.2 KiB)](videos/08-viewer-signin-language-and-nodes.mp4) · [WebVTT Captions](captions/08-viewer-signin-language-and-nodes.vtt) · [SRT Captions](captions/08-viewer-signin-language-and-nodes.srt)

1. Open `https://oscar.local`, enter the operator **Username** and **Password** (with **Keep me signed in until I log out** enabled, or click **Sign in with a passkey**), and click **Sign in**.
2. Click the top-bar language selector (**English**) to switch the console interface live between `English`, `Español`, `Français`, and `Ελληνικά`, and click the `?` help icon to open the **Operator Quick Guide & Glossary**.
3. Open **Servers** (`/servers`) from the navigation drawer to verify **Local Node** status or add federated OSCAR nodes using interactive browser sessions or scoped **Federation Service Tokens (`oscar_fed_...`)**.

<a id="09-dashboard-monitoring-and-quick-adjudication"></a>
### 09. Monitor Live 50-Lane Dashboard & Inspect Alarm Rows

Monitor real-time 50-lane status tiles and live alarm occupancy rows on the Dashboard, toggle Dashboard Widgets, and launch rapid alarm telemetry and adjudication review.

- **Video:** [Watch `09-dashboard-monitoring-and-quick-adjudication.mp4` (29s, 2439.6 KiB)](videos/09-dashboard-monitoring-and-quick-adjudication.mp4) · [WebVTT Captions](captions/09-dashboard-monitoring-and-quick-adjudication.vtt) · [SRT Captions](captions/09-dashboard-monitoring-and-quick-adjudication.srt)

1. Open the OSCAR **Dashboard** (`/`) to monitor real-time **Lane Status** tiles across all 50 portal lanes and use the **Dashboard Widgets** bar to toggle **Lane Status**, **Events Table**, or **Map / Preview**.
2. Review incoming occupancy and gamma/neutron alarm rows in the live Dashboard event table and open a row's action menu (`⋮` -> **Details**).
3. Inspect the populated **Gamma** and **Neutron** count-rate waveforms alongside the **Adjudication Form** on **Event Details**.

<a id="10-operational-views-scoping"></a>
### 10. Scope Workstation Lanes with Fail-Closed Operational Views

Scope the Dashboard and Status of Health to an assigned workstation Operational View (?view=east-gate) and verify fail-closed protection on unassigned views.

- **Video:** [Watch `10-operational-views-scoping.mp4` (29s, 1164.3 KiB)](videos/10-operational-views-scoping.mp4) · [WebVTT Captions](captions/10-operational-views-scoping.vtt) · [SRT Captions](captions/10-operational-views-scoping.srt)

1. Open a workstation-scoped URL such as `https://oscar.local/?view=east-gate` and confirm the **`east-gate (10)`** scoped view indicator restricts visible lanes.
2. Navigate to **Status of Health** (`/health?view=east-gate`) to verify that only the `10` lanes assigned to `east-gate` are loaded.
3. Verify that unassigned or malformed `?view=` keys fail closed with an explicit warning banner and zero loaded lane data.

<a id="11-live-lane-video-and-charts"></a>
### 11. Inspect Live Lane Camera Stream & Gamma/Neutron Waveforms

Open Lane Details from the Dashboard to watch live RTSP/WebRTC camera video alongside multi-second real-time Gamma and Neutron count-rate waveforms across TOTALS, GAMMA DETECTORS, and NEUTRON DETECTORS views, plus lane occupancy history.

- **Video:** [Watch `11-live-lane-video-and-charts.mp4` (62s, 3584.1 KiB)](videos/11-live-lane-video-and-charts.mp4) · [WebVTT Captions](captions/11-live-lane-video-and-charts.vtt) · [SRT Captions](captions/11-live-lane-video-and-charts.srt)

1. Click **Lane01** under **Lane Status** on the Dashboard (`/`) to open **Lane Details** (`/lane-view`) and let live camera video and 5 Hz count-rate streams populate.
2. Monitor live camera video alongside multi-second **TOTALS** Gamma and Neutron waveforms, then switch between **GAMMA DETECTORS** (`G1`–`G4`) and **NEUTRON DETECTORS** (`N1`–`N4`).
3. Scroll to the lane occupancy table below the live charts to inspect historical occupancies recorded on that lane.

<a id="12-event-log-filtering-and-adjudication-codes"></a>
### 12. Filter Event Log by UpSet Categories, Vehicle ID, Adjudication Code & Event UUID

Correlate repeat occupancies by normalized Vehicle ID in Multi-Pass Vehicle Comparison, filter Event Log via Alarm Category Co-Occurrence (UpSet), build nested server-side Advanced Filters, and look up exact records by Event UUID.

- **Video:** [Watch `12-event-log-filtering-and-adjudication-codes.mp4` (56.5s, 4116.8 KiB)](videos/12-event-log-filtering-and-adjudication-codes.mp4) · [WebVTT Captions](captions/12-event-log-filtering-and-adjudication-codes.vtt) · [SRT Captions](captions/12-event-log-filtering-and-adjudication-codes.srt)

1. Navigate to **Event Log** (`/event-log`), enter a container or plate identifier in the **Vehicle / Container ID** search bar (ignoring case, spaces, and hyphens), click **SEARCH VEHICLE**, and click **COMPARE PASSES (`N`)** to inspect correlated transits.
2. Click **Alarm Category Co-Occurrence (UpSet)** (`Show`) to display populated main categories first (`Unknown`, `SNM`, `NORM`, `Medical`, `Industrial`, `Gamma`, `Neutron`), then click any populated category chip or combination bar to filter the table.
3. Click **ADVANCED FILTERS** and **ADD CONDITION** to filter server-side by date/time window, lane, alarm status, **Vehicle ID**, or **Adjudication Code** (`Code 9998`, `Code 9999`, built-in `1–11`, and custom codes).
4. Paste an occupancy observation identifier into **Event UUID** and click **FIND EVENT** to open that exact record on **Event Details**.

<a id="13-event-details-adjudication-and-daily-file"></a>
### 13. Review Retained 5-Frame Media, Daily File Output & Adjudicate

Inspect five-frame retained JPEG camera evidence across First, Middle, and Last keyframes, switch detector waveform tabs, examine exact GS, GA, NS, and GX RPM Daily File Output records, and submit an append-only adjudication.

- **Video:** [Watch `13-event-details-adjudication-and-daily-file.mp4` (39s, 2159 KiB)](videos/13-event-details-adjudication-and-daily-file.mp4) · [WebVTT Captions](captions/13-event-details-adjudication-and-daily-file.vtt) · [SRT Captions](captions/13-event-details-adjudication-and-daily-file.srt)

1. Open **Event Details** (`/event-details?eventId=<id>`), verify the **Event UUID** header bar, and step through the five retained camera JPEG thumbnails (`First`, `Middle`, `Last`) under **Retained camera evidence**.
2. Switch between **TOTALS** and **GAMMA DETECTORS** / **NEUTRON DETECTORS** on the waveform charts and scroll to **Daily File Output** to inspect exact `GS`, `GA`, `NS`, and `GX` RPM daily-file records.
3. Complete **Vehicle ID**, **Adjudicate** disposition code, **Secondary Inspection**, and **Notes** under **Adjudication Form**.
4. Click **Submit** and confirm in **Confirm Adjudication Submission** (`Confirm & Submit`) to append the signed audit record while preserving prior adjudications.

<a id="14-airgapped-alarm-qr-transfer"></a>
### 14. Export Signed Alarm QR & Verify Offline on Air-Gapped Transfer

Export a SHA-256-authenticated Alarm QR image from Event Details, then import and verify its cryptographic integrity and reconstructed waveforms offline on Alarm Transfer.

- **Video:** [Watch `14-airgapped-alarm-qr-transfer.mp4` (27s, 1628.5 KiB)](videos/14-airgapped-alarm-qr-transfer.mp4) · [WebVTT Captions](captions/14-airgapped-alarm-qr-transfer.vtt) · [SRT Captions](captions/14-airgapped-alarm-qr-transfer.srt)

1. On **Event Details**, click **Export Alarm QR** to generate the `OSCAR-ALARM:1:` signed transfer payload and QR symbol.
2. Click **Download QR Image** (or **Download Alarm File**) to save the portable PNG QR symbol or JSON package.
3. Open **Alarm Transfer** (`/alarm-transfer`) on the receiving workstation and import the QR PNG image or scan via camera.
4. Confirm **`The alarm data passed its SHA-256 integrity check.`** and review the reconstructed occupancy UUID and Gamma/Neutron waveforms.

<a id="15-status-of-health-and-site-map"></a>
### 15. Monitor RPM/Camera Status of Health & Georeferenced Site Map

Track RPM connectivity, camera stream health, detector/tamper faults, and Extended occupancy: Clear status on Status of Health, then open live georeferenced portal lane marker popups on Site Map.

- **Video:** [Watch `15-status-of-health-and-site-map.mp4` (32.5s, 2886 KiB)](videos/15-status-of-health-and-site-map.mp4) · [WebVTT Captions](captions/15-status-of-health-and-site-map.vtt) · [SRT Captions](captions/15-status-of-health-and-site-map.srt)

1. Open **Status of Health** (`/health`) from the navigation drawer to inspect real-time `Online` RPM/camera pills and detector or tamper fault badges across every lane.
2. Review lane-level `Extended occupancy: Clear` / `Fault - Extended Occupancy` status (which suppresses gamma-only extended occupancy alarms from the Dashboard and auto-adjudicates them as `Code 9998: Extended Occupancy Gamma Alarm`).
3. Open **Map** (`/map`) and click any georeferenced portal lane marker to inspect its live telemetry popup alongside map layer and zoom controls.

<a id="16-national-statistics-and-reports"></a>
### 16. Analyze National View Statistics & Generate Multi-Format Reports

Review aggregated occupancy and alarm rows on National View, then configure and generate a populated Vehicle Incident Report preview inline with Open and Download controls.

- **Video:** [Watch `16-national-statistics-and-reports.mp4` (36s, 842.7 KiB)](videos/16-national-statistics-and-reports.mp4) · [WebVTT Captions](captions/16-national-statistics-and-reports.vtt) · [SRT Captions](captions/16-national-statistics-and-reports.srt)

1. Open **National View** (`/national-view`) to inspect aggregated occupancy totals, gamma/neutron alarm counts, and multi-lane trends.
2. Navigate to **Report Generator** (`/report`) and choose **Node Selector**, **Report Scope** (`Entire Node`, `Operational View`, or `Specific Lanes`), **Report Type** (`RDS_SITE`, `LANE`, `EVENT`, `ADJUDICATION`, `ADJUDICATION_DETAILS`, or `VEHICLE_INCIDENT`), **Export Format** (`PDF`, `CSV`, `JSON`, or `Excel (.xlsx)`), and **Time Range**.
3. Enter a normalized **Vehicle ID**, click **Generate Report**, and review the populated inline tabular preview alongside **Open** and **Download** controls.

<a id="17-vehicle-ocr-and-adjudication"></a>
### 17. Configure Vehicle OCR, Compare Multi-Pass Transits & Adjudicate

Inspect per-lane Vehicle OCR configuration on an OCR-enabled lane in SensorHub Admin, open an alarm in Event Details to review ISO 6346 container auto-fill, OCR suggestion chips, and Multi-Pass Vehicle History, compare overlaid radiation traces across passes, and record an adjudication.

- **Video:** [Watch `17-vehicle-ocr-and-adjudication.mp4` (48.5s, 2912.5 KiB)](videos/17-vehicle-ocr-and-adjudication.mp4) · [WebVTT Captions](captions/17-vehicle-ocr-and-adjudication.vtt) · [SRT Captions](captions/17-vehicle-ocr-and-adjudication.srt)

1. Open **Sensors -> Lane50 -> Vehicle OCR** in SensorHub Admin (`https://oscar.local/sensorhub/admin`) to review **Enable Vehicle OCR**, **Alarms Only**, **Frames Per Clip**, and confidence thresholds.
2. Open **Event Details** (`/event-details?eventId=<id>`) in OSCAR Viewer for an alarm occupancy on an OCR-enabled lane to verify ISO 6346 **Vehicle ID** auto-fill, clickable OCR suggestion chips, and the **Multi-Pass Vehicle History** correlation banner.
3. Click **COMPARE PASSES** and **LOAD RADIATION TRACES** to inspect chronological confirmation re-scans, visual continuity crops, and overlaid gamma/neutron radiation waveforms.
4. Select an **Adjudicate** disposition code and **Secondary Inspection** status, click **Submit**, and confirm in **Confirm Adjudication Submission** to append the signed audit decision.

<a id="18-operator-help-and-support-bundle"></a>
### 18. Use Flight Recorder, Help (?) & Redacted Support Bundles (UI & CLI)

Open Help (?) to browse the localized Operator Quick Guide & Glossary, export the built-in 400-event browser Flight Recorder + rolling server logs into oscar-support-<UTC>.zip, run oscar.sh / oscar.bat support-bundle offline, and inspect summary.json and redaction-report.json.

- **Video:** [Watch `18-operator-help-and-support-bundle.mp4` (37.5s, 3333.3 KiB)](videos/18-operator-help-and-support-bundle.mp4) · [WebVTT Captions](captions/18-operator-help-and-support-bundle.vtt) · [SRT Captions](captions/18-operator-help-and-support-bundle.srt)

1. Click the **Help (`?`)** button in the OSCAR Viewer top navigation bar to open the localized **OSCAR 3.11.8 Operator Quick Guide & Glossary** (`en`, `es`, `fr`, `el`).
2. Open **Manual & Video Guides** and click **Export Support Bundle** to merge the 400-event browser Flight Recorder (`client/client-diagnostics.json`) with rolling server logs (`backend/oscar.log`) into `oscar-support-<UTC>.zip` (automatically falling back to `oscar-client-support-<UTC>.zip` if the server is offline).
3. When containers are stopped or unreachable over HTTPS, run `sudo bash oscar.sh support-bundle` (Ubuntu) or `.\oscar.bat support-bundle` (Windows) on the host to capture `oscar-host-support-<UTC>.zip`.
4. Inspect `summary.json`, `client/client-diagnostics.json`, and `redaction-report.json` side-by-side to review recent events and confirm automatic `[REDACTED]` credential scrubbing.

<a id="19-viewer-users-passkeys-and-access"></a>
### 19. Manage Users, Bulk QR Invites, Offline Passkeys & Federation Tokens

Open Users & Access (/users) to enroll offline WebAuthn Passkeys, bulk-enroll a CSV user list with 1-tap setup QR codes, mint scoped Federation Service Tokens, and launch Servers (/servers?auth=bearer) in Federation Token mode.

- **Video:** [Watch `19-viewer-users-passkeys-and-access.mp4` (39.5s, 2798.3 KiB)](videos/19-viewer-users-passkeys-and-access.mp4) · [WebVTT Captions](captions/19-viewer-users-passkeys-and-access.vtt) · [SRT Captions](captions/19-viewer-users-passkeys-and-access.srt)

1. Open **Users & Access** (`/users`) from the navigation drawer to inspect persistent session status (`Stays signed in until you click Log Out`), register offline **Passkeys / YubiKeys**, or update your local OSCAR password (separate from Octelium tunnel credentials).
2. Switch to **Users & Roles** and click **Bulk Enroll (CSV / Paste)** to upload or paste a CSV/Excel user list (`username, role, display_name, views`), preview validated rows, and click **Enroll User(s) & Generate QR Pack**.
3. Copy or print the generated **Startup Messages & 1-Tap Setup QR Codes** (`/login/enroll?token=oscar_inv_...`, including fallback workstation codes for phone-free facilities).
4. Open **Federation Tokens**, mint a least-privilege `oscar_fed_...` token, inspect the minted token banner, and click **Open Servers Page (Federation Token Mode)** (`/servers?auth=bearer`) to paste the token into **Servers** (`HTTPS`, port `443`).

<a id="20-multi-node-federation-vehicle-search-and-report"></a>
### 20. Federate Multi-Site Nodes, Search Vehicles Across Portals & Generate Reports

Mint a scoped oscar_fed_* Federation Service Token on West Gate Portal, register the remote HTTPS node on Central HQ Node, correlate cross-portal container transits in Events -> Compare Passes, and export unified multi-node Vehicle Incident JSON and PDF reports.

- **Video:** [Watch `20-multi-node-federation-vehicle-search-and-report.mp4` (90s, 4423.5 KiB)](videos/20-multi-node-federation-vehicle-search-and-report.mp4) · [WebVTT Captions](captions/20-multi-node-federation-vehicle-search-and-report.vtt) · [SRT Captions](captions/20-multi-node-federation-vehicle-search-and-report.srt)

1. On the remote OSCAR portal (**West Gate Portal**), open **Users & Access (`/users`) -> Federation Tokens**, enter a descriptive node label, select `Viewer` or `Operator`, and click **Create Federation Token** to mint a revocable `oscar_fed_...` bearer credential.
2. On **Central HQ Node**, open **Servers (`/servers?auth=bearer`)**, enter **West Gate Portal**, its HTTPS address, and port `443`, paste the `oscar_fed_...` token, and click **Add Node**.
3. Open **Events (`/event-log`)**, enter an ISO 6346 container ID, click **SEARCH VEHICLE**, and click **COMPARE PASSES** + **LOAD RADIATION TRACES** to inspect cross-node crossings, OCR crops, and waveforms from both portals.
4. Open **Report Generator (`/report`)**, choose **Vehicle Incident Report** with **Include correlated passes from federated nodes** checked, and generate consolidated `JSON` and `PDF` reports spanning both federated portals.

<a id="21-federated-sso-passkey-onboarding-and-revocation"></a>
### 21. Onboard Authentik SSO Passkey Users & Revoke Access Across All Layers

Create centralized operator and viewer accounts in Authentik, map roles via oscar-admins, oscar-operators, and oscar-viewers, issue single-use 1-tap SSO Passkey enrollment links, and permanently revoke access across Authentik, Octelium Zero-Trust Hub, and OSCAR /users.

- **Video:** [Watch `21-federated-sso-passkey-onboarding-and-revocation.mp4` (39.5s, 1790.5 KiB)](videos/21-federated-sso-passkey-onboarding-and-revocation.mp4) · [WebVTT Captions](captions/21-federated-sso-passkey-onboarding-and-revocation.vtt) · [SRT Captions](captions/21-federated-sso-passkey-onboarding-and-revocation.srt)

1. In **Authentik Admin (`https://auth.hub.example.org/if/admin/`) -> Directory -> Users**, click **Create**, enter the username, display name, and email address, and add the user to `oscar-admins`, `oscar-operators`, or `oscar-viewers`.
2. Open the user's **Overview** tab and click **Create Recovery Link** to copy a single-use `oscar-passkey-onboarding` URL so the recipient registers their FIDO2 Passkey in one tap.
3. To completely offboard a user, select the account in **Authentik -> Directory -> Users**, click **Delete**, and confirm permanent deletion (`oscar-hub-sync.timer` purges Octelium Zero-Trust access automatically), then verify `/users` on OSCAR nodes.

<a id="24-continual-and-occasional-usb-backups"></a>
### 24. Manage Continual & Occasional USB NVMe Backups & Safe Field Eject

Open USB Backups (/usb-backups) to inspect an attached NTFS external USB 3.x NVMe SSD, configure Continual vs. Occasional zero-downtime sync, run an on-demand incremental backup, download the off-site recovery key, and perform a 1-click Safely Eject USB Drive offload.

- **Video:** [Watch `24-continual-and-occasional-usb-backups.mp4` (43.5s, 1570.8 KiB)](videos/24-continual-and-occasional-usb-backups.mp4) · [WebVTT Captions](captions/24-continual-and-occasional-usb-backups.vtt) · [SRT Captions](captions/24-continual-and-occasional-usb-backups.srt)

1. Open **USB Backups (`/usb-backups`)** from the left navigation drawer to inspect the attached external USB 3.x NVMe SSD (`ATTACHED & ONLINE`), carrier capacity, PostgreSQL WAL LSN, and deduplicated Parquet/media pack counts.
2. Click **Sync Incremental Snapshot Now** to capture new sealed Parquet daily packs, retained media/OCR crops, and an encrypted PostgreSQL checkpoint, and click **Download Off-Site Recovery Key (`backup-key.txt`)** for off-site escrow.
3. Under **Backup Mode & Sync Schedule**, choose **Continual Background Sync** (`15 min` default, `0.0 s` portal outage with automatic USB reconnect catch-up) or **Occasional / On-Demand Visit Sync**, and click **Save Mode & Schedule**.
4. Before unplugging the drive for laptop offload (`COPY-TO-ANOTHER-DRIVE.bat` or `./copy-to-another-drive.sh`) or cold-iron recovery (`sudo bash oscar.sh usb-backup restore`), click **Safely Eject USB Drive** and confirm the green **SAFE TO UNPLUG** banner.

<a id="25-pluggable-runtime-extensions-and-pmtiles"></a>
### 25. Swap Pluggable OCR Packs & Air-Gapped Regional .pmtiles Basemaps

Open Runtime Extensions (/extensions) to inspect OSCAR's shipped built-in defaults, hot-swap a Unicode regional OCR plate-rule pack and an offline PMTiles v3 (.pmtiles) regional basemap, render live portal lane markers over regional corridor roads/waterways on Map (/map), and restore shipped defaults.

- **Video:** [Watch `25-pluggable-runtime-extensions-and-pmtiles.mp4` (48s, 2039.9 KiB)](videos/25-pluggable-runtime-extensions-and-pmtiles.mp4) · [WebVTT Captions](captions/25-pluggable-runtime-extensions-and-pmtiles.vtt) · [SRT Captions](captions/25-pluggable-runtime-extensions-and-pmtiles.srt)

1. Open **Runtime Extensions (`/extensions`)** from the left navigation drawer to review the upgrade-safe extension domains (`OCR Models & Engines`, `Offline Maps (.pmtiles)`, `Spectroscopy / Nuclide ID`, `Trusted CA Certificates`, `Adjudication Policy Packs`, `EML Alarm Assessment`, and `Cargo NII (WCO UFF)`).
2. On **OCR Models & Engines**, upload a compliant `plate-rules.json` or ONNX/SPI `.zip` package to activate regional non-Latin or numeric plate rules (`CUSTOM OVERRIDE (UPGRADE-SAFE)`) while inheriting OSCAR's shipped PP-OCRv3 + PARSeq models.
3. Switch to **Offline Maps (`.pmtiles`)**, enter `Regional Port Corridor`, upload a Protomaps **PMTiles v3** regional archive, and open **Map (`/map`)** to view all 50 portal lane markers over `Offline: Regional Port Corridor` via HTTP `206` byte-range serving.
4. Return to **Runtime Extensions (`/extensions`)** and click **Reset to Shipped Default** to revert immediately (`SHIPPED DEFAULT ACTIVE`) with zero portal downtime.

<a id="29-lane-webrelay-lights-and-sound"></a>
### 29. Configure & Control Per-Lane Physical RPM Lights & Sound (WebRelay-Quad)

Configure per-lane ControlByWeb WebRelay-Quad HTTP/XML control in Status of Health (/health), inspect live R1-R4 coil telemetry and Code 9999 / Code 9998 suppression counts, fire timed commissioning pulses on Gamma Red + Siren (R3) and Neutron Blue (R4), and open the anytime Guided Walkthrough refresher.

- **Video:** [Watch `29-lane-webrelay-lights-and-sound.mp4` (44s, 2607.8 KiB)](videos/29-lane-webrelay-lights-and-sound.mp4) · [WebVTT Captions](captions/29-lane-webrelay-lights-and-sound.vtt) · [SRT Captions](captions/29-lane-webrelay-lights-and-sound.srt)

1. Sign in as an **Administrator**, open **Status of Health (`/health`)**, and click **Lights & Sound** on **Lane01** to open the native `<dialog>` WebRelay-Quad control modal.
2. Enter the lane's ControlByWeb `WebRelay-Quad` IPv4/hostname (`198.51.100.21`), port (`80`), pulse duration (`5 s`), and mode (`AUTO`), click **Test Connection**, and click **Save & Apply to Lane**.
3. Verify `R1=ARMED` and `R2=ARMED` intercept coils in `AUTO` mode, fire timed commissioning pulses on **Gamma Light + Sound (`R3=ACTIVE`)** and **Neutron Blue (`R4=ACTIVE`)**, and click **Silence** to re-arm `R1=ARMED, R2=ARMED`.
4. Close the dialog, verify **WebRelay (AUTO) · Online** on `/health`, and open **Guided Walkthrough** in the top bar anytime for a safe read-only refresher and `:8444` auto-shutdown details.

## Track D — End-to-End Regression & Multi-OS Capacity Scaling

<a id="22-regression-suite-setup-and-certification"></a>
### 22. Install, Configure & Run the End-to-End OSCAR Regression Suite

Install ORNL/oscar-regression, run all 246 offline unit tests, configure .env capability gates and 4-layer safety interlocks, execute smoke, full, release, restore-drill, and ui-endurance profiles across all 23 functional scenarios, and inspect summary.md and CSV evidence.

- **Video:** [Watch `22-regression-suite-setup-and-certification.mp4` (42.5s, 1748.3 KiB)](videos/22-regression-suite-setup-and-certification.mp4) · [WebVTT Captions](captions/22-regression-suite-setup-and-certification.vtt) · [SRT Captions](captions/22-regression-suite-setup-and-certification.srt)

1. Clone [`ORNL/oscar-regression`](https://github.com/ORNL/oscar-regression), run `npm ci` and `npm run install:browser`, and verify TypeScript compilation and all 246 offline unit tests with `npm run check && npm test`.
2. Copy `.env.example` to `.env` (`chmod 600 .env`), set target, emulator, `RPM_LANE_MAPPING_ACK`, and `DISPOSABLE-STORAGE` safety interlocks, and run `./scripts/rebind-active-release.sh --apply --build-label <label>` after clean-directory upgrades.
3. Execute `npm run test:smoke` (`13` read-only scenarios), `npm run test:full` (`23` scenarios including faults, alarms, Vehicle OCR, EML, Cargo UFF, Sandbox, WebRelay, and `PARQUET_PRIMARY` retirement), `npm run test:restore-drill`, or `./scripts/run-ui-endurance.sh`.
4. Review `results/<UTC-timestamp>-<runner>/summary.md`, `functional-results.csv`, `performance.csv`, `storage-performance.csv`, `errors.csv`, and `evidence/` screenshots (`exit 0` requires `0` incorrect checks).

<a id="23-windows-wsl2-host-readiness-and-ocr-scaling"></a>
### 23. Prepare Windows 11 WSL 2 Hosts & Right-Size 100% Per-Lane OCR

Prepare unattended 24/7 Windows 11 + WSL 2 hosts with oscar.bat prepare-host, attach outbound Zero-Trust tunnels, and size 100% Container & License Plate OCR cleanly (6 OCR lanes on Windows 11 WSL 2 vs. 50 OCR lanes on Ubuntu Server 24.04 bare-metal) without 5 Hz RPM sample bunching.

- **Video:** [Watch `23-windows-wsl2-host-readiness-and-ocr-scaling.mp4` (55s, 13167.7 KiB)](videos/23-windows-wsl2-host-readiness-and-ocr-scaling.mp4) · [WebVTT Captions](captions/23-windows-wsl2-host-readiness-and-ocr-scaling.vtt) · [SRT Captions](captions/23-windows-wsl2-host-readiness-and-ocr-scaling.srt)

1. On Windows 11 x86-64 (Administrator PowerShell 5.1), run `.\oscar.bat host-check` and `.\oscar.bat prepare-host` to enable High Performance AC power, disable sleep/USB suspend, and write bounded `%USERPROFILE%\.wslconfig` limits.
2. Attach firewalled portals outbound over TLS `443` via `.\oscar-remote-access.ps1 configure` (Windows) or `sudo bash oscar-remote-access.sh configure` (Ubuntu).
3. When enabling `100%` per-lane Container & License Plate OCR (`ocrConfig.enabled = true`), size Windows 11 + WSL 2 deployments to `1–8` lanes (`6` lanes validated) for smooth `200 ms` (`5 Hz`) radiation plots, and deploy `25–50` OCR lanes on Ubuntu Server 24.04 bare-metal.

<a id="26-ubuntu-hotel-staging-and-airgapped-cutover"></a>
### 26. Stage Ubuntu 24.04 Off-Site & Cut Over to Air-Gapped Portal Subnets

Unpack the self-contained Ubuntu 24.04 offline bundle on hotel/office Wi-Fi, identify physical NICs by carrier blink, pre-stage the portal's static Netplan YAML without dropping SSH, expand Ubuntu LVM root storage and initialize OSCAR 3.11.8 offline, then cut over on-site and discover RPMs and RTSP cameras.

- **Video:** [Watch `26-ubuntu-hotel-staging-and-airgapped-cutover.mp4` (33.5s, 1007.3 KiB)](videos/26-ubuntu-hotel-staging-and-airgapped-cutover.mp4) · [WebVTT Captions](captions/26-ubuntu-hotel-staging-and-airgapped-cutover.vtt) · [SRT Captions](captions/26-ubuntu-hotel-staging-and-airgapped-cutover.srt)

1. Off-site (hotel or staging bench), extract `oscar-3.11.8-ubuntu-x86_64-offline-full.zip`, verify bundle checksums (`sudo bash verify-bundle.sh`), and run `sudo bash oscar.sh identify-nics --watch` while plugging a patch cord into the target NIC to confirm its Linux interface name (`enp2s0`).
2. Stage the portal's static IPv4 configuration safely without touching active Wi-Fi/SSH via `sudo bash oscar.sh stage-site-network --interface enp2s0 --ip 198.51.100.10/24 --gateway 198.51.100.1`.
3. Run `sudo bash oscar.sh prepare-host --offline --expand-lvm` to expand Ubuntu Server's default `100 GiB` LVM logical volume across the full NVMe disk and install offline `.deb` packages, then run `sudo bash oscar.sh init --offline` to load air-gapped container images and initialize credentials.
4. On-site inside the air-gapped portal rack, apply the pre-staged static subnet with `sudo bash oscar.sh apply-site-network` and scan the sensor LAN with `sudo bash oscar.sh discover-devices --interface enp2s0` to verify Rapiscan RPM (`10001–10050`) and RTSP camera (`554`/`8554`) endpoints.

<a id="27-cargo-uff-smb-and-xray-inspection"></a>
### 27. Connect Cargo NII (WCO UFF 2.0 & 3.0.0) SMB Shares & Inspect 16-Bit X-Rays

Enable an optional SMBv2/SMBv3 Cargo Non-Intrusive Inspection share in Runtime Extensions, browse scanner packages with 1-character fuzzy ISO 6346 OCR correlation in Event Details, inspect progressive 16-bit dual-energy HEMD radiographs aligned with the RPM gamma/neutron waveform, and stage a .uffref.json adjudication pointer.

- **Video:** [Watch `27-cargo-uff-smb-and-xray-inspection.mp4` (55s, 3599.7 KiB)](videos/27-cargo-uff-smb-and-xray-inspection.mp4) · [WebVTT Captions](captions/27-cargo-uff-smb-and-xray-inspection.vtt) · [SRT Captions](captions/27-cargo-uff-smb-and-xray-inspection.srt)

1. Open **Runtime Extensions** (`/extensions`), select **Cargo NII (WCO UFF)**, configure the read-only SMBv2/SMBv3 share (`\\nas.port.local\oscar-uff`), click **TEST CONNECTION**, and click **SAVE & INDEX** to index `160` `.uff` packages in place.
2. In **Event Details** (`/event-details`), click **Browse Cargo UFF** to search by ISO 6346 container ID (`EGHU3972694`, including **OCR ±1** 1-character fuzzy matching), scanner ID, customs HS code, or UFF UUID.
3. Click **Inspect 16-Bit X-Ray** to view full 16-bit Window/Level, **HEMD (`Z_eff`)** material coloration, **High-Z** `<Annotation>` bounding boxes, and the synchronized RPM Gamma/Neutron waveform alignment strip.
4. Click **Link to Adjudication** to stage a lightweight `.uffref.json` NAS pointer, manifest PDF, and embedded ANSI N42.42 spectrum in **Evidence Collection** without copying multi-megabyte `.uff` archives.

<a id="28-hands-on-training-sandbox"></a>
### 28. Practice Safely in the Ephemeral Hands-On Training Sandbox & Guided Academy

Launch the isolated ephemeral Training Sandbox (:8444) with zero production database or Parquet writes, inject live Rapiscan RPM alarms and NORM/fault scenarios until Lab 1.3 turns Auto-Verified, inspect Services -> OSCAR Service inside Split-Pane SensorHub Admin, and export a watermarked PDF Training Completion Record.

- **Video:** [Watch `28-hands-on-training-sandbox.mp4` (79s, 3193.2 KiB)](videos/28-hands-on-training-sandbox.mp4) · [WebVTT Captions](captions/28-hands-on-training-sandbox.vtt) · [SRT Captions](captions/28-hands-on-training-sandbox.srt)

1. Start the isolated sandbox (`sudo bash oscar.sh sandbox start` or `Help (?) -> Launch Hands-On Training Sandbox`), open `:8444`, and confirm the single-row **TRAINING SANDBOX** badge and **Training Coach** dock.
2. Select **Track 1 — Operator (`Lab 1.3`)** on `/event-log`, click **Inject Distributed NORM (Code 9999)**, and wait for the live loopback Rapiscan + EML pipeline to turn **Lab 1.3** green **`Auto-Verified`**.
3. Switch to **Track 3 — Administrator**, click **Open Split-Pane SensorHub Admin**, and expand **Services -> OSCAR Service** inside the embedded admin pane beside the Guided Coach.
4. Enter the trainee name to download a watermarked 1-page PDF **Training Completion Record**, then run `oscar.sh sandbox stop` (`oscar.bat sandbox stop`) when finished to flush disposable sandbox volumes.
