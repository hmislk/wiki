# Organisational Structure: Institution, Site, and Department

CareCode HIMS is designed to support complex healthcare environments where multiple entities may operate under shared infrastructure. To facilitate accurate data separation, permissions, reporting, and financial tracking, the system uses three core structural entities: **Institution**, **Site**, and **Department**.

---

## 🏢 Institution

An **Institution** represents a legal or business entity that owns or operates one or more healthcare services.

**Examples:**

* Ruhunu Hospital Pvt Ltd
* Ruhunu Diagnostics Pvt Ltd
* Ruhunu Pharmaceuticals

Each institution is uniquely identifiable and maintains its own:

* Administrative structure
* Financial reporting
* User hierarchy

---

## 📍 Site

A **Site** refers to a **physical location** or campus where one or more departments operate.

**Examples:**

* Matara Ruhunu Hospital
* Galle Central Collection Centre

> 🔄 **Note:** Multiple institutions can **share a single site**. For example, both Ruhunu Diagnostics and Ruhunu Hospital may operate from the same Matara campus.

---

## 🧪 Department

A **Department** is a functional unit within an institution that provides a specific service. Each department is:

* **Always attached to a single institution**
* **Always located at a single site**

**Examples:**

* Karapitiya RHD Laboratory
* Karapitiya OPD Pharmacy
* Matara X-Ray Unit

> 🔒 Departments are never shared between institutions or sites. Each one belongs strictly to **one institution** and **one site**.

---

## Summary Table

| Entity      | Description                         | Shared Across |
| ----------- | ----------------------------------- | ------------- |
| Institution | Legal or business entity            | ❌ No          |
| Site        | Physical location or campus         | ✅ Yes         |
| Department  | Functional sub-unit (Lab, Pharmacy) | ❌ No          |

---

[🔙 Back to Knowledgebase](https://github.com/hmislk/hmis/wiki/Knowledgebase)



[Back](https://github.com/hmislk/hmis/wiki)
