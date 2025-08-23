<html>
<body>
<!--StartFragment--><html><head></head><body><h1>ReportTimerController Integration Guide</h1>
<h2>📋 Overview</h2>
<p>The <code>ReportTimerController</code> utility class has been introduced to track and monitor the time taken for report generation in the system. This allows automatic logging of report execution metrics for audit, performance optimization, and debugging purposes.</p>
<h3>What Gets Logged</h3>
<ul>
<li>⏰ <strong>Start time</strong> - When report generation begins</li>
<li>⏰ <strong>End time</strong> - When report generation completes</li>
<li>👤 <strong>Executing user</strong> - Who initiated the report</li>
<li>📊 <strong>Report type and name</strong> - What report was generated</li>
</ul>
<p>All captured data is saved in the <code>ReportLog</code> entity for future analysis.</p>
<h2>📁 File Location</h2>
<pre><code>com.divudi.bean.common.ReportTimerController
</code></pre>
<h2>🎯 Purpose</h2>
<p>The ReportTimerController encapsulates the logic required to:</p>
<ul>
<li>Log the start time of a report</li>
<li>Execute the report generation logic</li>
<li>Log the end time and calculate report duration</li>
<li>Save execution metrics to the database</li>
</ul>
<hr>
<h2>🔧 Integration Steps</h2>
<p>Follow this step-by-step guide to integrate report time tracking into your existing report methods:</p>
<h3>Step 1: Locate Your Report Files</h3>
<p>Find the XHTML file where your report exists (e.g., <code>/pharmacy/bin_card.xhtml</code>)</p>
<h3>Step 2: Find the Processing Method</h3>
<p>Navigate to the processing button and identify the method in the <code>action</code> attribute:</p>
<pre><code class="language-xhtml">action="#{pharmacyErrorChecking.processBinCard()}"
</code></pre>
<h3>Step 3: Wrap Your Report Logic</h3>
<p>Wrap your existing report processing logic inside the <code>trackReportExecution</code> method:</p>
<pre><code class="language-java">reportTimerController.trackReportExecution(() -&gt; {
    // Your existing report processing code goes here
}, YourReportEnum.REPORT_NAME, sessionController.getLoggedUser());
</code></pre>
<hr>
<h2>📝 Example Implementation</h2>
<h3>Before Integration</h3>
<pre><code class="language-java">public void processBinCard() {
    binCardEntries = stockHistoryController.findBinCardDTOs(fromDate, toDate, null, department, item);
    
    if (configOptionApplicationController.getBooleanValueByKey("Pharmacy Bin Card - Hide Adjustment Bills in Bin Card", true)) {
        List&lt;BillType&gt; bts = new ArrayList&lt;&gt;();
        bts.add(BillType.PharmacyAdjustmentSaleRate);
        
        Iterator&lt;PharmacyBinCardDTO&gt; iterator = binCardEntries.iterator();
        while (iterator.hasNext()) {
            PharmacyBinCardDTO dto = iterator.next();
            if (dto.getBillType() != null &amp;&amp; bts.contains(dto.getBillType())) {
                iterator.remove();
            }
        }
    }
}
</code></pre>
<h3>After Integration</h3>
<pre><code class="language-java">public void processBinCard() {
    reportTimerController.trackReportExecution(() -&gt; {
        binCardEntries = stockHistoryController.findBinCardDTOs(fromDate, toDate, null, department, item);
        
        if (configOptionApplicationController.getBooleanValueByKey("Pharmacy Bin Card - Hide Adjustment Bills in Bin Card", true)) {
            List&lt;BillType&gt; bts = new ArrayList&lt;&gt;();
            bts.add(BillType.PharmacyAdjustmentSaleRate);
            
            Iterator&lt;PharmacyBinCardDTO&gt; iterator = binCardEntries.iterator();
            while (iterator.hasNext()) {
                PharmacyBinCardDTO dto = iterator.next();
                if (dto.getBillType() != null &amp;&amp; bts.contains(dto.getBillType())) {
                    iterator.remove();
                }
            }
        }
    }, PharmacyReports.PHARMACY_BIN_CARD, sessionController.getLoggedUser());
}
</code></pre>
<hr>
<h2>🏷️ Report Enum Configuration</h2>
<h3>Creating Report Type Enums</h3>
<p>To enable proper identification of report types, ensure your report type is declared in the appropriate module enum. Use the module-specific enum file based on your report's domain.</p>
<p><strong>Example: PharmacyReports.java</strong></p>
<pre><code class="language-java">package com.divudi.core.data.reports;

public enum PharmacyReports implements IReportType {
    PHARMACY_BIN_CARD("Pharmacy Bin Card"),
    PHARMACY_STOCK_SUMMARY("Pharmacy Stock Summary"),
    PHARMACY_SALES_REPORT("Pharmacy Sales Report");
    
    private final String displayName;
    
    PharmacyReports(String displayName) {
        this.displayName = displayName;
    }
    
    @Override
    public String getDisplayName() {
        return displayName;
    }
    
    @Override
    public String getReportType() {
        return this.getClass().getSimpleName();
    }
    
    @Override
    public String getReportName() {
        return this.name();
    }
}
</code></pre>


</body></html><!--EndFragment-->
</body>
</html>

[Back](https://github.com/hmislk/hmis/wiki)
