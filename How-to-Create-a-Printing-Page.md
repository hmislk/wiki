# How to Create a Printing Page

The system has several receipts / bills to print: OPD Bills, Pharmacy Retail Sale Bills, Pharmacy Adjustment Bills, etc.

The different installations have different printers, paper sizes and configuration requirements.

A new **flexible configuration method** is introduced to handle the customization efficiently.

## New Flexible Configuration System

CSS styles, headers, and footers are stored as configuration options. They are loaded at the onset of the application. The system now provides:

1. **Common Default Configurations** - Fallback settings used when specific configurations are not available
2. **Specific Bill Type Configurations** - Individual settings for each bill type that can be customized independently
3. **Automatic Fallback Logic** - If a specific configuration is empty, the system automatically uses the common default

### Configuration Architecture

#### Common Default Settings
- `Pharmacy Common Bill CSS` - Default CSS used by all pharmacy bills
- `Pharmacy Common Bill Header` - Default header content
- `Pharmacy Common Bill Footer` - Default footer content

#### Specific Bill Type Settings
For different bill types, you can create specific configurations:

**Pharmacy Adjustments:**
- `Pharmacy Adjustment Purchase Rate CSS/Header/Footer`
- `Pharmacy Adjustment Cost Rate CSS/Header/Footer`
- `Pharmacy Adjustment Retail Rate CSS/Header/Footer`
- `Pharmacy Adjustment Stock CSS/Header/Footer`
- `Pharmacy Adjustment Wholesale Rate CSS/Header/Footer`

**Other Pharmacy Bills:**
- `Pharmacy Issue Receipt CSS/Header/Footer`
- `Pharmacy Transfer Issue Receipt CSS/Header/Footer`
- `Pharmacy Transfer Receive Receipt CSS/Header/Footer`
- And many more...

### Implementation in ConfigOptionApplicationController

```java
@Named
@ApplicationScoped
public class ConfigOptionApplicationController implements Serializable {

    @PostConstruct
    public void init() {
        loadApplicationOptions();
    }

    public void loadApplicationOptions() {
        applicationOptions = new HashMap<>();
        List<ConfigOption> options = getApplicationOptions();
        for (ConfigOption option : options) {
            applicationOptions.put(option.getOptionKey(), option);
        }
        loadEmailGatewayConfigurationDefaults();
        loadPharmacyConfigurationDefaults();
        loadPharmacyIssueReceiptConfigurationDefaults();
        loadPharmacyCommonBillConfigurationDefaults();  // NEW: Common defaults
        loadPharmacyAdjustmentReceiptConfigurationDefaults();  // NEW: Specific adjustments
    }

    // NEW: Common default configuration loader
    private void loadPharmacyCommonBillConfigurationDefaults() {
        getLongTextValueByKey("Pharmacy Common Bill CSS",
                ".receipt-container {\n"
                + "    font-family: Verdana, sans-serif;\n"
                + "    font-size: 12px;\n"
                + "    color: #000;\n"
                + "    width: 21cm;\n"
                + "    margin: auto;\n"
                + "    page-break-inside: avoid;\n"
                + "}\n"
                + ".receipt-header {\n"
                + "    margin-bottom: 15px;\n"
                + "    text-align: center;\n"
                + "}\n"
                + ".receipt-institution-name {\n"
                + "    font-weight: bold;\n"
                + "    font-size: 18px;\n"
                + "    margin-bottom: 5px;\n"
                + "}\n"
                + ".receipt-institution-contact {\n"
                + "    font-size: 10px;\n"
                + "    margin-bottom: 10px;\n"
                + "}\n"
                + ".receipt-title {\n"
                + "    text-align: center;\n"
                + "    font-size: 16px;\n"
                + "    font-weight: bold;\n"
                + "    margin: 15px 0;\n"
                + "    text-decoration: underline;\n"
                + "}\n"
                + ".receipt-separator {\n"
                + "    margin: 10px 0;\n"
                + "    border-top: 1px solid #333;\n"
                + "}\n"
                + ".receipt-details-table {\n"
                + "    width: 100%;\n"
                + "    margin-bottom: 15px;\n"
                + "    border-collapse: collapse;\n"
                + "}\n"
                + ".receipt-details-table td {\n"
                + "    padding: 3px 5px;\n"
                + "    vertical-align: top;\n"
                + "}\n"
                + ".receipt-details-table td:first-child {\n"
                + "    font-weight: bold;\n"
                + "    width: 20%;\n"
                + "}\n"
                + ".receipt-details-table td:nth-child(2) {\n"
                + "    width: 5%;\n"
                + "    text-align: center;\n"
                + "}\n"
                + ".noBorder, .noBorder td, .noBorder th {\n"
                + "    border: none !important;\n"
                + "}\n"
                + ".normalFont {\n"
                + "    font-size: 12px;\n"
                + "}\n"
                + ".text-end {\n"
                + "    text-align: right;\n"
                + "}\n"
                + "@media print {\n"
                + "    .receipt-container {\n"
                + "        margin: 0;\n"
                + "        page-break-after: always;\n"
                + "    }\n"
                + "}\n"
        );
        getLongTextValueByKey("Pharmacy Common Bill Header", "");
        getLongTextValueByKey("Pharmacy Common Bill Footer", "");
    }

    // NEW: Specific adjustment configurations (initially empty, can be customized)
    private void loadPharmacyAdjustmentReceiptConfigurationDefaults() {
        // Purchase Rate Adjustment specific configurations
        getLongTextValueByKey("Pharmacy Adjustment Purchase Rate CSS", "");
        getLongTextValueByKey("Pharmacy Adjustment Purchase Rate Header", "");
        getLongTextValueByKey("Pharmacy Adjustment Purchase Rate Footer", "");
        
        // Cost Rate Adjustment specific configurations
        getLongTextValueByKey("Pharmacy Adjustment Cost Rate CSS", "");
        getLongTextValueByKey("Pharmacy Adjustment Cost Rate Header", "");
        getLongTextValueByKey("Pharmacy Adjustment Cost Rate Footer", "");
        
        // Retail Rate, Stock, Wholesale Rate configurations...
        // (All start empty and can be customized independently)
    }

    // NEW: Fallback helper methods
    public String getPharmacyBillCSSWithFallback(String specificKey) {
        String specificCSS = getLongTextValueByKey(specificKey);
        if (specificCSS != null && !specificCSS.trim().isEmpty()) {
            return specificCSS;
        }
        return getLongTextValueByKey("Pharmacy Common Bill CSS");
    }

    public String getPharmacyBillHeaderWithFallback(String specificKey) {
        String specificHeader = getLongTextValueByKey(specificKey);
        if (specificHeader != null && !specificHeader.trim().isEmpty()) {
            return specificHeader;
        }
        return getLongTextValueByKey("Pharmacy Common Bill Header");
    }

    public String getPharmacyBillFooterWithFallback(String specificKey) {
        String specificFooter = getLongTextValueByKey(specificKey);
        if (specificFooter != null && !specificFooter.trim().isEmpty()) {
            return specificFooter;
        }
        return getLongTextValueByKey("Pharmacy Common Bill Footer");
    }

    // Original method for backward compatibility
    private void loadPharmacyIssueReceiptConfigurationDefaults() {
        getLongTextValueByKey("Pharmacy Issue Receipt CSS",
                ".receipt-container {\n"
                + "    font-family: Verdana, sans-serif;\n"
                + "    font-size: 12px;\n"
                + "    color: #000;\n"
                + "}\n"
                + ".receipt-header, .receipt-title, .receipt-separator, .receipt-summary {\n"
                + "    margin-bottom: 10px;\n"
                + "}\n"
                + ".receipt-institution-name {\n"
                + "    font-weight: bold;\n"
                + "    font-size: 16px;\n"
                + "    text-align: center;\n"
                + "}\n"
                + ".receipt-institution-contact {\n"
                + "    text-align: center;\n"
                + "    font-size: 11px;\n"
                + "}\n"
                + ".receipt-title {\n"
                + "    text-align: center;\n"
                + "    font-size: 14px;\n"
                + "    font-weight: bold;\n"
                + "    text-decoration: underline;\n"
                + "}\n"
                + ".receipt-details-table, .receipt-items-table, .receipt-summary-table {\n"
                + "    width: 100%;\n"
                + "    border-collapse: collapse;\n"
                + "}\n"
                + ".receipt-items-header {\n"
                + "    font-weight: bold;\n"
                + "    border-bottom: 1px solid #ccc;\n"
                + "}\n"
                + ".item-name, .item-qty, .item-rate, .item-value {\n"
                + "    padding: 4px;\n"
                + "    text-align: left;\n"
                + "}\n"
                + ".item-qty, .item-rate, .item-value {\n"
                + "    text-align: right;\n"
                + "}\n"
                + ".summary-label {\n"
                + "    font-weight: bold;\n"
                + "}\n"
                + ".summary-value {\n"
                + "    text-align: right;\n"
                + "    font-weight: bold;\n"
                + "}\n"
                + ".total-amount {\n"
                + "    font-size: 14px;\n"
                + "    font-weight: bold;\n"
                + "}\n"
                + ".receipt-cashier {\n"
                + "    margin-top: 20px;\n"
                + "    text-align: right;\n"
                + "    text-decoration: overline;\n"
                + "}"
            );
    }
}
```

## Updated Composite Component Pattern

### New Flexible Approach (Recommended)

This example shows how to use the new flexible configuration system with automatic fallbacks:

```xml
<?xml version='1.0' encoding='UTF-8' ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:cc="http://xmlns.jcp.org/jsf/composite"
      xmlns:f="http://xmlns.jcp.org/jsf/core"
      xmlns:h="http://xmlns.jcp.org/jsf/html"
      xmlns:ui="http://xmlns.jcp.org/jsf/facelets">

    <!-- INTERFACE -->
    <cc:interface>
        <cc:attribute name="bill" />
    </cc:interface>

    <!-- IMPLEMENTATION -->
    <cc:implementation>

        <!-- NEW: Use fallback methods for CSS -->
        <style>
            <h:outputText escape="false"
            value="#{configOptionApplicationController.getPharmacyBillCSSWithFallback('Pharmacy Adjustment Purchase Rate CSS')}"/>
        </style>

        <!-- NEW: Use fallback methods for Header -->
        <h:outputText escape="false"
                      value="#{configOptionApplicationController.getPharmacyBillHeaderWithFallback('Pharmacy Adjustment Purchase Rate Header')}"/>

        <div class="receipt-container">
            <div class="receipt-header">
                <div class="receipt-institution-name">
                    <h:outputLabel value="#{cc.attrs.bill.department.printingName}" />
                </div>
                <div class="receipt-institution-contact">
                    <h:outputLabel value="#{cc.attrs.bill.department.address}" /><br />
                    <h:outputLabel value="#{cc.attrs.bill.department.telephone1}" />
                    <h:outputLabel value=" #{cc.attrs.bill.department.telephone2}" /><br />
                    <h:outputLabel value="#{cc.attrs.bill.department.fax}" />
                </div>
            </div>

            <div class="receipt-title">
                <h:outputLabel value="Purchase Rate Adjustment Note" />
            </div>

            <div class="receipt-separator"><hr /></div>

            <!-- Bill content goes here -->
            
        </div>

        <!-- NEW: Use fallback methods for Footer -->
        <h:outputText escape="false"
                      value="#{configOptionApplicationController.getPharmacyBillFooterWithFallback('Pharmacy Adjustment Purchase Rate Footer')}"/>
    </cc:implementation>
</html>
```

### Original Approach (Still Supported)

For existing bills that have specific configurations:

```xml
<style>
    <h:outputText escape="false"
    value="#{configOptionApplicationController.getLongTextValueByKey('Pharmacy Issue Receipt CSS')}"/>
</style>

<h:outputText escape="false"
              value="#{configOptionApplicationController.getLongTextValueByKey('Pharmacy Issue Receipt Header')}"/>
```

## Benefits of the New System

1. **Scalability**: Handles hundreds of bill types without requiring individual configuration for each
2. **Flexibility**: Each bill type can be customized independently when needed
3. **Maintainability**: Common defaults reduce duplication and simplify management
4. **Backward Compatibility**: Existing configurations continue to work unchanged
5. **Automatic Fallback**: No need to configure every bill type - common defaults are used automatically

## Usage in Pages

The composite is called from the relevant page like below:

```xml
<h:panelGroup id="gpBillPreview">
    <phi:pharmacy_issue_receipt bill="#{pharmacyIssueController.printBill}"/>
</h:panelGroup>
```

For adjustment bills:

```xml
<h:panelGroup id="print">
    <ph:adjustmentBill_purchase_price bill="#{pharmacyAdjustmentController.deptAdjustmentPreBill}" />
</h:panelGroup>
```

## Configuration Management

Administrators can:
1. Start with common default configurations that work for all bills
2. Customize specific bill types only when needed (e.g., different CSS for purchase rate vs stock adjustments)
3. Modify common defaults to affect all uncustomized bills at once
4. Override specific configurations for individual bill types when required

[Back](https://github.com/hmislk/hmis/wiki/Developer-Manual)