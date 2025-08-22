# Pharmacy Disposal Reports

## Overview
The Disposal Reports feature provides comprehensive analytics and reporting capabilities for pharmacy disposal operations. These reports help pharmacy staff track disposal patterns, monitor department-wise distributions, and analyze item usage for audit and inventory management purposes.

## When to Use
- **Monthly audit reports** for disposal activities
- **Department performance analysis** to track distribution patterns
- **Item usage analysis** for inventory planning and control
- **Financial reporting** for disposal operation costs and margins
- **Compliance reporting** for regulatory requirements

## Navigation Paths

### Search Reports
For searching specific disposal bills and items:
- **Menu → Pharmacy → Disposal → Search Disposal Bills**
- **Menu → Pharmacy → Disposal → Search Disposal Items**

### Analytics Reports
For comprehensive disposal analytics:
- **Menu → Pharmacy → Analytics → Disposal Reports**

## Available Reports

### 1. Unit Issue by Bill
**Purpose**: View disposal bills with summary information
**Navigation**: Menu → Pharmacy → Analytics → Disposal Reports → Unit Issue by bill

**How to Use**:
1. Set date range (From/To dates)
2. Optionally select Issue From department
3. Optionally select Issue To department
4. Click "Fill" to generate report
5. Export to Excel or Print as needed

**Report Shows**:
- Bill numbers and invoice numbers
- Bill creation dates
- Gross, margin, and net values
- Department information

### 2. Unit Issue by Department
**Purpose**: Analyze disposal patterns by department
**Navigation**: Menu → Pharmacy → Analytics → Disposal Reports → Unit Issue by Department

**How to Use**:
1. Set date range (From/To dates)
2. Select Issue From department
3. Click "Fill" to generate report

**Report Shows**:
- Department-wise disposal totals
- Net values by receiving department
- Summary totals for the selected period

### 3. Unit Issue by Item (Batch)
**Purpose**: Detailed item analysis with batch information
**Navigation**: Menu → Pharmacy → Analytics → Disposal Reports → Unit Issue by Item (Batch)

**How to Use**:
1. Set date range (From/To dates)
2. Select From Department and To Department
3. Optionally select Item Category to filter results
4. Click "Fill" to generate report

**Report Shows**:
- Item names and batch numbers
- Purchase rates and retail rates
- Quantity counts and values
- Margin calculations
- Gross and net values with totals

### 4. Unit Issue by Item
**Purpose**: Item-level analysis without batch details
**Navigation**: Menu → Pharmacy → Analytics → Disposal Reports → Unit Issue by Item

**How to Use**:
1. Set date range (From/To dates)
2. Select From Department and To Department
3. Optionally select Item Category
4. Click "Fill" to generate report

**Report Shows**:
- Item names and quantities
- Net values per item
- Summary totals for the period

## Understanding the Reports

### Key Terms
- **Unit Issue**: Disposal of items from pharmacy to departments
- **From Department**: Department issuing/disposing items (usually pharmacy)
- **To Department**: Department receiving the disposed items
- **Gross Value**: Total value before discounts
- **Net Value**: Final value after all adjustments
- **Margin Value**: Profit margin on disposed items

### Report Features
- **Date Filtering**: All reports support date range filtering
- **Department Filtering**: Filter by issuing or receiving departments
- **Category Filtering**: Available in item reports for specific drug categories
- **Export Options**: Excel export and print functionality
- **Summary Totals**: Automatic calculation of totals and subtotals

## Best Practices

### Report Generation
- **Use appropriate date ranges** - broader ranges for trends, narrower for detailed analysis
- **Filter by department** when analyzing specific department performance
- **Use category filters** to focus on specific types of medications
- **Generate regular reports** for consistent monitoring

### Data Analysis
- **Compare monthly patterns** to identify trends
- **Monitor high-value disposals** for cost control
- **Track department usage** for resource planning
- **Review batch information** for expiry and quality control

### Export and Documentation
- **Export to Excel** for further analysis and record keeping
- **Print reports** for physical documentation
- **Save report parameters** for consistent reporting periods
- **Document unusual patterns** for investigation

## Troubleshooting

**Problem: No data appears in reports**
- Verify the date range includes disposal activities
- Check that selected departments have disposal transactions
- Ensure disposal bills were properly processed in the system

**Problem: Incorrect totals or values**
- Verify bill processing was completed correctly
- Check for cancelled or returned disposals in the period
- Ensure proper bill type selection (disposal vs. other transactions)

**Problem: Missing department or item data**
- Confirm department names are correctly entered
- Verify item categories are properly assigned
- Check that disposal transactions included all required information

**Problem: Export or print issues**
- Ensure browser allows pop-ups for print functionality
- Check Excel is available for export features
- Verify sufficient data exists before attempting export

## FAQ

**Q: What types of disposal transactions are included?**
A: Reports include regular disposals, cancelled disposals, and disposal returns for comprehensive tracking.

**Q: Can I filter by specific items or medications?**
A: Yes, use the Item Category filter in item reports, or use the Search Disposal Items feature for specific item searches.

**Q: How far back can I generate reports?**
A: Reports can go back as far as your system's data retention policy allows, typically several years.

**Q: What's the difference between batch and non-batch item reports?**
A: Batch reports show detailed batch information including purchase/retail rates and batch numbers. Non-batch reports focus on item quantities and net values only.

**Q: Can I schedule automatic report generation?**
A: Currently, reports are generated on-demand. Contact your system administrator for automated reporting options.

**Q: Why do values differ between different report types?**
A: Different reports may include different components (gross vs. net values, margins, etc.). Check the report description to understand what values are included.

## Related Features
- [Pharmacy Disposal Issue Search](Disposal-Issue-Search) - Search specific disposal bills and items
- [Pharmacy Issue Bills](Pharmacy-Issue) - Creating disposal issue bills
- [Pharmacy Analytics](Pharmacy-Analytics) - Other pharmacy reporting features
- [Inventory Management](Inventory-Management) - Overall inventory tracking

## Technical Notes
This feature uses optimized DTO-based queries for improved performance and uses proper disposal bill type filtering (BillTypeAtomic.PHARMACY_DISPOSAL_ISSUE) for accurate reporting.