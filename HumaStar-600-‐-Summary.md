### ✅ **Summary of Required Actions for Interface Development**

**1. Communication Setup (Serial, ASTM E1381):**

* Configure **RS-232** settings:

  * **Baud rate:** 38400
  * **Parity:** Odd
  * **Timeouts:** 3000ms for query and retry, 100ms between messages
* Ensure analyzer is set to **Host Query Mode** for automation:

  * Auto send results = **Enabled**
  * Auto request tests = **Enabled**
  * Only order by LIS = **Enabled**

**2. Implement ASTM Message Handling (ASTM E1394):**
You must handle the following message types:

* **H** – Header
* **P** – Patient Information
* **O** – Order
* **R** – Result
* **Q** – Query
* **L** – Terminator

Ensure your message parser and builder in `ResponseHandler` and `LISCommunicator` are structured to send and receive:

* **Order queries** (e.g., when a new barcode is scanned)
* **Result transmissions** (after result acceptance)
* Optional: **Dilution Factor** and **QC results** if needed

**3. Sample Lifecycle in Host Query Mode:**

* Analyzer sends a **Q-record query** for a sample.
* LIS replies with **P + O** records (patient + order).
* Analyzer runs test → sends back **P + O + R + L** messages (result).
* System must correctly respond to {ENQ}, {ACK}, {EOT}, {STX}, {ETX}, etc.

**4. Message Construction Details:**

* `^^^TESTID` format required in O and R records.
* Use consistent timestamp format: `YYYYMMDDHHMMSS`.
* Confirm that **specimen descriptor** values are mapped (Serum, Plasma, etc.).
* Use correct ASTM checksum calculation and block framing (important for hardware protocol).

**5. Analyzer Software Settings:**

* Activate LIMS under: `Maintenance > Parameters > Software > LIMS`.
* Enable settings:

  * Auto send results
  * Auto request tests
  * Only order by LIMS
  * Apply method limits
* Leave QC/calibrator options **disabled** unless needed.

**6. Testing & Troubleshooting:**

* Use **“LIMS > Communication”** window on the analyzer to view live data flow.
* Use **“LIMS > Save debug info”** to access `ErrorsLog.txt`.
* Use **“Purge”** to reset LIS communications.

**7. Optional Features (for future stages):**

* **Send Dilution Factor**
* **Query samples at rack positions**
* **Send individual result**
* **Handle batch and legacy modes** (not recommended for new systems)
