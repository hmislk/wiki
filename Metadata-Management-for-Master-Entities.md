# Metadata Management for Master Entities

This document defines the UI structure, behaviour, and controller logic for CRUD operations in master metadata management within the application, applicable to all domain entities like `AMP`, `VMP`, `AMPP`, `VMPP`, `Services`, `Items`, etc.

## 🧩 UI Layout

### Left Panel:

* **Action Buttons (Top):**

  * `Add New` (icon: `fa-plus`)
  * `Edit` (icon: `fa-pen`)
  * `Delete` (icon: `fa-trash`, confirm required)

* **Selection Widget (Below Actions):**

  * `<p:autoComplete>` (if item count is high)
  * `<p:selectOneMenu>` (if item count is low)

### Right Panel:

* Displays all editable attributes of the selected entity.
* **Buttons (Bottom Right):**

  * `Save` (icon: `fa-save`, confirm on edit)
  * `Cancel` (icon: `fa-times`)

---

## 🔁 Behavioural Logic

### Add New

* Clears the current selection.
* Enables right-side inputs.
* Activates the `Cancel` button.
* Disables the left-side buttons (`Add New`, `Edit`, `Delete`, `Selection`).

### Edit

* Enabled only when an item is selected.
* Clicking `Edit`:

  * Enables right-side inputs for editing.
  * Disables left-side controls (to prevent state conflicts).
  * Enables the `Cancel` button.

### Cancel

* Reverts changes (unsaved edits or new item).
* Disables right-side inputs.
* Re-enables all left-side controls.
* Clears unsaved state.

### Save

* Validates input fields.
* If adding: persists a new entity.
* If editing: updates the existing entity.
* Re-initializes the entity list.
* Reverts to view-only mode and re-enables left-side controls.

### Delete

* Prompts user with confirmation.
* Soft-retirement (sets `retired = true` and adds metadata).
* Refreshes list post-deletion.

---

## 🔐 Controller Implementation (JSF Backing Bean)

* `prepareAdd()` → Prepares new instance.
* `saveSelected()` → Handles both `create` and `edit` logic.
* `delete()` → Handles soft deletion.
* `completeEntity(String query)` → Autocomplete logic.
* `getItems()` → Reloads list of active (non-retired) records.
* `recreateModel()` → Clears cached list on CRUD changes.

---

## ✅ Field Audit & Metadata

Each entity should support:

* `createdAt`, `creater`
* `retired`, `retiredAt`, `retirer`, `retireComments`

These fields are filled using `SessionController.getLoggedUser()` and `new Date()`.

---

## 💡 Example Entity: `Area`


```java
public void prepareAdd() {
    current = new Area(); // Create new
}

public void saveSelected() {
    if (current.getId() == null) {
        current.setCreatedAt(new Date());
        current.setCreater(sessionController.getLoggedUser());
        facade.create(current);
        JsfUtil.addSuccessMessage("Saved Successfully");
    } else {
        facade.edit(current);
        JsfUtil.addSuccessMessage("Updated Successfully");
    }
    recreateModel();
    items = null;
}
```

Yes, absolutely — that would be a valuable addition. Introducing the structural layout components like `<p:panel>`, `<p:panelGrid>`, `<div>` with Bootstrap classes, and how they interoperate will help your team or future contributors better understand how the CRUD interface is constructed and styled.

You could include a section titled **“📦 UI Layout Components Explained”** in the Wiki right after the behaviour section. Here's how you could structure that:

---

## 📦 UI Layout Components Explained

This section explains the layout components used to implement metadata CRUD screens such as AMP, AMPP, VMP, VMPP, and Services.

### `<p:panel>`

Wraps a segment of the interface with a titled panel container.

```xhtml
<p:panel header="Manage AMPPs">
    <!-- Content here -->
</p:panel>
```

* Used to group the entire left + right panel structure with a contextual title.
* Useful for collapsible sections or when embedding within tabs.

### `<div class="row">` & `<div class="col-md-x">`

Bootstrap-based grid used to place the left and right sides in parallel.

```xhtml
<div class="row">
    <div class="col-md-5"> <!-- Left -->
    <div class="col-md-7"> <!-- Right -->
```

* Always wrap with `row` and then divide into `col-md-x` based on ratio (e.g., 5:7).
* Ensures responsiveness and clean spacing.

### `<p:panelGrid>`

Used for aligned label-control pairs.

```xhtml
<p:panelGrid columns="2" columnClasses="w-25, w-75">
    <h:outputText value="Name"/>
    <p:inputText value="#{controller.current.name}"/>
</p:panelGrid>
```

* Inner grids (e.g., `gpDetailText`) handle label-input layout.
* Outer grids (e.g., `gpDetail`) organize groups like buttons, descriptions, or sub-sections.

### `<p:commandButton>`

Bootstrap classes like `w-25`, `m-1`, and PrimeFaces `ui-button-*` ensure compact styling:

```xhtml
<p:commandButton value="Add" class="m-1 ui-button-success w-25"/>
```

* Use `m-1` for spacing, `w-25` to control width, and `ui-button-*` for intent.
* Always include `icon="fa fa-*"`, not just `value`, for clarity and consistency.

### General Guidelines

* Control layout with Bootstrap classes for predictable spacing (`m-1`, `w-100`, `form-control`).
* Avoid custom CSS unless unavoidable.

---

I can update the full wiki file or render this into a downloadable `.md` or GitHub Wiki format if you'd like. Let me know how you'd like to proceed.


---



## 🎯 Notes

* Always disable conflicting actions (e.g., `Add` while editing).
* Cancel must fully reset to avoid accidental partial updates.
* JSF view should be aligned with PrimeFaces behavior and avoid plain JavaScript unless necessary.
* Use Bootstrap and FontAwesome consistently for layout and iconography.

[Back](https://github.com/hmislk/hmis/wiki/Developer-Guidelines)