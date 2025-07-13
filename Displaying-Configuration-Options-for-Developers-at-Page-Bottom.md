## Displaying Configuration Options for Developers at Page Bottom

### Purpose

To support debugging, development, and transparency, pages can be enhanced to display their configuration options (defined in the `ConfigOptionApplicationController`) at the bottom of the page. This feature is visible **only** to users with the `Developers` privilege.

---

### How Configuration Options Are Used

#### In JSF Pages

```xhtml
<pharmacy:direct_purhcase_with_costing
    bill="#{pharmacyDirectPurchaseController.bill}"
    ShowProfit="#{configOptionApplicationController.getBooleanValueByKey('Show Profit % in Direct Purchase Bill', true)}"
    ShowRetailValue="#{configOptionApplicationController.getBooleanValueByKey('Show Retail Value in Direct Purchase Bill', true)}" />
```

#### In Java Controllers

```java
if (configOptionApplicationController.getBooleanValueByKey("Allow to Denomination for shift Starting Process", false)) {
    denominationTransactions = denominationTransactionController.createDefaultDenominationTransaction();
}
```

---

### Developer Privilege Check in JSF

Ensure developer-only content is rendered as below:

```xhtml
<ui:fragment rendered="#{webUserController.hasPrivilege('Developers')}">
    <!-- Developer-specific content -->
</ui:fragment>
```

---

### Step-by-Step Implementation

#### 1. **Create ConfigOptionInfo Inner Class**

In the relevant Controller (e.g., `TransferReceiveController`):

```java
public static class ConfigOptionInfo {
    private final String key;
    private final String defaultValue;
    private final String currentValue;

    public ConfigOptionInfo(String key, String defaultValue, String currentValue) {
        this.key = key;
        this.defaultValue = defaultValue;
        this.currentValue = currentValue;
    }

    public String getKey() { return key; }
    public String getDefaultValue() { return defaultValue; }
    public String getCurrentValue() { return currentValue; }
}
```

#### 2. **Add Method to List Config Options**

Example:

```java
public List<ConfigOptionInfo> getConfigOptionsForDevelopers() {
    List<ConfigOptionInfo> list = new ArrayList<>();
    list.add(new ConfigOptionInfo(
        "Pharmacy Transfer is by Purchase Rate",
        "false",
        configOptionApplicationController.getStringValueByKey("Pharmacy Transfer is by Purchase Rate", "false")
    ));
    list.add(new ConfigOptionInfo(
        "Report Font Size of Item List in Pharmacy Disbursement Reports",
        "10pt",
        configOptionApplicationController.getStringValueByKey("Report Font Size of Item List in Pharmacy Disbursement Reports", "10pt")
    ));
    // Add more keys as needed
    return list;
}
```

---

### 3. **Add Developer Panel to XHTML Page**

At the bottom of the relevant XHTML page:

```xhtml
<p:panel rendered="#{webUserController.hasPrivilege('Developers')}">
    <f:facet name="header">
        <h:outputLabel value="Configuration Options" />
    </f:facet>
    <p:dataTable value="#{yourController.configOptionsForDevelopers}" var="opt" style="min-width:100%">
        <p:column headerText="Option Key">
            <h:outputText value="#{opt.key}" />
        </p:column>
        <p:column headerText="Default Value">
            <h:outputText value="#{opt.defaultValue}" />
        </p:column>
        <p:column headerText="Current Value">
            <h:outputText value="#{opt.currentValue}" />
        </p:column>
    </p:dataTable>
</p:panel>
```

---

### Optional Enhancements

* Extract developer panel into a reusable composite or fragment for reuse.
* Add filtering input for long option lists.
* Allow temporary override of config values for Developer testing (if security permits).

---

### Notes

* Keep configuration keys consistent and meaningful.
* Add all config options affecting visual or logical behaviour to the Developer panel.
* Ensure config visibility does not interfere with page styling or break user flows.

---
[Back](https://github.com/hmislk/hmis/wiki/Code-Concepts-for-Developers)
