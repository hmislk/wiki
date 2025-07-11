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

---

## 🎯 Notes

* Always disable conflicting actions (e.g., `Add` while editing).
* Cancel must fully reset to avoid accidental partial updates.
* JSF view should be aligned with PrimeFaces behavior and avoid plain JavaScript unless necessary.
* Use Bootstrap and FontAwesome consistently for layout and iconography.

[Back](https://github.com/hmislk/hmis/wiki/Developer-Guidelines)