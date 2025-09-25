# Copiar Documento de Origen a Referencia de DTE (Chile)
========================================================

## Descripción

Este módulo, diseñado específicamente para la **Localización Chilena**, automatiza el proceso de rellenar la sección de referencias de la factura electrónica (DTE) con los datos de la orden de compra.

El módulo copia el valor del campo **Documento de Origen** ('origin') del pedido de venta a la sección de referencias del **Documento Tributario Electrónico (DTE)**, utilizando el **código de referencia 801 (Orden de Compra)**.

Adicionalmente, la fecha de la orden de compra para esta referencia se establece automáticamente con la **Fecha del Pedido de Venta**. Si la fecha real de la orden de compra es diferente, debe ser actualizada manually en la factura antes de su validación.

Esta funcionalidad agiliza el proceso de facturación para empresas en Chile, asegurando que el número de la orden de compra del cliente se referencie correctamente en el DTE, un requisito común para muchos clientes.

---

## Localización

* **Chile**

---

## Instalación

1.  Descargue los archivos del módulo.
2.  Copie la carpeta del módulo a su directorio de 'addons' de Odoo.
3.  Reinicie el servidor de Odoo.
4.  Vaya a **Aplicaciones** en su instancia de Odoo.
5.  Haga clic en **Actualizar Lista de Aplicaciones**.
6.  Busque el módulo y haga clic en **Instalar**.

---

## Uso

1.  Navegue al módulo de **Ventas** y cree un nuevo Pedido de Venta.
2.  En el campo **Documento de Origen**, ingrese el número de la Orden de Compra (OC) del cliente.
3.  Confirme el Pedido de Venta y cree la factura correspondiente.
4.  Una vez creada la factura en estado borrador, navegue a la pestaña **Referencias Cruzadas de Documentos**.
5.  Observará una nueva línea creada automáticamente con los siguientes detalles:
    * **Nro documento origen**: El valor que ingresó en el campo **Documento de Origen**.
    * **Tipo de documento SII**: Aparecerá '(801) Orden de Compra'.
    * **Código de referencia SII**: Estará vacío.
    * **Motivo**: Estará vacío.
    * **Fecha**: La fecha del Pedido de Venta.
6.  Si la fecha de la Orden de Compra es distinta a la del Pedido de Venta, puede cambiarla manualmente en esta sección antes de validar la factura y emitir el DTE.

# Copy Source Document to Chilean E-Invoice (DTE)
=================================================

## Description

This module, designed specifically for the **Chilean Localization**, automates the process of populating the electronic invoice's cross-reference field with the purchase order details.

It copies the value from the sales order's **Source Document** ('origin') field to the cross-reference section of the electronic invoice (**DTE - Documento Tributario Electrónico**) using **reference code 801 (Orden de Compra)**.

Additionally, the purchase order date for the cross-reference is automatically set to the **Sale Order's Date**. If the actual purchase order date differs, it must be updated manually on the invoice before validation.

This functionality streamlines the invoicing process for Chilean companies by ensuring that the purchase order number is correctly referenced in the DTE, a common requirement for clients.

---

## Target Localization

* **Chile**

---

## Installation

1.  Download the module files.
2.  Copy the module folder to your Odoo 'addons' directory.
3.  Restart the Odoo server.
4.  Go to **Apps** in your Odoo instance.
5.  Click on **Update Apps List**.
6.  Search for the module and click **Install**.

---

## Usage

1.  Navigate to the **Sales** module and create a new Sales Order.
2.  In the **Source Document** field, enter the customer's Purchase Order number.
3.  Confirm the Sales Order and create the corresponding invoice.
4.  Once the draft invoice is created, navigate to the **Document Cross-References** tab.
5.  You will see a new line automatically created with the following details:
    * **Origin Document No.**: The value you entered in the **Source Document** field.
    * **SII Document Type**: Will show '(801) Purchase Order'.
    * **SII Reference Code**: This will be empty.
    * **Reason**: This will be empty.
    * **Date**: The date of the Sales Order.
6.  If the date of the Purchase Order is different from the Sales Order's date, you can manually change it in this section before validating the invoice and issuing the DTE.
