# Pharmacy Disposal Issue Search

## Overview
The Disposal Issue Search feature allows pharmacy staff to quickly find and review disposal issue bills and their items. This is essential for tracking medicines and supplies that have been issued to departments, monitoring disposal patterns, and maintaining accurate inventory records.

## When to Use
- **Finding specific disposal bills** by bill number or date range
- **Tracking items issued to departments** for inventory management
- **Reviewing disposal history** for audit purposes
- **Checking bill details** before processing returns or corrections
- **Monitoring disposal patterns** across departments

## How to Use

### Searching Disposal Bills
1. **Navigate to Search**
   - Go to Menu → Pharmacy → Search → Search Issue Bills

2. **Set Search Criteria**
   - **From Date/To Date**: Select the date range for your search
   - **Bill No**: Enter specific bill number if known
   - **Patient Name**: Leave blank (not applicable for disposal bills)
   - **From Department Name**: Enter the department that issued the items
   - **Total/Net Total**: Enter bill amounts if searching by value

3. **Execute Search**
   - Click the "Search" button
   - Results will display in a table below

4. **Review Results**
   - **Bill No**: Click to view detailed bill information
   - **From Department**: Department that issued the items
   - **To Department**: Department that received the items
   - **Billed At**: Date and time when bill was created
   - **Values**: Gross, discount, and net totals

### Searching Disposal Bill Items
1. **Navigate to Item Search**
   - Go to Menu → Pharmacy → Search → Search Issue Bill Items

2. **Set Search Criteria**
   - **From Date/To Date**: Select the date range
   - **Bill No**: Enter specific bill number
   - **Item Name**: Enter medicine or supply name
   - **Item Value**: Enter item value if searching by amount
   - **Department**: Enter issuing department name
   - **Item Code**: Enter specific item code

3. **Execute Search**
   - Click the "Search" button
   - Results show individual items from disposal bills

4. **Review Item Details**
   - **Bill No**: Click to view the complete bill
   - **Item Name**: Medicine or supply name with code
   - **Billed At**: When the disposal was processed
   - **Qty**: Quantity issued
   - **Item Value**: Value of the issued item
   - **To Department**: Receiving department

## Understanding Messages
- **No results found**: Check your date range and search criteria
- **Search completed**: Results are displayed in the table below
- **Loading**: System is processing your search request

## Best Practices
- **Use date ranges** to narrow down large result sets
- **Start with broader searches** then refine with specific criteria
- **Note department names** exactly as they appear in the system
- **Use item codes** for more precise item searches
- **Check both bill and item searches** for complete information

## Troubleshooting

**Problem: No search results appear**
- Verify the date range includes the period when disposals occurred
- Check that department names are spelled correctly
- Ensure you're searching in the correct date format

**Problem: Too many results to review**
- Narrow the date range to specific weeks or months
- Add department name filters
- Use specific bill numbers when known

**Problem: Can't find a specific disposal**
- Try searching by item name instead of bill number
- Check if the disposal was processed as a different transaction type
- Verify the date range covers when the disposal actually occurred

## FAQ

**Q: What types of disposals can I search for?**
A: You can search for regular disposals, cancelled disposals, and disposal returns.

**Q: Can I search across all departments?**
A: Yes, leave the department field blank to search across all departments.

**Q: How far back can I search?**
A: You can search as far back as your system's data retention policy allows.

**Q: Why do some bills show different values?**
A: Values may vary based on the costing method used and whether rates include taxes or discounts.

**Q: Can I export search results?**
A: Currently, you can view and print results. Export functionality may be available through the main reporting module.

## Related Features
- [Pharmacy Issue Bills](Pharmacy-Issue) - Creating disposal issue bills
- [Purchase GRN Search Report](Purchase-GRN-Search-Report) - Additional pharmacy search features
- [Ward Pharmacy BHT Substitute Functionality](Ward-Pharmacy-BHT-Substitute-Functionality) - Related pharmacy features

[Back](https://github.com/hmislk/hmis/wiki)
