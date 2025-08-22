# Purchase/GRN Search Report

## Overview

The Purchase/GRN Search Report allows pharmacy staff to search and view procurement records (purchases, Good Receive Notes, and donations) based on various criteria. This report provides two different views: bill-level summaries and detailed item-level information.

## When to Use

Use this report when you need to:
- Track procurement activities for a specific time period
- Find bills containing specific items
- Review purchase history for particular suppliers
- Generate reports for specific departments or institutions
- Export procurement data for analysis or auditing
- View purchase summaries or detailed item breakdowns

## How to Access

1. **Login** to the HMIS system
2. **Navigate** to Pharmacy module
3. **Click** on "Analytics" from the pharmacy menu
4. **Find** the "Procurement Reports" section
5. **Click** on "Item-wise Procurement" button

## How to Use

### Step 1: Set Search Criteria

#### Date Range (Required)
- **From Date**: Select the start date for your search
- **To Date**: Select the end date for your search
- Use the calendar picker to ensure correct date format

#### Filter Options (Optional)
- **Institution**: Select specific institution (leave blank for all)
- **Department**: Choose specific department (leave blank for all)  
- **Supplier**: Pick specific supplier (leave blank for all)
- **Item**: **MANDATORY** - You must select an item to search for bills containing that item

#### Report View Type (Required)
Choose your preferred view:
- **By Bills**: Shows complete bills that contain the selected item (bill-level totals)
- **By Bill Items**: Shows individual line items for the selected item

### Step 2: Run the Search

1. **Ensure** all required fields are filled (From Date, To Date, Item, Report View)
2. **Click** the green "Search" button
3. **Wait** for results to load

### Step 3: Review Results

#### By Bills View
Shows complete procurement bills containing your selected item:
- **Bill Number**: Internal reference number
- **Bill Date**: When the bill was created
- **Institution**: Where the procurement was made
- **Department**: Requesting department
- **Supplier**: Vendor or donor
- **Bill Type**: Type of procurement (GRN, Purchase, Donation, etc.)
- **Bill Total**: Complete bill amount
- **Net Total**: Amount after discounts
- **Discount**: Total discount applied

#### By Bill Items View
Shows detailed line items for the selected item:
- **Bill Number**: Reference to parent bill
- **Bill Date**: When the procurement occurred
- **Institution/Department/Supplier**: Same as above
- **Item**: The specific item name
- **Quantity**: Purchased quantity
- **Free Quantity**: Bonus quantity received
- **Total Quantity**: Sum of purchased and free quantities

### Step 4: Export or Print

1. **Click** "Excel" button to download spreadsheet
2. **Click** "Print" button to print the report
3. Use browser print options if needed

### Step 5: View Individual Bills

- **Click** "View" button next to any bill
- Opens the complete bill details in a new page
- Review all items, costs, and transaction information

## Understanding Messages

### Success Messages
- **"Search completed successfully"**: Results are displayed in the table below
- **"X records found"**: Shows the number of matching records

### Warning Messages
- **"Item selection is mandatory"**: You must choose an item before searching
- **"No results found"**: No bills match your criteria - try different dates or filters

### Error Messages
- **"Date range is required"**: Both From Date and To Date must be selected
- **"Invalid date range"**: To Date must be after From Date
- **"Not yet Supported"**: Item type not supported for this search

## Best Practices

### Effective Searching
1. **Start with broader criteria** then narrow down
2. **Use date ranges wisely** - shorter periods load faster
3. **Select items carefully** - search is case-sensitive
4. **Choose appropriate view** - Bills for summaries, Items for details

### Item Selection Tips
- **Type partial name** in Item field and select from dropdown
- **Use generic names** (e.g., "Paracetamol" instead of brand names)
- **Check spelling** - items must match exactly
- **Try different forms** if not found (tablet vs injection)

### Performance Tips
- **Use shorter date ranges** for faster searches
- **Filter by institution/department** when possible
- **Export large datasets** rather than viewing on screen
- **Close report when done** to free system resources

## Troubleshooting

### No Results Found
1. **Check date range** - expand if too narrow
2. **Verify item exists** in the selected timeframe
3. **Try different suppliers** or institutions
4. **Check for typos** in item name
5. **Use broader search terms**

### Slow Loading
1. **Reduce date range** to smaller periods
2. **Add more specific filters** (institution, department)
3. **Try during off-peak hours**
4. **Clear browser cache** if persistent

### Export Issues
1. **Ensure popup blockers** are disabled
2. **Check download folder** for saved files
3. **Try Print option** as alternative
4. **Contact IT support** if Excel export fails

### Navigation Problems
1. **Use "View" buttons** to see individual bills
2. **Use browser back button** to return to search
3. **Refresh page** if buttons not responding
4. **Clear browser cache** if navigation fails

## Configuration Options (Admin)

### Report Visibility Control
**Configuration Key:** `Pharmacy Analytics - Show Item-wise Procurement`
- **Default Value:** `true` (enabled)
- **Purpose:** Controls whether the "Item-wise Procurement" button appears in Pharmacy Analytics
- **Location:** System Administration → Configuration Options
- **Impact:** When disabled, users cannot access this report from the navigation menu

### Report Access Control
- User permissions control who can access this report
- Department restrictions may limit visible data
- Institution filtering applies based on user role

### Data Visibility
- Results limited to user's authorized institutions
- Date ranges may have system-imposed limits
- Export capabilities depend on user permissions

### Admin Setup Instructions
1. **Navigate to:** System Administration → Configuration Options
2. **Find:** "Pharmacy Analytics - Show Item-wise Procurement"
3. **Set Value:** 
   - `true` = Show button (default)
   - `false` = Hide button
4. **Save Configuration**
5. **Restart Application** (if required by your deployment)

## FAQ

**Q: Why must I select an item?**
A: The report specifically searches for bills containing that item. Without an item selection, the system cannot determine which bills to retrieve.

**Q: What's the difference between "By Bills" and "By Bill Items"?**
A: "By Bills" shows complete bills that contain your item with bill totals. "By Bill Items" shows only the line items for your specific item with quantities.

**Q: Can I search without selecting an item?**
A: No, item selection is mandatory for this report. Use other procurement reports for general bill searches.

**Q: Why do I see different totals between the two views?**
A: "By Bills" shows complete bill totals including all items. "By Bill Items" shows only quantities for your selected item.

**Q: Can I search for multiple items at once?**
A: No, select one item per search. Run multiple searches for different items if needed.

**Q: How do I find cancelled or refunded bills?**
A: The report includes all bill types (GRN, Purchase, Cancelled, Refund, Donation). Check the "Bill Type" column to identify the transaction type.

**Q: Why can't I see all institutions?**
A: Your user account may have restrictions. Contact your system administrator for access to additional institutions.