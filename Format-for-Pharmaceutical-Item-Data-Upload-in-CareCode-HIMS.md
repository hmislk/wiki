<html>
<body>
<!--StartFragment--><html><head></head><body><p><strong>Wiki Article: Format for Pharmaceutical Item Data Upload in CareCode HIMS</strong></p>
<p>The CareCode HIMS requires a standardised format for uploading pharmaceutical item data. This format ensures consistency and accuracy in inventory and prescribing systems. Below is the description of the columns and their expected contents in the Excel file format.</p>
<hr>
<h3><strong>Columns and Definitions</strong></h3>
<h4><strong>Category (Optional)</strong></h4>
<ul>
<li><strong>Definition</strong>: A classification column that allows hospitals to categorise items based on their internal management needs, such as discounts, department-specific usage, or procurement types.</li>
<li><strong>Example Values</strong>:
<ul>
<li>General Medicine</li>
<li>Emergency Stock</li>
<li>Paediatric Use</li>
</ul>
</li>
</ul>
<h4><strong>Dosage Form</strong></h4>
<ul>
<li><strong>Definition</strong>: Specifies the pharmaceutical form of the product, indicating how it is administered.</li>
<li><strong>Example Values</strong>:
<ul>
<li>Tablet</li>
<li>Capsule</li>
<li>Syrup</li>
</ul>
</li>
</ul>
<h4><strong>AMP (Actual Medicinal Product)</strong></h4>
<ul>
<li><strong>Definition</strong>: This is the brand name or trade name of the product as marketed by the manufacturer.</li>
<li><strong>Example Values</strong>:
<ul>
<li>Acarb Tablet 50mg</li>
<li>Acetazolamide 250mg Tablets</li>
<li>Aldactone 100mg Tablets</li>
</ul>
</li>
</ul>
<h4><strong>VMP (Virtual Medicinal Product)</strong></h4>
<ul>
<li><strong>Definition</strong>: Represents a standardised description of the medicinal product, inclusive of the strength, dosage form, and active ingredient(s).</li>
<li><strong>Example Values</strong>:
<ul>
<li>Acarbose 50mg Tablet</li>
<li>Acetazolamide 250 mg Tablet</li>
<li>Spironolactone 100 mg Tablet</li>
</ul>
</li>
</ul>
<h4><strong>VTM (Virtual Therapeutic Moiety)</strong></h4>
<ul>
<li><strong>Definition</strong>: The generic name or active ingredient of the medicinal product. It helps group products with the same therapeutic moiety.</li>
<li><strong>Example Values</strong>:
<ul>
<li>Acarbose</li>
<li>Acetazolamide</li>
<li>Spironolactone</li>
</ul>
</li>
</ul>
<h4><strong>Strength</strong></h4>
<ul>
<li><strong>Definition</strong>: The amount of active ingredient in each unit of the product. This should only contain the numeric value.</li>
<li><strong>Example Values</strong>:
<ul>
<li>50</li>
<li>100</li>
<li>250</li>
</ul>
</li>
</ul>
<h4><strong>Strength Unit</strong></h4>
<ul>
<li><strong>Definition</strong>: The unit of measurement for the strength of the product. Commonly used units include mg (milligrams) or mcg (micrograms).</li>
<li><strong>Example Values</strong>:
<ul>
<li>mg</li>
<li>mcg</li>
</ul>
</li>
</ul>
<h4><strong>Issue Unit</strong></h4>
<ul>
<li><strong>Definition</strong>: The form in which the product is issued or dispensed.</li>
<li><strong>Example Values</strong>:
<ul>
<li>Tablet</li>
<li>Capsule</li>
<li>Sachet</li>
</ul>
</li>
</ul>
<hr>
<h3><strong>Guidelines for Preparing the Data</strong></h3>
<ol>
<li><strong>Consistency</strong>: Ensure all data fields are consistently filled, particularly for VMP and VTM, to avoid duplication.</li>
<li><strong>No Blank Rows</strong>: Every row should contain valid data for all mandatory columns.</li>
<li><strong>Standardised Units</strong>: Use the approved abbreviations for strength units (e.g., mg, mcg).</li>
<li><strong>Accuracy</strong>: Double-check spelling, especially for VTM, to avoid incorrect mapping of therapeutic moieties.</li>
<li><strong>Category Allocation</strong>: Use meaningful categories to aid hospital workflow; these can vary based on the hospital’s preferences.</li>
</ol>
<hr>
<h3><strong>Example Dataset</strong></h3>

Category | Dosage Form | AMP | VMP | VTM | Strength | Strength Unit | Issue Unit
-- | -- | -- | -- | -- | -- | -- | --
General Medicine | Tablet | Acarb Tablet 50mg | Acarbose 50mg Tablet | Acarbose | 50 | mg | Tablet
Emergency Stock | Tablet | Acetazolamide 250mg Tablets | Acetazolamide 250 mg Tablet | Acetazolamide | 250 | mg | Tablet
Allergy Care | Tablet | Allegra 180mg Tablets | Fexofenadine Hydrochloride 180 mg Tablet | Fexofenadine Hydrochloride | 180 | mg | Tablet


<hr>
<h3><strong>Conclusion</strong></h3>
<p>The above format and guidelines provide a standardised approach to uploading pharmaceutical data into the CareCode HIMS. Following these ensures smooth integration of inventory and prescribing modules, ultimately enhancing hospital operations.</p></body></html><!--EndFragment-->
</body>
</html>